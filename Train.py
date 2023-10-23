import os
import gc
import pandas as pd
import numpy as np
import keras.backend as K
from Normalizer import Normalizer
from GRUTrainer import GRUTrainer


class Train:
    def __init__(self, data, symbols, batch_size=50):
        self.data = data
        self.symbols = symbols
        self.batch_size = batch_size


    def write_log(self, log_file, idx, symbol, X_train, X_test, y_train, sc, df_prediction):
        log_file.write(f"Symbol {idx + 1} of {len(self.symbols)} ({symbol}) processing...\n")
        log_file.write(f"X_train shape: {X_train.shape}\n")
        log_file.write(f"y_train shape: {y_train.shape}\n")
        log_file.write(f"X_test shape: {X_test.shape}\n")
        log_file.write(f"NaN in X_train: {np.isnan(X_train).sum()}\n")
        log_file.write(f"NaN in y_train: {np.isnan(y_train).sum()}\n")
        log_file.write(f"NaN in X_test: {np.isnan(X_test).sum()}\n")
        log_file.write(f"sc min_: {sc.min_}\n")
        log_file.write(f"sc scale_: {sc.scale_}\n")
        log_file.write(f"NaN in df_prediction: {df_prediction.isna().sum().sum()}\n")


    def clear_mem(self, var_list):
        for var in var_list:
            del var
        gc.collect()
            

    def read_X_y(self, symbol):
        X_path = os.path.join("data/train", f"train_{symbol}.csv")
        y_path = os.path.join("data/test", f"test_{symbol}.csv")
        cond = os.path.exists(X_path) and os.path.exists(y_path)        
        if cond:
            return pd.read_csv(X_path), pd.read_csv(y_path)
        else:
            return None, None


    def train_and_save(self):
        os.makedirs("data/model", exist_ok=True)
        os.makedirs("data/pred", exist_ok=True)
        
        gru = GRUTrainer()
        log_file = open("debug_logs.txt", "w")
        
        for idx, symbol in enumerate(self.symbols):
            print(f"Processing Symbol {idx+1} of {len(self.symbols)} ({symbol})")
            
            # 모델 초기화
            K.clear_session()
            
            # 모델 재시작
            gru.initialize_model()

            # 심볼별 csv 파일을 불러옵니다.
            X, y = self.read_X_y(symbol)
            if X is not None and y is not None:
                # 데이터 전처리
                X_train, y_train, X_test, sc = Normalizer(X, y, time_steps=5, for_periods=2).normalize()

                # 모델 학습 및 예측
                prediction = gru.train(X_train, y_train, X_test, sc)

                # 예측 값만 저장
                df_prediction = pd.DataFrame({
                    'Adj Close': prediction[:min(len(prediction), len(y)-1), 0]
                })

                # 예측 결과를 CSV로 저장
                df_prediction.to_csv(os.path.join("data/pred", f"pred_{symbol}.csv"), index=False)
                
                # 로그 기록
                self.write_log(log_file, idx, symbol, X_train, X_test, y_train, sc, df_prediction)
            else:
                # 에러 출력
                print(f"{symbol}에 해당하는 csv 파일을 찾을 수 없습니다.")
                
                # 로그 기록
                log_file.write(f"{symbol}에 해당하는 csv 파일을 찾을 수 없습니다.\n")
            
            # 메모리 정리
            self.clear_mem([X, y, X_train, y_train, X_test, sc, prediction, df_prediction])

        # 로그 기록 종료
        log_file.close()
import os
import pandas as pd
import numpy as np
from Normalize import Normalize
from GRUTrainer import GRUTrainer

class Train:

    def __init__(self, symbols):
        self.symbols = symbols  # 일차원 리스트

    def train_and_save_models(self):
        os.makedirs("data/model", exist_ok=True)
        os.makedirs("data/pred", exist_ok=True)
        log_file = open("debug_logs.txt", "w")

        for idx, symbol in enumerate(self.symbols):  # 일차원 리스트를 순회
            print(f"Symbol {idx + 1} of {len(self.symbols)} ({symbol}) processing...")
            log_file.write(f"Symbol {idx + 1} of {len(self.symbols)} ({symbol}) processing...\n")

            # GRU 모델 초기화
            gru = GRUTrainer()

            # 심볼별 csv 파일을 불러옵니다.
            X_file_path = os.path.join("data/train", f"train_{symbol}.csv")
            y_file_path = os.path.join("data/test", f"test_{symbol}.csv")

            if os.path.exists(X_file_path) and os.path.exists(y_file_path):
                X = pd.read_csv(X_file_path)
                y = pd.read_csv(y_file_path)

                # 데이터 전처리
                normalizer = Normalize(X, y, time_steps=5, for_periods=2)
                X_train, y_train, X_test, sc = normalizer.ts_train_test_normalize()

                log_file.write(f"X_train shape: {X_train.shape}\n")
                log_file.write(f"y_train shape: {y_train.shape}\n")
                log_file.write(f"X_test shape: {X_test.shape}\n")
                log_file.write(f"NaN in X_train: {np.isnan(X_train).sum()}\n")
                log_file.write(f"NaN in y_train: {np.isnan(y_train).sum()}\n")
                log_file.write(f"NaN in X_test: {np.isnan(X_test).sum()}\n")
                log_file.write(f"sc min_: {sc.min_}\n")
                log_file.write(f"sc scale_: {sc.scale_}\n")

                # 모델 학습 및 예측
                prediction = gru.train(X_train, y_train, X_test, sc)
                log_file.write(f"NaN in prediction: {np.isnan(prediction).sum()}\n")

                # 길이가 더 작은 쪽으로 맞춰줍니다.
                min_length = min(len(prediction), len(y) - 1)

                # 예측값만 저장
                prediction_df = pd.DataFrame({
                    'Adj Close': prediction[:min_length, 0]
                })

                log_file.write(f"NaN in prediction_df: {prediction_df.isna().sum().sum()}\n")

                # 예측 결과를 CSV 형식으로 저장
                prediction_df.to_csv(os.path.join("data/pred", f"pred_{symbol}.csv"), index=False)
            else:
                print(f"{symbol}에 해당하는 csv 파일을 찾을 수 없습니다.")
                log_file.write(f"{symbol}에 해당하는 csv 파일을 찾을 수 없습니다.\n")

        log_file.close()
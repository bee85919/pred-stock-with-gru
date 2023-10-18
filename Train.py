import os
import pandas as pd
from Normalize import Normalize
from GRUTrainer import GRUTrainer

class Train:

    def __init__(self, symbols_divided):
        self.symbols_divided = symbols_divided

    def train_and_save_model(self):
        os.makedirs("model", exist_ok=True)
        os.makedirs("predict", exist_ok=True)

        # GRU 모델 초기화
        gru = GRUTrainer()

        # symbol 별로 전처리, 학습, 저장
        for i, symbol_group in enumerate(self.symbols_divided):
            for idx, symbol in enumerate(symbol_group):
                print(f"Group {i+1} of {len(self.symbols_divided)}: Symbol {idx + 1} of {len(symbol_group)} ({symbol}) processing...")


                # 심볼별 csv 파일을 불러옵니다.
                X_file_path = os.path.join("data_train", f"train_{symbol}.csv")
                y_file_path = os.path.join("data_test", f"test_{symbol}.csv")

                if os.path.exists(X_file_path) and os.path.exists(y_file_path):
                    X = pd.read_csv(X_file_path)
                    y = pd.read_csv(y_file_path)

                    # 데이터 전처리
                    normalizer = Normalize(X, y, time_steps=5, for_periods=2)
                    X_train, y_train, X_test, sc = normalizer.ts_train_test_normalize()

                    # 모델 학습 및 예측
                    pred = gru.train(X_train, y_train, X_test, sc)

                    # 모델을 keras 형식으로 저장
                    gru.get_model().save(os.path.join("model", f"model_{symbol}.keras"))

                    # 예측 결과를 CSV 형식으로 저장
                    pd.DataFrame(pred).to_csv(os.path.join("predict", f"pred_{symbol}.csv"), index=False)
                else:
                    print(f"{symbol}에 해당하는 csv 파일을 찾을 수 없습니다.")

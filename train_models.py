import os
from dotenv import load_dotenv
from modules.Train.Train import Train
from modules.Train.Pooler import Pooler


def pool_train(symbols):
    # 병렬로 여러 모델 훈련
    Pooler(symbols, p_num=4).execute()

if __name__ == "__main__":
    load_dotenv()
    Train.make_dir()
    pool_train(symbols)

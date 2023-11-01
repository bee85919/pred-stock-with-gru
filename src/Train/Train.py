import os
import pandas as pd
from .Normalizer import Normalizer
from .GRUTrainer import GRUTrainer
from .Logger import Logger
from Utils.envLoader import envLoader

get_path = envLoader().get_path


class Train:
    
    @staticmethod
    def make_dir():
        os.makedirs(get_path('logs_path'), exist_ok=True)
        os.makedirs(get_path('pred_path'), exist_ok=True)
        

    @staticmethod
    def read_Xy(symbol):
        X_path = os.path.join(get_path('train_path'), f"train_{symbol}.csv")
        y_path = os.path.join(get_path('test_path'), f"test_{symbol}.csv")
        cond = os.path.exists(X_path) and os.path.exists(y_path)
        if cond: return pd.read_csv(X_path), pd.read_csv(y_path)
        else: return None, None


    @staticmethod
    def create_and_save_df(pred, y, symbol):
        pred_df = pd.DataFrame({'Adj Close': pred[:min(len(pred), len(y)-1), 0]})
        pred_df.to_csv(os.path.join(get_path('pred_path'), f"pred_{symbol}.csv"), index=False)
        return pred_df


    @staticmethod
    def train_and_save(symbol, idx=0, len_symbols=0):
        try:
            log = f"{get_path('logs_path')}/log_{symbol}.txt"
            gru = GRUTrainer(idx=idx, len_symbols=len_symbols)
            gru.initialize_model()
            
            X, y = Train.read_Xy(symbol)
            if X is not None and y is not None:
                X_train, y_train, X_test, sc = Normalizer(X, y, time_steps=5, for_periods=2).normalize()
                pred    = gru.train(X_train, y_train, X_test, sc, symbol)
                pred_df = Train.create_and_save_df(pred, y, symbol)
                Logger.log(log, symbol, X_train, X_test, y_train, sc, pred_df)
                
            else:
                Logger.err(log, symbol)
        except Exception as e:
            print(f"An error occurred: {e}")

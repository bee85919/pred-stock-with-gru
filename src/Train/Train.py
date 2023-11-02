import os
import pandas as pd
from .Normalizer import Normalizer
from .GRUModeling import GRUModeling
from Utils.envLoader import envLoader
from Utils.Logger import Logger


pth = envLoader().path.get
log = Logger.log
err = Logger.err


class Train:        
    
    def __init__(self, sym, i, size):
        logf = f"{pth('logs')}/l{sym}.txt"  
        X, y = self.read(sym)
        if not X or not y: 
            err(logf, sym)
            return
        X_train, y_train, X_test, sc = Normalizer(X, y, 5, 2)
        pred = GRUModeling(X_train, y_train, X_test, sc, sym, i, size)
        self.save(sym, pred, logf, sym, X_train, X_test, y_train, sc, pred, y)


    def read(sym):
        X_path = os.path.join(pth('train'), f"train_{sym}.csv")
        y_path = os.path.join(pth('test'), f"test_{sym}.csv")
        if os.path.exists(X_path) and os.path.exists(y_path): 
            return pd.read_csv(X_path), pd.read_csv(y_path)
        else: return None, None
    
    
    def adjust(self, pred, y):
        return pd.DataFrame({'Adj Close': pred[:min(len(pred), len(y)-1), 0]})
        
        
    def save(self, logf, sym, X_train, X_test, y_train, sc, pred, y):        
        pred = self.adjust(pred, y)
        pred.to_csv(os.path.join(pth('pred'), f"pred_{sym}.csv"), index=False)
        log(logf, sym, X_train, X_test, y_train, sc, pred)
import pandas as pd
import os
from .envLoader import envLoader
from .createDir import createDir


pth = envLoader().path().get
dir = createDir


dir(pth('pred'))
dir(pth('result'))


class Save:
    def __init__(self, date):
        bdays, preds = self.business_days(date), []
        for f in os.listdir(pth('pred')):
            if not f.endswith('.csv'): 
                return
            pred = self.process(bdays, pred, f)
            preds.append(pred)
        result = pd.concat(preds)
        self.save(result)
        

    def business_days(self, date):
        print("Merging preds...")
        p = len(pd.read_csv(f"{pth('pred')}/pred_AMZN.csv"))
        bdays = pd.bdate_range(start=date, periods=p, freq='B')
        return bdays
    
    
    def get_sym(self, f):
        return f.replace('pred_', '').replace('.csv', '')
    
    
    def load_pred(self, f):        
        print(f"Loading {f}...")
        pred = pd.read_csv(f"{pth('pred')}/{f}")
        pred.dropna(subset=['Adj Close'], inplace=True)
        return pred
    
    
    def process(self, bdays, pred, f):
        sym = self.get_sym(f)
        pred = self.load_pred(f)
        pred = self.bday_indexing(pred, bdays)
        pred = self.symbol_column(pred, sym)
        pred = self.rename_column(pred)
        pred = self.order_columns(pred)
        return pred        
    
    
    def bday_indexing(self, pred, bdays):
        pred.index = bdays[:len(pred)]
        pred.index.name = 'date'
        return pred
    
    
    def symbol_column(self, pred, sym):
        pred['symbol'] = sym
        return pred
    
    
    def rename_column(self, pred):
        pred = pred.rename(columns={'Adj Close': 'close'})
        return pred
    
    
    def order_columns(self, pred):
        return pred[['symbol', 'close']]
    
    
    def save(self, result):
        result.sort_values(by=['symbol', 'date'], inplace=True)
        result.to_csv(f"{pth('result')}/result.csv")
        print("Merged preds!")
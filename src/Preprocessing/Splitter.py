import os
import pandas as pd
from Utils.envLoader import envLoader
from Utils.createDir import createDir

                
pth = envLoader().get_path.get
dir = createDir


class Splitter:
    
    def __init__(self, test_size=23):        
        dir(pth('train'))
        dir(pth('test'))
        self.split_data(test_size)
            
            
    def split_data(self, test_size):
        csvs, size = self.get_csvs()
        for i, csv in enumerate(csvs, 1):
            sym, path = self.get_csv(i, csv, size)
            train_csv, test_csv = self.split_csv(sym, path, test_size)
            train_csv_path, test_csv_path = self.save_path(sym)
            self.save(sym, train_csv, test_csv, train_csv_path, test_csv_path)
            
            
    def get_csvs(self):
        csvs = [csv for csv in os.listdir(pth('prep')) if csv.endswith('.csv')]
        size = len(csvs)
        print(f"Total size: {size}")
        return csvs, size
    
    
    def get_csv(self, i, csv, size):
        print(f"Processing {i}/{size}")
        sym = csv.replace('.csv', '')
        path = os.path.join(pth('prep'), csv)
        return sym, path
        
        
    def split_csv(self, path, test_size):
        csv = pd.read_csv(path)
        train_size = len(csv) - test_size
        train_set = csv.iloc[:train_size]
        test_set = csv.iloc[train_size:]
        return train_set, test_set
    
    
    def save_path(sym):
        train_csv_path = os.path.join(pth('train'), f"train_{sym}.csv")
        test_csv_path = os.path.join(pth('test'), f"test_{sym}.csv")
        return train_csv_path, test_csv_path
    
    
    def save(sym, train_csv, test_csv, train_csv_path, test_csv_path):   
        train_csv.to_csv(train_csv_path, index=False)     
        print(f"Saved {sym} train data to {train_csv_path}")
        test_csv.to_csv(test_csv_path, index=False)
        print(f"Saved {sym} test data to {test_csv_path}")        
        
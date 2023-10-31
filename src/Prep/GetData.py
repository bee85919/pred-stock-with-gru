import os
import pandas as pd
from Utils.envLoader import envLoader


class GetData:    
    def __init__(self, data, symbols):
        self.get_env = envLoader.get_env
        self.prep_path = self.get_env('prep_path')        
        self.data = data        
        self.symbols = symbols        
        self.make_dirs()                
        print("Generating datasets for symbols...")        
        self.get_data_prepared(self.symbols)
        print("Data extraction completed.")
        

    def make_dirs(self):     
        if not os.path.exists(self.prep_path):       
            os.makedirs(self.prep_path)


    def get_data_prepared(self, symbols):        
        total_symbols = len(symbols)        
        for index, symbol in enumerate(symbols):
            amzn = self.data[self.data['symbol'] == 'AMZN']
            temp = self.data[self.data['symbol'] == symbol]            
            if len(temp) == len(amzn):
                temp = temp.set_index('Date').drop(columns=['symbol'])                                
                temp_path = os.path.join(self.prep_path, f"{symbol}.csv")                
                temp.to_csv(temp_path)                
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Saved!")                
            else:
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Skipped due to row count!")
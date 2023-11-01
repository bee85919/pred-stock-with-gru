import os
import pandas as pd
from Utils.envLoader import envLoader


class GetData:    
    def __init__(self, data, symbols):
        get_path = envLoader().get_path
        self.prep_path = get_path('prep_path')        
        self.data = data        
        self.symbols = [s for symbol in symbols for s in symbol]
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
            print(index, symbol)
            amzn = self.data[self.data['symbol'] == 'AMZN']
            temp = self.data[self.data['symbol'] == symbol]
            if len(temp) == len(amzn):
                temp = temp.set_index('date').drop(columns=['symbol'])                                
                temp_path = os.path.join(self.prep_path, f"{symbol}.csv")                
                temp.to_csv(temp_path)                
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Saved!")                
            else:
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Skipped due to row count!")
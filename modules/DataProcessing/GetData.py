import os
import pandas as pd
from dotenv import load_dotenv


class GetData:
    
    def __init__(self, data, symbols):        
        load_dotenv()        
        self.prep_path = os.getenv('prep_path')        
        self.data = data        
        self.symbols = symbols        
        self.make_dirs()                
        print("Generating datasets for symbols...")        
        self.get_data_prepared(self.symbols)        
        print("Data extraction completed.")
        

    def make_dirs(self):        
        print("Checking or creating directory for datasets...")        
        if not os.path.exists(self.prep_path):            
            print(f"Creating {self.prep_path} directory...")            
            os.makedirs(self.prep_path)            
        else:
            print(f"{self.prep_path} directory already exists.")


    def get_data_prepared(self, symbols):        
        total_symbols = len(symbols)        
        for index, symbol in enumerate(symbols):            
            temp = self.data[self.data['symbol'] == symbol]            
            if len(temp) == 206:
                temp = temp.set_index('Date').drop(columns=['symbol'])                                
                temp_path = os.path.join(self.prep_path, f"{symbol}.csv")                
                temp.to_csv(temp_path)                
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Saved!")                
            else:
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Skipped due to row count!")
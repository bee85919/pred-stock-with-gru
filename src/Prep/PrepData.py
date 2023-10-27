import pandas as pd
import os
from dotenv import load_dotenv
from .GetSymbol import GetSymbol


class PrepData:
    
    def __init__(self, csv_path, year, month, day, period=70):
                
        load_dotenv()        
        self.data_path = os.getenv('data_path')    
        
        print("DataLoader is initializing...")
        self.make_dirs()
        
        self.data = self.load_and_preprocess_data(csv_path, year, month, day, period)
        self.get_symbol()
            
        print("DataLoader is initialized!")


    def read_data(self, csv_path):        
        data_amex = pd.read_csv(csv_path[0])        
        data_nsdq = pd.read_csv(csv_path[1])        
        data_nyse = pd.read_csv(csv_path[2])            
        return data_amex, data_nsdq, data_nyse


    def make_dirs(self):        
        if not os.path.exists(self.data_path):            
            os.makedirs(self.data_path)


    def preprocess_data(self, data_amex, data_nsdq, data_nyse):        
        data = pd.concat([data_amex, data_nsdq, data_nyse])        
        data = data.drop(columns=['Unnamed: 0'])        
        data['Date'] = pd.to_datetime(data['Date'])        
        data = data.set_index('Date').sort_values(by=['Date', 'symbol'])        
        data = data[['symbol', 'Adj Close', 'Open', 'High', 'Low', 'Close', 'Volume']]
        return data
    

    def get_data_from_date(self, data, year, month, day, period):        
        date_target = pd.Timestamp(year=year, month=month, day=day)        
        date_start = date_target - pd.Timedelta(days=(period-1))        
        return data[(data.index >= date_start) & (data.index <= date_target)]
    

    def save_data(self, data):        
        data.to_csv(self.data_path)


    def load_data(self):
        return pd.read_csv(self.data_path, index_col='Date', parse_dates=True)
    
    
    def load_and_preprocess_data(self, csv_path, year, month, day, period):        
        print('loading csv files...')
        data_amex, data_nsdq, data_nyse = self.read_data(csv_path)    
        print('processing csv files...')
        data = self.preprocess_data(data_amex, data_nsdq, data_nyse)
        print('filtering data...')        
        data_filtered = self.get_data_from_date(data, year, month, day, period)    
        print('saving data...')    
        self.save_data(data_filtered)        
        return self.load_data()
        
        
    def get_symbol(self):
        
        symbols        = os.getenv('symbols_path')
        symbols_length = os.getenv('symbols_length_path')
        
        symbols_exists        = os.path.exists(symbols)
        symbols_length_exists = os.path.exists(symbols_length)     
        
        if not (symbols_exists and symbols_length_exists):
            
            print("Getting symbols...")
            GetSymbol(self.data).get_symbols()
            
        else:
            
            print("Symbols already exists!")
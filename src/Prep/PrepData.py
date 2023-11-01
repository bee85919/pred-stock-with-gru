import pandas as pd
import os
from .GetSymbol import GetSymbol
from Utils.envLoader import envLoader


class PrepData:    
    def __init__(self, csv_path, year, month, day, period=300):
        get_path = envLoader().get_path
        self.data_path = get_path('data_path')
        self.symbols = get_path('symbols_path')
        self.symbols_length = get_path('symbols_length_path')

        print("DataLoader is initializing...")
        self.make_dirs()
        self.data = self.preprocess_data(csv_path, year, month, day, period)
        print("DataLoader is initialized!")
        
    
    def make_dirs(self):
        dir_path = os.path.dirname(self.data_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
    
    def preprocess_data(self, csv_path, year, month, day, period):
        print('Loading csv files...')
        data_list = self.read_data(csv_path)
        
        print('Processing csv files...')
        data = self.concat_data(data_list)
        
        print('Filtering data...')
        data_filtered = self.filter_data(data, year, month, day, period)
        
        print('Getting symbols...')
        self.get_symbols(data_filtered)
        
        print('Saving data...')
        self.save_data(data_filtered)


    def read_data(self, csv_path):
        rename_column = {'company_code': 'symbol'}
        return [pd.read_csv(path).rename(columns=rename_column) for path in csv_path]


    def concat_data(self, data_list):
        data = pd.concat(data_list)
        data['date'] = pd.to_datetime(data['date'])
        data = data.set_index('date').sort_values(by=['symbol', 'date'])
        return data[['symbol', 'close', 'open', 'high', 'low', 'volume']]


    def filter_data(self, data, year, month, day, period):
        date_target = pd.Timestamp(year=year, month=month, day=day)
        date_start = date_target - pd.Timedelta(days=(period-1))
        return data[(data.index >= date_start) & (data.index <= date_target)]


    def get_symbols(self, data):
        if not (os.path.exists(self.symbols) and os.path.exists(self.symbols_length)):
            print("Getting symbols...")
            GetSymbol(data).get_symbols()
        else:
            print("Symbols already exist!")


    def save_data(self, data):
        data.to_csv(self.data_path)

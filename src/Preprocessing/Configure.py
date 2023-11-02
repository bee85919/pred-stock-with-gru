import pandas as pd
import os
from .GetSymbol import GetSymbol
from Utils.envLoader import envLoader
from Utils.createDir import createDir


pth = envLoader().get_path().get
dir = createDir


class Configure:    
    
    def __init__(self, csvs_list, y, m, d, p=300):
        print("Configuring csvs...")
        dir(pth('data'))
        csvs = self.read_data(csvs_list)
        data = self.concat_data(csvs)
        data = self.filter_data(data, y, m, d, p)
        self.get_syms(data)
        self.save_data(data)
        print("Configuration completed.")


    def read_data(self):
        print('Loading csv files...')
        rename_column = {'company_code': 'symbol'}
        return [pd.read_csv(csv).rename(columns=rename_column) for csv in pth('csvs')]


    def concat_data(self, csvs):
        print('Processing csv files...')
        data = pd.concat(csvs).assign(date=lambda data: pd.to_datetime(data['date']))
        data = data.set_index('date').sort_values(by=['symbol', 'date'])
        return data[['symbol', 'close', 'open', 'high', 'low', 'volume']]


    def filter_data(self, data, y, m, d, p):
        print('Filtering data...')
        date = data.index
        end = pd.Timestamp(y=y, m=m, d=d)
        start = end - pd.Timedelta(days=(p-1))
        return data[(start <= date <= end)]


    def get_syms(self, data):
        print("Getting symbols...")
        if not os.path.exists(pth('syms')): 
            GetSymbol(data)
        else: print("Symbols already exist!")


    def save_data(self, data):
        print('Saving data...')
        data.to_csv(pth('data'))
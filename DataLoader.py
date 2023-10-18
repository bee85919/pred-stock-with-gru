import pandas as pd
import os

class DataLoader:
    def __init__(self, csv_paths, year, month, period):
        print("DataLoader is initializing...")
        data_amex, data_nsdq, data_nyse = self.read_data(csv_paths)
        self.make_dirs()
        data = self.preprocess_data(data_amex, data_nsdq, data_nyse)
        filtered_data = self.get_data_from_date(data, year, month, period)
        self.save_data(filtered_data)
        print("DataLoader is initialized!")
        self.data = self.load_data()


    def read_data(self, csv_paths):
        csv_reads = [pd.read_csv(path) for path in csv_paths]
        return csv_reads


    def make_dirs(self):
        if not os.path.exists('./data_concated'):
            os.makedirs('./data_concated')


    def preprocess_data(self, data_amex, data_nsdq, data_nyse):
        data = pd.concat([data_amex, data_nsdq, data_nyse])
        data = data.drop(columns=['Unnamed: 0'])
        data['Date'] = pd.to_datetime(data['Date'])
        data = data.set_index('Date').sort_values(by=['Date', 'symbol'])
        data = data[['symbol', 'Adj Close', 'Open', 'High', 'Low', 'Close', 'Volume']]
        return data
    

    def get_data_from_date(self, data, year, month, period):
        date_start = pd.Timestamp(year=year, month=month, day=1)
        date_end = pd.Timestamp(year=year + (month + period - 1) // 12, 
                                month=(month + period - 1) % 12 + 1, 
                                day=1) - pd.Timedelta(days=1)  
        return data[(data.index >= date_start) & (data.index <= date_end)]


    def save_data(self, data):
        data.to_csv('./data_concated/data.csv')


    def load_data(self):
        return pd.read_csv('./data_concated/data.csv', index_col='Date', parse_dates=True)

import pandas as pd
import os

class DataLoader:
    def __init__(self, csv_paths, period, year, month):
        print("DataLoader is initializing...")
        data_amex, data_nsdq, data_nyse = self._read_data(csv_paths)
        self._make_dirs()
        data = self._preprocess_data(data_amex, data_nsdq, data_nyse)
        filtered_data = self._get_data_from_date(data, period, year, month)
        self._save_data(filtered_data)
        print("DataLoader is initialized!")
        self.data = self._load_data()


    def _read_data(self, csv_paths):
        csv_reads = [pd.read_csv(path) for path in csv_paths]
        return csv_reads


    def _make_dirs(self):
        if not os.path.exists('./dataset_concated'):
            os.makedirs('./dataset_concated')


    def _preprocess_data(self, data_amex, data_nsdq, data_nyse):
        data = pd.concat([data_amex, data_nsdq, data_nyse])
        data = data.drop(columns=['Unnamed: 0'])
        data['Date'] = pd.to_datetime(data['Date'])
        data = data.set_index('Date').sort_values(by=['Date', 'symbol'])
        data = data[['symbol', 'Adj Close', 'Open', 'High', 'Low', 'Close', 'Volume']]
        return data


    def _get_data_from_date(self, data, period, year, month):
        date_start = pd.Timestamp(year=year, month=month, day=1)
        date_end = date_start + pd.DateOffset(months=period)
        return data[(data.index >= date_start) & (data.index <= date_end)]


    def _save_data(self, data):
        data.to_csv('./dataset_concated/data.csv')


    def _load_data(self):
        return pd.read_csv('./dataset_concated/data.csv', index_col='Date', parse_dates=True)

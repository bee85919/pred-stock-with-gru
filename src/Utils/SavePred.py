import pandas as pd
import os
from .envLoader import envLoader


class SavePred:
    def __init__(self, date, pred_path=None, result_path=None):
        get_path = envLoader().get_path
        self.date = date
        self.pred_path = get_path('pred_path')
        self.result_path = get_path('result_path')        
        self.make_dir(self.pred_path)
        self.make_dir(self.result_path)
        
    
    def make_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        

    def generate_business_days(self):
        length = len(pd.read_csv(f'{self.pred_path}/pred_AMZN.csv'))
        business_days = pd.bdate_range(start=self.date, periods=length, freq='B')
        self.end_date = business_days[-1]
        return business_days
    

    def merge_csv_files(self):
        business_days = self.generate_business_days()
        all_dfs = []
        print("Merging CSV files...")
        for file in os.listdir(self.pred_path):
            if file.endswith('.csv'):
                symbol = file.replace('pred_', '').replace('.csv', '')
                print(f"Merging {file}...")
                df = pd.read_csv(f'{self.pred_path}/{file}')
                df.dropna(subset=['Adj Close'], inplace=True)
                df = df[df['Adj Close'] != 0]
                df.index = business_days[:len(df)]
                df.index.name = 'Date'
                df['Symbol'] = symbol
                df = df[['Symbol', 'Adj Close']]
                all_dfs.append(df)
        result_df = pd.concat(all_dfs)
        result_df.sort_values(by=['Symbol', 'Date'], inplace=True)
        result_df.to_csv(f'{self.result_path}/result.csv')
        print("Merged CSV files successfully.")
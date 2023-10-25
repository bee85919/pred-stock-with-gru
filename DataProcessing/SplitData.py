import os
import pandas as pd
from dotenv import load_dotenv

class SplitData:
    def __init__(self, data, symbol, len_test=23):
        load_dotenv()
        self.train_path = os.getenv('train_path')
        self.test_path = os.getenv('test_path')
        
        self.data = data
        self.symbol = symbol
        self.len_test = len_test
        

    def splitter(self):
        total_rows = len(self.data)
        train_size = total_rows - self.len_test
        train_set = self.data.iloc[:train_size]
        test_set = self.data.iloc[train_size:]

        os.makedirs(self.train_path, exist_ok=True)
        os.makedirs(self.test_path, exist_ok=True)

        train_file_path = os.path.join(self.train_path, f"train_{self.symbol}.csv")
        test_file_path = os.path.join(self.test_path, f"test_{self.symbol}.csv")

        train_set.to_csv(train_file_path, index=False)
        test_set.to_csv(test_file_path, index=False)
        print(f"Saved {self.symbol} train data to {train_file_path}")
        print(f"Saved {self.symbol} test data to {test_file_path}")


    @staticmethod
    def split_data(folder_path, len_test=23):
        total_files = len([name for name in os.listdir(folder_path) if name.endswith('.csv')])
        print(f"Total groups to process: {total_files}")
        for idx, file_name in enumerate(os.listdir(folder_path), 1):  # idx starts from 1
            if file_name.endswith('.csv'):
                print(f"Processing group {idx} of {total_files}")                
                file_path = os.path.join(folder_path, file_name)
                symbol_name = file_name.replace('.csv', '')
                
                print(f"Processing file {symbol_name} in group {idx}")
                file_data = pd.read_csv(file_path)
                split_data = SplitData(file_data, symbol_name, len_test=len_test)                
                split_data.splitter()
import os
import pandas as pd


class GetData:
    def __init__(self, data, symbols):
        self.data = data
        self.symbols = symbols

        self.make_dirs()        
        print("Generating datasets for symbols...")
        self.get_data_prepared(self.symbols)
        print("Data extraction completed.")

    def make_dirs(self):
        print("Checking or creating directory for datasets...")
        if not os.path.exists("./data/prepared"):
            print("Creating 'data/prepared' directory...")
            os.makedirs("./data/prepared")
        else:
            print("'./data/prepared' directory already exists.")

    def get_data_prepared(self, symbols):
        total_symbols = len(symbols)
        for index, symbol in enumerate(symbols):
            temp = self.data[self.data['symbol'] == symbol]
            if len(temp) == 206:
                # Date를 인덱스로 설정하고 'symbol' 열을 제거
                temp = temp.set_index('Date').drop(columns=['symbol'])                
                temp_path = os.path.join("./data/prepared", f"{symbol}.csv")
                temp.to_csv(temp_path)
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Saved!")
            else:
                print(f"Symbol {index+1}/{total_symbols}: {symbol} ... Skipped due to row count!")
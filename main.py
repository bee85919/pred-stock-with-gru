import pandas as pd

from DataLoader import DataLoader
from DataExtractor import DataExtractor

def main():        
    csv_paths = ['./dataset/amex_data.csv',
                 './dataset/nasdaq_data.csv',
                 './dataset/nyse_data.csv']

    # data = DataLoader(csv_paths, period=12, year=2022, month=9).data
    data = pd.read_csv('./dataset_concated/data.csv', index_col='Date', parse_dates=True)
    extractor = DataExtractor(data, n=10)
    symbols_divided = extractor.symbols_divided

if __name__ == "__main__":
    main()
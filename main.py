import pandas as pd
from DataLoader import DataLoader
from DivideData import DivideData
from GetData import GetData
from Train import Train
from SplitData import SplitData

def main():        
    csv_paths = ['./dataset/amex_data.csv',
                 './dataset/nasdaq_data.csv',
                 './dataset/nyse_data.csv']

    DataLoader(csv_paths, year=2023, month=9, day=31, period=70)
    data = pd.read_csv('./data/concated/data.csv')
    symbols = DivideData(data, n=10).get_divided_symbols()
    
    GetData(data, symbols)
    SplitData.split_data('./data_prepared')
    Train(symbols).train_and_save_model()

if __name__ == "__main__":
    main()
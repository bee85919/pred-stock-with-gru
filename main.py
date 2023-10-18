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

    DataLoader(csv_paths, year=2022, month=9, period=12)
    data = pd.read_csv('./data_concated/data.csv')
    symbols_divided = DivideData(data, n=10).get_divided_symbols()
    
    GetData(data, symbols_divided)
    SplitData.split_data('./data_prepared')
    
    trainer = Train(symbols_divided)
    trainer.train_and_save_models()

if __name__ == "__main__":
    main()
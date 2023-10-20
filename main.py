import pandas as pd
from DataLoader import DataLoader
from GetSymbol import GetSymbol
from GetData import GetData
from Train import Train
from SplitData import SplitData

def main():        
    csv_paths = ['./dataset/amex_data.csv',
                 './dataset/nasdaq_data.csv',
                 './dataset/nyse_data.csv']
    y, m, d, p = 2023, 9, 30, 300
    # DataLoader(csv_paths, year=y, month=m, day=d, period=p)
    
    data = pd.read_csv('./data/dataset/dataset.csv')
    symbols = GetSymbol(data).get_symbols()    
    # GetData(data, symbols)
    
    SplitData.split_data('./data/prepared')
    Train(symbols).train_and_save_models()
    

if __name__ == "__main__":
    main()
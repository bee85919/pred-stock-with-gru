import pandas as pd
from DataLoader import DataLoader
from GetSymbol import GetSymbol
from GetData import GetData
from SplitData import SplitData
from Train import Train
from SavePreds import SavePreds


def main():        
    csv_paths = ['./dataset/amex_data.csv',
                 './dataset/nasdaq_data.csv',
                 './dataset/nyse_data.csv']
    y, m, d, p = 2023, 9, 30, 300
    
    DataLoader(csv_paths, year=y, month=m, day=d, period=p)
     
    data = pd.read_csv('./data/dataset/dataset.csv')
    
    symbols = GetSymbol(data).get_symbols()
    
    GetData(data, symbols)    
    
    SplitData.split_data('./data/prepd')
    
    Train(symbols).train_and_save_models()
    
    SavePreds(start_date=f'{y}-{m}-{d}').merge_csv_files()
    
    
if __name__ == "__main__":
    main()
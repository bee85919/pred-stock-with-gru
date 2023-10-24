import pandas as pd
from multiprocessing import Pool
from DataLoader import DataLoader
from GetSymbol import GetSymbol
from GetData import GetData
from SplitData import SplitData
from Train import Train
from Pooler import Pooler
from SavePred import SavePred


def main():        
    csv_paths = ['./dataset/amex_data.csv',
                 './dataset/nasdaq_data.csv',
                 './dataset/nyse_data.csv']
    y, m, d, p = 2023, 9, 30, 300
    
    # DataLoader(csv_paths, year=y, month=m, day=d, period=p)
     
    data = pd.read_csv('./data/dataset/dataset.csv')
    
    symbols = GetSymbol(data).get_symbols()
    
    # GetData(data, symbols)
    
    # SplitData.split_data('./data/prep')
    
    Train.make_dir()
    
    # Train.train_and_save('AMZN')
    
    Pooler(symbols, p_num=4).execute()
    
    SavePred(start_date=f'{y}-{m}-{d}').merge_csv_files()
    
    
if __name__ == "__main__":
    main()
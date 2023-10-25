import os
import pandas as pd
from dotenv import load_dotenv
from multiprocessing import Pool
from DataProcessing.DataLoader import DataLoader
from DataProcessing.GetSymbol import GetSymbol
from DataProcessing.GetData import GetData
from DataProcessing.SplitData import SplitData
from Train.Train import Train
from Train.Pooler import Pooler
from Save.SavePred import SavePred


def main():
    
    load_dotenv()
    
    data_path = os.getenv('data_path')    
    prep_path = os.getenv('prep_path')
               
    csv_paths = ['./dataset/amex_data.csv',
                 './dataset/nasdaq_data.csv',
                 './dataset/nyse_data.csv']
    y, m, d, p = 2023, 9, 30, 300
    
    # DataLoader(csv_paths, year=y, month=m, day=d, period=p)
     
    data = pd.read_csv(os.path.join(data_path, 'data.csv'))
    
    symbols = GetSymbol(data).get_symbols()
    
    print(symbols)
    
    print(len(symbols))
    
    # GetData(data, symbols)
    
    # SplitData.split_data(prep_path)
    
    # Train.make_dir()
    
    # Train.train_and_save('AMZN')
    
    # Pooler(symbols, p_num=4).execute()
    
    # SavePred(date=f'{y}-{m}-{d}').merge_csv_files()
    
    
if __name__ == "__main__":
    main()
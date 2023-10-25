import os
import pandas as pd
from dotenv import load_dotenv
from multiprocessing import Pool
from modules.DataProcessing.DataLoader import DataLoader
from modules.DataProcessing.GetSymbol import GetSymbol
from modules.DataProcessing.GetData import GetData
from modules.DataProcessing.SplitData import SplitData
from modules.Train.Train import Train
from modules.Train.Pooler import Pooler
from modules.Save.SavePred import SavePred


def main():
    
    load_dotenv()
    
    data_path = os.getenv('data_path')    
    prep_path = os.getenv('prep_path')
               
    csv_paths = ['./input/amex_data.csv',
                 './input/nasdaq_data.csv',
                 './input/nyse_data.csv']
    y, m, d, p = 2023, 9, 30, 300
    
    # DataLoader(csv_paths, year=y, month=m, day=d, period=p)
     
    data = pd.read_csv(os.path.join(data_path, 'data.csv'))
    
    symbols = GetSymbol(data).get_symbols()
    
    print(symbols)
    
    print(len(symbols))
    
    # GetData(data, symbols)
    
    # SplitData.split_data(prep_path)
    
    # modules.Train.make_dir()
    
    # modules.Train.train_and_save('AMZN')
    
    # Pooler(symbols, p_num=4).execute()
    
    # SavePred(date=f'{y}-{m}-{d}').merge_csv_files()
    
    
if __name__ == "__main__":
    main()
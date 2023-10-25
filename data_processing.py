import os
from dotenv import load_dotenv
from modules.DataProcessing.DataLoader import DataLoader
from modules.DataProcessing.GetSymbol import GetSymbol
from modules.DataProcessing.GetData import GetData
from modules.DataProcessing.SplitData import SplitData
import pandas as pd


def process_data():
    load_dotenv()
    data_path = os.getenv('data_path')
    prep_path = os.getenv('prep_path')    
    input_path = ['./input/amex_data.csv',
                 './input/nasdaq_data.csv',
                 './input/nyse_data.csv']
    
    y, m, d, p = 2023, 9, 30, 300
    
    DataLoader(input_path, year=y, month=m, day=d, period=p)
    
    data = pd.read_csv(os.path.join(data_path, 'data.csv'))
    
    symbols = GetSymbol(data).get_symbols()
    
    GetData(data, symbols)
    
    SplitData.split_data(prep_path)


if __name__ == "__main__":
    process_data()
import os
import pandas as pd
from dotenv import load_dotenv
from modules.etc.TxtReader import TxtReader
from modules.Preparation.GetData import GetData
from modules.Preparation.SplitData import SplitData


load_dotenv()
prep_path = os.getenv('prep_path')
data_path = os.getenv('data_path')
symbols_path = os.getenv('symbols_path')


get = TxtReader().get_list
symbols = get(symbols_path)


def prepare_data():    
    data = pd.read_csv(data_path)  
    GetData(data, symbols)    
    SplitData.split_data(prep_path)


if __name__ == "__main__":
    prepare_data()
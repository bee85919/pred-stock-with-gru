import os
import pandas as pd
from dotenv import load_dotenv
from Util.txtReader import txtReader
from Prep.GetData import GetData
from Prep.SplitData import SplitData


load_dotenv()
prep_path = os.getenv('prep_path')
data_path = os.getenv('data_path')
symbols_path = os.getenv('symbols_path')


get = txtReader().get_list
symbols = get(symbols_path)


def prep_data():    
    data = pd.read_csv(data_path)  
    GetData(data, symbols)    
    SplitData.split_data(prep_path)


if __name__ == "__main__":
    prep_data()
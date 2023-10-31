import pandas as pd
from Prep.GetData import GetData
from Prep.SplitData import SplitData
from Utils.envLoader import envLoader
from Utils.txtReader import txtReader


get_path = envLoader().get_path
prep_path = get_path('prep_path')
data_path = get_path('data_path')
symbols_path = get_path('symbols_path')


get_list = txtReader().get_list
symbols = get_list(symbols_path)


def prep_data():    
    data = pd.read_csv(data_path)  
    GetData(data, symbols)    
    SplitData.split_data(prep_path)


if __name__ == "__main__":
    prep_data()
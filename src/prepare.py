import pandas as pd
from Preprocessing.GetData import GetData
from Preprocessing.Splitter import Splitter
from Utils.envLoader import envLoader
from Utils.txtReader import txtReader    


pth = envLoader().get_path.get
lst = txtReader().get_lst


if __name__ == "__main__":
    syms = lst(pth('syms'))        
    data = pd.read_csv(pth('data'))  
    GetData(data, syms)
    Splitter()
import os
from dotenv import load_dotenv
from Utils.envLoader import envLoader
from Utils.txtReader import txtReader
from Utils.Save import Save


pth = envLoader().path().get
lst = txtReader().get_list


if __name__ == "__main__":
    y, m, d, _ = lst(pth('date'))    
    Save(date=f'{y}-{m}-{d}')
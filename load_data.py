import os
from dotenv import load_dotenv
from modules.etc.TxtReader import TxtReader
from modules.Load.DataLoader import DataLoader


load_dotenv()
input_path = os.getenv('input_path')
date_path = os.getenv('date_path')


get = TxtReader().get_list
input_path = get(input_path)
y, m, d, p = get(date_path)


def load_data():
    DataLoader(input_path, year=y, month=m, day=d, period=p)
    
    
if __name__ == "__main__":
    load_data()
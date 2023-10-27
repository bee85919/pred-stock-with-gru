import os
from dotenv import load_dotenv
from src.Util.txtReader import txtReader
from src.Prep.PrepData import PrepData


load_dotenv()
csv_path = os.getenv('csv_path')
date_path = os.getenv('date_path')


get = txtReader().get_list
csv_path = get(csv_path)
y, m, d, p = get(date_path)


def conf_data():
    PrepData(csv_path, year=y, month=m, day=d, period=p)
    
    
if __name__ == "__main__":
    conf_data()
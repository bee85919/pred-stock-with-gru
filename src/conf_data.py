from Prep.PrepData import PrepData
from Utils.txtReader import txtReader
from Utils.envLoader import envLoader


get_path = envLoader().get_path
csv_path = get_path('csv_path')
date_path = get_path('date_path')


get_list = txtReader().get_list
csv_path = get_list(csv_path)
y, m, d, p = get_list(date_path)
print(csv_path)
print(y, m, d, p)


def conf_data():
    PrepData(csv_path, year=y, month=m, day=d, period=p)
    
    
if __name__ == "__main__":
    conf_data()
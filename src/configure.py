from Preprocessing.Configure import Configure
from Utils.envLoader import envLoader    
from Utils.txtReader import txtReader


pth = envLoader().get_path().get   
lst = txtReader().get_list
    
    
if __name__ == "__main__":
    Configure(lst(pth('csvs')), *lst(pth('date')))
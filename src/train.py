from Utils.envLoader import envLoader
from Utils.txtReader import txtReader
from Utils.createDir import createDir
from Train.Pooler import Pooler


pth = envLoader().get_path.get
lst = txtReader().get_list
upd = txtReader().update_list
dir = createDir


dir('logs')
dir('pred')


if __name__ == "__main__":
    syms_lst = lst(pth('syms'))
    syms = syms_lst.pop(0) 
    Pooler(syms, pnum=8)
    upd(syms_lst, pth('syms'))
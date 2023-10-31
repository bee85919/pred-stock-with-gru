from Utils.envLoader import envLoader
from Utils.txtReader import txtReader
from Train.Train import Train
from Train.Pooler import Pooler


get_path = envLoader().get_path
symbols_path = get_path('symbols_path')


get = txtReader().get_list
symbols_lst = get(symbols_path)
symbols = symbols_lst.pop(0)


def train(p_num=8):
    Pooler(symbols, p_num)
    

def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as f:
        f.write(repr(lst))


if __name__ == "__main__":
    Train.make_dir()
    train()
    write_list_to_file(symbols_lst, symbols_path)
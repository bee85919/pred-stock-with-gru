import os
from dotenv import load_dotenv
from Util.txtReader import txtReader
from Train.Train import Train
from Train.Pooler import Pooler


load_dotenv()
symbols_path = os.getenv('symbols_path')

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
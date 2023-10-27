import os
from dotenv import load_dotenv
from modules.etc.TxtReader import TxtReader
from modules.Train.Train import Train
from modules.Train.Pooler import Pooler


load_dotenv()
symbols_path = os.getenv('symbols_path')

get = TxtReader().get_list
symbols_lst = get(symbols_path)
symbols = symbols_lst.pop(0)


def pool_train(p_num=8):
    Pooler(symbols, p_num)
    

def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")


if __name__ == "__main__":
    Train.make_dir()
    pool_train()
    write_list_to_file(symbols_lst, symbols_path)
from multiprocessing import Pool
from modules.Train.Train import Train


class Pooler:
    def __init__(self, symbols, p_num=4):
        self.p_num = p_num
        self.symbols = symbols
        self.len_symbols = len(symbols)


    def process_and_count(self, args):
        idx, symbol = args
        modules.Train.train_and_save(symbol, idx=idx, len_symbols=self.len_symbols)


    def execute(self):
        with Pool(processes=self.p_num) as p:
            p.map(self.process_and_count, enumerate(self.symbols))
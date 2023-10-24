from multiprocessing import Pool
from Train import Train

class Pooler:
    def __init__(self, symbols, p_num=8):
        self.p_num = p_num
        self.symbols = symbols
        self.total = len(symbols)


    def process_and_count(self, symbol, index):
        Train([symbol]).train_and_save()
        print(f"Processed symbol: {symbol} ({index + 1}/{self.total})")


    def execute(self):
        with Pool(processes=self.p_num) as p:
            for i, symbol in enumerate(self.symbols):
                p.apply_async(self.process_and_count, args=(symbol, i))
            p.close()
            p.join()
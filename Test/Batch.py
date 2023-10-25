import gc
from Train.Train import Train


class Batch:
    def __init__(self, data, symbols, batch_size):
        self.data = data
        self.symbols = symbols
        self.batch_size = batch_size
        self.batch_cnt = len(symbols)//batch_size


    def process_batch(self, data, batch_symbols):
        train = Train(data, batch_symbols, self.batch_size)
        train.train_and_save()


    def process_batches(self):
        for i in range(self.batch_cnt + 1):
            batch_symbols = self.symbols[i * self.batch_size: (i + 1) * self.batch_size]
            print(f"Processing batch {i + 1}/{self.batch_cnt + 1}...")
            self.process_batch(self.data, batch_symbols)
import os

class DataExtractor:
    def __init__(self, data, n):
        self.data, self.n = data, n
        self.get_symbols()        
        self.divide_symbols()
        self.make_dirs()        
        print("Generating datasets for symbols...")
        for i in range(self.n):
            self.get_train_dataset(i, self.n, self.symbols_divided[i])
        print("Data extraction completed.")
            
    
    def get_symbols(self):
        print("Extracting symbols...")
        self.symbols = self.data['symbol'].unique()
        print(f"Total unique symbols: {len(self.symbols)}")
        return self.symbols
    
    
    def divide_symbols(self):
        print("Dividing symbols...")
        cnt_symbols = len(self.symbols)
        divisor = cnt_symbols // self.n
        indices = range(0, cnt_symbols, divisor)
        self.symbols_divided = [self.symbols[i: i + divisor] for i in indices]
        return self.symbols_divided
        
        
    def make_dirs(self):
        print("Checking or creating directory for datasets...")
        if not os.path.exists("train_dataset"):
            print("Creating 'train_dataset' directory...")
            os.makedirs("train_dataset")
        else:
            print("'train_dataset' directory already exists.")
    
    
    def get_train_dataset(self, i, n, symbols):
        total_symbols = len(symbols)
        for index, symbol in enumerate(symbols):
            temp = self.data[self.data['symbol'] == symbol]
            if len(temp) == 252:
                temp_path = os.path.join("train_dataset", f"train_{symbol}.csv")
                temp.to_csv(temp_path, index=False)
                print(f"Processing order: {i+1}/{n}, symbol {index+1}/{total_symbols}: {symbol} ... Saved!")
            else:
                print(f"Processing order: {i+1}/{n}, symbol {index+1}/{total_symbols}: {symbol} ... Skipped due to row count!")
class DivideData:
    def __init__(self, data, n):
        self.data = data
        self.n = n
        self.symbols = self.get_symbols()
        self.symbols_divided = self.divide_symbols()

    def get_symbols(self):
        print("Extracting symbols...")
        symbols = self.data['symbol'].unique().tolist()
        print(f"Total unique symbols: {len(symbols)}")
        return symbols

    def divide_symbols(self):
        print("Dividing symbols...")
        print(self.data)
        cnt_symbols = len(self.symbols)
        divisor = cnt_symbols // self.n
        symbols_divided = [self.symbols[i: i + divisor] for i in range(0, cnt_symbols - cnt_symbols % self.n, divisor)]
        if cnt_symbols % self.n:
            symbols_divided[-1].extend(self.symbols[cnt_symbols - cnt_symbols % self.n:])
        return symbols_divided
    
    def get_divided_symbols(self):
        return self.symbols_divided
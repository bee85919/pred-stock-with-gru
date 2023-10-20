class GetSymbol:
    def __init__(self, data):
        self.data = data
        self.symbols = self.get_symbols()

    def get_symbols(self):
        print("Extracting symbols...")
        symbols = self.data['symbol'].unique().tolist()
        print(f"Total unique symbols: {len(symbols)}")
        return symbols
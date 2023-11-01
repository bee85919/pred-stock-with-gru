import os
from Utils.envLoader import envLoader


class GetSymbol:

    def __init__(self, data):
        self.get_path = envLoader().get_path
        self.data = data
        self.symbols_path = self.get_path('symbols_path')
        self.symbols_length_path = self.get_path('symbols_length_path')
        

    def get_symbols(self):
        print("Extracting symbols...")
        symbols = self.data['symbol'].unique().tolist()
        chunked_symbols = [symbols[i:i + 100] for i in range(0, len(symbols), 100)]
        symbols_length = len(chunked_symbols)        
        print(f"Save total symbols: {len(symbols)}")
        print(f"Save total chunks: {symbols_length}")        
        with open(self.symbols_path, 'w') as f:
            f.write(str(chunked_symbols))
        with open(self.symbols_length_path, 'w') as f:
            f.write(str(symbols_length))
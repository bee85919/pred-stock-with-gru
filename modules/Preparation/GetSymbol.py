import os
from dotenv import load_dotenv


class GetSymbol:

    def __init__(self, data):
        
        load_dotenv()
        self.data = data
        self.symbols_path = os.getenv('symbols_path')


    def get_symbols(self):
        
        print("Extracting symbols...")
        symbols = self.data['symbol'].unique().tolist()
        chunked_symbols = [symbols[i:i + 100] for i in range(0, len(symbols), 100)]

        print(f"Save total symbols: {len(symbols)}")        
        with open(self.symbols_path, 'w') as f:
            f.write(str(chunked_symbols))
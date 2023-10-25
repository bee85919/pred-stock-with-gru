class GetSymbol:
    
    def __init__(self, data):        
        self.data = data


    def get_symbols(self):        
        print("Extracting symbols...")        
        symbols = self.data['symbol'].unique().tolist()        
        print(f"Total unique symbols: {len(symbols)}")        
        return symbols
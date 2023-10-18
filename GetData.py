import os

class GetData:
    def __init__(self, data, symbols_divided):
        self.data = data
        self.symbols_divided = symbols_divided

        self.make_dirs()        
        print("Generating datasets for symbols...")
        for i, divided_symbols in enumerate(self.symbols_divided):
            self.get_data_prepared(i, len(self.symbols_divided), divided_symbols)
        print("Data extraction completed.")

    def make_dirs(self):
        print("Checking or creating directory for datasets...")
        if not os.path.exists("data_prepared"):
            print("Creating 'data_prepared' directory...")
            os.makedirs("data_prepared")
        else:
            print("'data_prepared' directory already exists.")
    
    def get_data_prepared(self, i, n, symbols):
        total_symbols = len(symbols)
        for index, symbol in enumerate(symbols):
            temp = self.data[self.data['symbol'] == symbol]
            if len(temp) == 251:
                temp_path = os.path.join("data_prepared", f"{symbol}.csv")
                temp.to_csv(temp_path, index=False)
                print(f"Processing order: {i+1}/{n}, symbol {index+1}/{total_symbols}: {symbol} ... Saved!")
            else:
                print(f"Processing order: {i+1}/{n}, symbol {index+1}/{total_symbols}: {symbol} ... Skipped due to row count!")
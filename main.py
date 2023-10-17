from DataLoader import DataLoader

def main():    
    
    data_amex_path = './dataset/amex_data.csv'
    data_nsdq_path = './dataset/nasdaq_data.csv'
    data_nyse_path = './dataset/nyse_data.csv'

    data = DataLoader(data_amex_path, data_nsdq_path, data_nyse_path, period=12, year=2022, month=9)
    data = data.data
    print(data)

if __name__ == "__main__":
    main()
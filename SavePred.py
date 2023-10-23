import pandas as pd
import os

class SavePred:
    def __init__(self, start_date, input_dir='./data/pred/', output_file='./data/merged_result.csv'):
        self.start_date = start_date
        self.input_dir = input_dir
        self.output_file = output_file

    def generate_business_days(self):
        # pred_AMZN csv 파일의 길이 계산
        amzn_df = pd.read_csv(f'{self.input_dir}/pred_AMZN.csv')
        length = len(amzn_df)

        # start_date에서부터 해당 길이만큼의 business days를 생성
        business_days = pd.bdate_range(start=self.start_date, periods=length, freq='B')
        
        # 가장 늦은 날짜를 end_date로 설정
        self.end_date = business_days[-1]
        
        return business_days

    def merge_csv_files(self):
        business_days = self.generate_business_days()
        all_dfs = []

        print("Start merging CSV files...")

        for file in os.listdir(self.input_dir):
            if file.endswith('.csv'):
                symbol = file.replace('pred_', '').replace('.csv', '')
                print(f"Processing {file}...")

                df = pd.read_csv(f'{self.input_dir}/{file}')

                # 결측치가 있는 행 제거
                df.dropna(subset=['Adj Close'], inplace=True)

                # Adj Close가 0인 행도 제거
                df = df[df['Adj Close'] != 0]

                # 인덱스를 business_days로 설정
                df.index = business_days[:len(df)]
                df.index.name = 'Date'

                # Symbol 칼럼 추가
                df['Symbol'] = symbol

                # 칼럼 순서 변경
                df = df[['Symbol', 'Adj Close']]

                all_dfs.append(df)

        # 모든 DataFrame을 하나로 합치기
        result_df = pd.concat(all_dfs)
        
        # 인덱스와 Symbol로 정렬
        result_df.sort_values(by=['Symbol', 'Date'], inplace=True)

        # 결과 저장
        result_df.to_csv(self.output_file)

        print("CSV files merged successfully.")
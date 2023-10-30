# 설치
pip install requirements.txt

# 실행 준비
chmod +x ./scripts/train.sh
chmod +x ./scripts/load.sh
chmod +x ./run.sh

# 실행
echo INSTNACE_IP={EC2 인스턴스 IP}
echo POSTGRES_CONTAINER_ID={Docker의 postgresql container ID}
./run.sh

# input
- input_data : csv 데이터 셋 저장 폴더
- csv.txt : csv 경로 위치
- date.txt : 날짜, 학습 기간
- symbols_length.txt : symbols의 length
- symbols.txt : symbols 이차원 리스트
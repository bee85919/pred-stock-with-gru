#!/bin/bash
export INSTANCE_IP=$1
export POSTGRES_CONTAINER_ID=$2
export INPUT_PATH=$(pwd)/input
export INPUT_DATA_PATH=$(pwd)/input/csvs


echo "INSTANCE_IP: $INSTANCE_IP"
echo "POSTGRES_CONTAINER_ID: $POSTGRES_CONTAINER_ID"
echo "INPUT_PATH: $INPUT_PATH"
echo "INPUT_DATA_PATH: $INPUT_DATA_PATH"


export DATE=$(date '+%Y, %m, %d')
export PERIOD=300


echo "DATE: $DATE"
echo "PERIOD: $PERIOD"


echo "Create directories..."
mkdir -p $INPUT_PATH
mkdir -p $INPUT_DATA_PATH


echo "Extract data from DB..."
ssh -i $PEM_SIX ubuntu@$INSTANCE_IP "
  for table in amex nyse nasdaq; do
    CSV_PATH=/tmp/\$table.csv
    docker exec -i $POSTGRES_CONTAINER_ID psql -U postgres -d test01 -c \"
      COPY (
        SELECT 
          * 
        FROM 
          \$table
        WHERE 
          date >= CURRENT_DATE - interval '$PERIOD days'
        ORDER BY 
          company_code ASC, 
          date ASC
      ) 
      TO 
        '/tmp/\$table.csv' 
      WITH 
        CSV HEADER;
    \"
    docker cp $POSTGRES_CONTAINER_ID:\$CSV_PATH \$CSV_PATH
    docker exec -i $POSTGRES_CONTAINER_ID rm \$CSV_PATH
  done
"


echo "Download data from DB..."
for table in amex nyse nasdaq; do
  scp -i $PEM_SIX ubuntu@$INSTANCE_IP:/tmp/$table.csv $INPUT_DATA_PATH/$table.csv
done


echo "Write txt files..."
echo "[$DATE, $PERIOD]" > $INPUT_PATH/date.txt
echo "['$INPUT_DATA_PATH/amex.csv', '$INPUT_DATA_PATH/nasdaq.csv', '$INPUT_DATA_PATH/nyse.csv']" > $INPUT_PATH/csv.txt
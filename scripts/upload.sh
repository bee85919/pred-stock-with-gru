#!/bin/bash
export INSTANCE_IP=$1
export POSTGRES_CONTAINER_ID=$2

export RESULT_PATH=$(pwd)/data/result/result.csv
export DB_NAME="test01"
export TABLE_NAME="pred"


echo "Drop table..."
ssh -i $PEM_SIX ubuntu@$INSTANCE_IP "
  docker exec -i $POSTGRES_CONTAINER_ID psql -U postgres -d $DB_NAME -c \"
    DROP TABLE IF EXISTS $TABLE_NAME;
  \"
"


echo "Create table..."
ssh -i $PEM_SIX ubuntu@$INSTANCE_IP "
  docker exec -i $POSTGRES_CONTAINER_ID psql -U postgres -d $DB_NAME -c \"
    CREATE TABLE $TABLE_NAME (
      date DATE,
      symbol VARCHAR(50),
      close FLOAT8
    );
  \"
"


echo "Upload result.csv..."
scp -i $PEM_SIX $RESULT_PATH ubuntu@$INSTANCE_IP:/tmp/result.csv


echo "Copy result.csv to DB..."
ssh -i $PEM_SIX ubuntu@$INSTANCE_IP "
  docker exec -i $POSTGRES_CONTAINER_ID psql -U postgres -d $DB_NAME -c \"
    COPY $TABLE_NAME FROM '/tmp/result.csv' DELIMITER ',' CSV HEADER;
  \"
"


echo "Run upload.py..."
python ./src/upload.py


echo "Remove result.csv..."
ssh -i $PEM_SIX ubuntu@$INSTANCE_IP "
  rm /tmp/result.csv
"

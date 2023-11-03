#!/bin/bash
source ./config.sh


run_ssh() {
  local command=$1
  ssh -i $PEM_PATH ubuntu@$INSTANCE_IP "$command"
}


run_docker_exec() {
  local command=$1
  run_ssh "docker exec -i $POSTGRES_CONTAINER_ID psql -U postgres -d $DB_NAME -c \"$command\""
}


echo "Drop table..."
run_docker_exec "DROP TABLE IF EXISTS $TABLE_NAME;"


echo "Create table..."
run_docker_exec "CREATE TABLE $TABLE_NAME (date DATE, symbol VARCHAR(50), close FLOAT8);"


echo "Upload result.csv..."
scp -i $PEM_PATH $RESULT_PATH ubuntu@$INSTANCE_IP:$RESULT_INSTANCE_PATH


echo "Copy result.csv to postgresql..."
run_ssh "docker cp $RESULT_INSTANCE_PATH $POSTGRES_CONTAINER_ID:$RESULT_POSTGRESQL_PATH"


echo "Copy result.csv to DB..."
run_docker_exec "COPY $TABLE_NAME FROM '$RESULT_POSTGRESQL_PATH' DELIMITER ',' CSV HEADER;"


echo "Remove /tmp/result.csv inside Docker container..."
run_ssh "docker exec -i $POSTGRES_CONTAINER_ID rm $RESULT_POSTGRESQL_PATH"


echo "Run upload.py..."
python ./src/upload.py


echo "Remove result.csv..."
run_ssh "rm $RESULT_INSTANCE_PATH"
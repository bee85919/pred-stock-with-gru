INSTANCE_IP=$1
POSTGRES_CONTAINER_ID=$2


ssh -i $PEM_SIX ubuntu@$INSTANCE_IP "
  for table in pred; do
    CSV_PATH=/tmp/\$table.csv
    docker exec -i $POSTGRES_CONTAINER_ID psql -U postgres -d test01 -c \"
      COPY (
        SELECT 
          * 
        FROM 
          \$table
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
for table in pred; do
  scp -i $PEM_SIX ubuntu@$INSTANCE_IP:/tmp/$table.csv ~/Desktop/$table.csv
done


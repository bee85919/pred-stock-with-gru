from hdfs import InsecureClient
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2
import pendulum

local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 31, tzinfo=local_tz),
    'retry_delay': timedelta(minutes=30),
}

dag = DAG(
    'hdfs_pred_dag',
    default_args=default_args,
    schedule_interval='00 10 * * *',
    catchup=False,
    tags=['LAST'],
)

def fetch_from_postgres():
    conn = psycopg2.connect(
        host="host_ip",
        port="host_port",
        dbname="db_name",
        user="user",
        password="password"
    )
    query = "SELECT * FROM your_table_name"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def To_hdfs(df):
    hdfs_client = InsecureClient(f'http://{host_ip}:{hdfs_port}', user='airflow')
    hdfs_upload_path = '/path/to/output.csv'
    with hdfs_client.write(hdfs_upload_path) as writer:
        df.to_csv(writer, index=False)

def pipeline():
    df = fetch_from_postgres()
    To_hdfs(df)

with dag:
    task_fetch_and_write = PythonOperator(
        task_id='pred_from_postgres_to_hdfs',
        python_callable=pipeline,
    )

if __name__ == "__main__":
    dag.run()
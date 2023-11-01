from hdfs import InsecureClient
import pandas as pd
from sqlalchemy import create_engine


def fetch():
    conn_str = "postgresql://manager:'password'@'ip_address':'port'/'db_name'"
    engine = create_engine(conn_str)
    print("Connected to Database")
    print("Fetching Data")
    query = "SELECT * FROM 'table_name'"
    df = pd.read_sql(query, engine)
    return df


def write(df):
    print("Uploading to HDFS")
    hdfs_client = InsecureClient("'ip_address':'port'")
    hdfs_upload_path = '/path/to/result.csv'
    with hdfs_client.write(hdfs_upload_path) as writer:
        df.to_csv(writer, index=False)


df = fetch()
write(df)
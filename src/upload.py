import os
import pandas as pd
from hdfs import InsecureClient
from sqlalchemy import create_engine


conn_str = "postgresql://manager:tPZm7M7gAC8UKeNAf3yf@172.31.10.86:5432/test01"
hdfs_adr = "http://172.31.3.34:50070"
result = "/home/ubuntu/pred/2311/result.csv"


def fetch():
    engine = create_engine(conn_str)
    print("DB connected")
    query = "SELECT * FROM pred"
    df = pd.read_sql(query, engine)    
    print("Data fetched")
    return df


def write(df):
    print("Uploading..")
    client = InsecureClient(hdfs_adr)
    with client.write(result, overwrite=True) as writer:
        df.to_csv(writer, index=False)
        print("Success!")
    check(client, result)
        
        
def check(client, result):
    tmp = os.path.dirname(result)
    lst = client.list(tmp)
    if 'result.csv' in lst:
        print("File exists")
    else:
        print("File doesn't exist")


df = fetch()
write(df)
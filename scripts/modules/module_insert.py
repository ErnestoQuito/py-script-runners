import pandas as pd
import sqlalchemy
from pandas import DataFrame

def insert_table(data: DataFrame, msg_boolean: bool, connect, table_name, schema_name):   

    if msg_boolean:
        data.to_sql(table_name, con = connect, schema=schema_name, if_exists='append', chunksize=200, method='multi', index=False)
        
    print('INSERT: Process successful')
    
    return True
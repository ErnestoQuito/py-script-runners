import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from pandas import DataFrame

def insert(data: DataFrame, host, name, user, password, driver, schema, table_name, port):   

    url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, name)
    engine = create_engine(url)

    data.to_sql(table_name, con = engine, schema=name, if_exists='append', chunksize=200, method='multi', index=False)
        
    print('Process successful')
    
    return True
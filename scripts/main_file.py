"""
import pymysql
from sqlalchemy import create_engine

conexion = pymysql.connect(
                        host='198.100.154.133',
                        port=3306,
                        user='admin_servicio',
                        password='ZJv5c7CspU',        
                        database='admin_servicio',
                    )

cursor=conexion.cursor()
print(cursor)
conexion.commit()
conexion.close()

#url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('admin_servicio', 'ZJv5c7CspU', 'http://hasber.net/phpmyadmin/', 3306, 'admin_servicio')
#engine = create_engine(url)

#print(engine)

"""
"""
#-------------------------------------------------------


from modules.services_db import MSSQLConection

mssql = MSSQLConection(h_host='198.100.154.133',h_db_name='admin_servicio',h_user='admin_servicio',h_pass='ZJv5c7CspU',h_port=3306)
mssql.open_conn_pymysql()
cursor = mssql.conn_pymysql.cursor()

cursor.execute("select * from configuracion_sftp;")
resultado=cursor.fetchone()
# print(cursor.description)
print(resultado)
try:
    columns: list = [col[0] for col in cursor.description]
    table_dict: dict = {}
    for idx, i in enumerate(resultado):
        table_dict[columns[idx]] = i

    print(table_dict)
except Exception as err:
    print('error')
    print(err.__class__, err)
finally:
    mssql.close_conn()
"""

"""
import pandas as pd
import os
from pandas import DataFrame
from modules.services_db import MariaDbConnection

HOST = os.getenv('HOST', '198.100.154.133')
NAME = os.getenv('HOST', 'admin_servicio')
USER = os.getenv('HOST', 'admin_servicio')
PASSW = os.getenv('HOST', 'ZJv5c7CspU')
PORT = os.getenv('PORT', 3306)

maria = MariaDbConnection(h_host=HOST, h_db_name=NAME, h_user=USER, h_pass=PASSW, h_port=3306)
engine = maria.open_conn_engine()

df=pd.DataFrame([
        ['terminado',   'yorman']
        ], columns=['estado', 'nombre'])
print(df)

df.to_sql('prueba', con = engine, schema='admin_servicio', if_exists='append', chunksize=200, method='multi', index=False)

print('hecho')
"""
from modules.functions_for_tables import get_date

a = get_date()
print(a)
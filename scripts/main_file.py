import pymysql
from sqlalchemy import create_engine

conexion = pymysql.connect(
                        host='http://hasber.net/phpmyadmin/',
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
#-------------------------------------------------------

import mysql.connector
from modules.config import MSSQLConection

mssql = MSSQLConection()
#mssql.open_conn()

conexion = mysql.connector.connect(host={mssql.HOST},user={mssql.HOST},password={mssql.PASSWORD},db={mssql.NAME})
mssql.conn = conexion
if mssql.conn.is_connected():
    print("Conexion existosa")
else:
    print("valide conexion")

#-------------------------------------------------------

import mysql.connector

conexion = mysql.connector.connect(host='http://hasber.net/phpmyadmin/',port='3306', user='admin_servicio',password='ZJv5c7CspU',db='admin_servicio')
cursor = conexion.cursor()

if cursor:
    print("Conexion existosa")
else:
    print("valide conexion")

"""

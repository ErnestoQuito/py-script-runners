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
print(resultado)


mssql.close_conn()


"""
from modules.module_read_files import read_pdf_paginas

source_ = r"D:\runners_source_files\notificaciones\2023\02\01"

var=read_pdf_paginas(source_)

print(var)


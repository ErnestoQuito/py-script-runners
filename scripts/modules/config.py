import sqlalchemy
from typing import List
from pandas import DataFrame
import os
import mysql.connector
import pymysql
from dotenv import load_dotenv
load_dotenv()

class MSSQLConection:
    HOST = ''
    NAME = ''
    USER = ''
    PASSWORD = ''
    DRIVER = ''

    conn = None
    engine = None

    def __init__(self):
        self.HOST = os.getenv("h_host")
        self.NAME = os.getenv("h_db_name")
        self.USER = os.getenv("h_user")
        self.PASSWORD = os.getenv("h_pass")
        self.PORT = os.getenv("h_port")
 
    def open_conn(self):
        #sc = f"DRIVER={self.DRIVER};SERVER={self.HOST};DATABASE={self.NAME};UID={self.USER};PWD={self.PASSWORD}"
        conexion = mysql.connector.connect(host={self.HOST},port={self.PORT},user={self.HOST},password={self.PASSWORD},db={self.NAME})
        self.conn = conexion
        if self.conn.is_connected():
            print("Conexion existosa")
        else:
            print("valide conexion")

    def open_conn_engine(self):
        #sc = f"mssql+pyodbc://{self.USER}:{self.PASSWORD}@{self.HOST}:1433/{self.NAME}?driver={driver}"
        sc="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(self.USER, self.PASSWORD, self.HOST, self.PORT, self.NAME)
        self.engine = sqlalchemy.create_engine(sc)
        return self.engine.connect()

    def open_conn_pymysql(self):
        conexion = pymysql.connect(host=self.HOST,
                                    port=self.PORT,
                                    user=self.USER,
                                    password=self.PASSWORD,        
                                    database=self.NAME,
                                )
        self.conn=conexion.cursor()

    def close_conn(self):
        if self.conn:
            self.conn.close()
    
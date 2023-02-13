import sqlalchemy
from typing import List
from pandas import DataFrame
import os
import mysql.connector
import pymysql

class MariaDbConnection:
    HOST = ''
    NAME = ''
    USER = ''
    PASSWORD = ''
    DRIVER = ''

    conn = None
    conn_pymysql = None
    engine = None

    def __init__(self,h_host,h_db_name,h_user,h_pass,h_port):
        self.HOST = h_host
        self.NAME = h_db_name
        self.USER = h_user
        self.PASSWORD = h_pass
        self.PORT = h_port

    def open_conn(self):
        #sc = f"DRIVER={self.DRIVER};SERVER={self.HOST};DATABASE={self.NAME};UID={self.USER};PWD={self.PASSWORD}"
        conexion = mysql.connector.connect(host=self.HOST,port=self.PORT,user=self.USER,password=self.PASSWORD,db=self.NAME)
        self.conn = conexion

    def open_conn_engine(self):
        #sc = f"mssql+pyodbc://{self.USER}:{self.PASSWORD}@{self.HOST}:1433/{self.NAME}?driver={driver}"
        sc="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(self.USER, self.PASSWORD, self.HOST, self.PORT, self.NAME)
        self.engine = sqlalchemy.create_engine(sc, isolation_level='AUTOCOMMIT')
        return self.engine.connect()

    def open_conn_pymysql(self):
        conexion = pymysql.connect(host=self.HOST,
                                    port=self.PORT,
                                    user=self.USER,
                                    password=self.PASSWORD,
                                    database=self.NAME,
                                )
        self.conn_pymysql=conexion

    def close_conn(self):
        if self.conn:
            self.conn.close()

        if self.conn_pymysql:
            self.conn_pymysql.close()

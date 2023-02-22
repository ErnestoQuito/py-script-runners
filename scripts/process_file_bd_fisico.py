import os
from datetime import datetime
import pandas as pd
from modules.functions_for_tables import select_table,ejecutar_sp,select_df_stage
from modules.services_db import MariaDbConnection
from modules.module_insert import insert_table
from tranform.tranform_fisico import tranform_data_fisico


# VARIABLE FOR PROCESS
HOST = os.getenv('HOST', '198.100.154.133')
NAME = os.getenv('HOST', 'admin_servicio')
USER = os.getenv('HOST', 'admin_servicio')
PASSW = os.getenv('HOST', 'ZJv5c7CspU')
PORT = os.getenv('PORT', 3306)

ID_TABLE_DB_NOTIF = 1
WHERE_COL_DB_NOTIF = 'flag_estado_procesado'
TABLE_DB = 'configuracion_db'
WHERE_COL_DB = 'id_db'
ID_TABLE_DB = 5
ID_TEMP_DB = 6
SP_DB = 'configuracion_store_procedure'
WHERE_COL_SP = 'id_sp'
ID_SP = 3


maria = MariaDbConnection(h_host=HOST, h_db_name=NAME, h_user=USER, h_pass=PASSW, h_port=3306)
maria.open_conn()
engine = maria.open_conn_engine()
try:
    table_db_notf: dict = select_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, id_table=ID_TABLE_DB_NOTIF)
    a_bd_noft= table_db_notf.get("tabla")
    
    table_db: dict = select_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, id_table=ID_TABLE_DB)
    a_bd= table_db.get("base_datos")
    a_table= table_db.get("tabla")

    temp_db: dict = select_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, id_table=ID_TEMP_DB)
    a_temp= temp_db.get("tabla")

    sp_db: dict = select_table(maria.conn, table_name=SP_DB, where_col=WHERE_COL_SP, id_table=ID_SP)
    a_sp= sp_db.get("name_procedure")
    
    df_read = select_df_stage(connect=engine, table_name=a_bd_noft, where_name=WHERE_COL_DB_NOTIF, id_flag=0)
    df_read.drop(['flag_estado_procesado'], axis=1, inplace=True)
    df_notif=tranform_data_fisico(df_read)
    
    if df_notif.empty:
        print("Proceso cancelado: No se encontraron datos para la carga de información")
    else:      
        print("Inciando insert")
        msg_insert_temp = insert_table(data=df_notif, msg_boolean=True, connect=engine, table_name=a_temp, schema_name=a_bd)
        ejecutar_sp(maria.conn, query=a_sp)

        print('OK -> Proceso finalizado')
    
except Exception as err:
    print(err.__class__, err, err.__traceback__.tb_lineno)
finally:
    maria.close_conn()
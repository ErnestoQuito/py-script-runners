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

ID_TABLE_STAGE_DB = 2
ID_TABLE_DB = 5
TABLE_DB = 'configuracion_db'
WHERE_COL_DB = 'id_db'
ID_TEMP = 6
ID_SP = 3
SP_DB = 'configuracion_store_procedure'
WHERE_COL_SP = 'id_sp'

maria = MariaDbConnection(h_host=HOST, h_db_name=NAME, h_user=USER, h_pass=PASSW, h_port=3306)
maria.open_conn()
engine = maria.open_conn_engine()
try:
    stage_db: dict = select_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, id_table=ID_TABLE_STAGE_DB)
    a_bd_stage= stage_db.get("tabla")
    
    table_db: dict = select_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, id_table=ID_TABLE_DB)
    a_bd= table_db.get("base_datos")
    a_table= table_db.get("tabla")

    temp_db: dict = select_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, id_table=ID_TEMP)
    a_temp= temp_db.get("tabla")

    sp_db: dict = select_table(maria.conn, table_name=SP_DB, where_col=WHERE_COL_SP, id_table=ID_SP)
    a_sp= sp_db.get("name_procedure")
    a_fecha_inicio= sp_db.get("fecha_inicio")
    a_fecha_fin= sp_db.get("fecha_fin")
    
    df_read = select_df_stage(connect=engine, table_name=a_bd_stage)
    
    df_notif=tranform_data_fisico(df_read)
    
    if df_notif.empty:
        print("Proceso cancelado: No se encontraron datos para la carga de información")
    else:      
        print("Inciando insert")
        msg_insert_temp = insert_table(data=df_notif, msg_boolean=True, connect=engine, table_name=a_temp, schema_name=a_bd)
        #msg_insert = insert_table(data=df_notif, msg_boolean=True, connect=engine, table_name=a_table, schema_name=a_bd)
        
        ejecutar_sp(maria.conn, query=a_sp, fechaini=a_fecha_inicio, fechafin=a_fecha_fin)

        print('OK -> Proceso finalizado')
    
    
except Exception as err:
    print(err.__class__, err, err.__traceback__.tb_lineno)
finally:
    maria.close_conn()
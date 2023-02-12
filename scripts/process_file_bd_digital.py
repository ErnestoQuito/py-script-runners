import os
from datetime import datetime
from modules.functions_for_tables import select_table,delete_table
from modules.commons import set_format_path_to_date
from modules.services_db import MariaDbConnection
from modules.module_read_files import read_files_excel
from modules.module_insert import insert_table
from tranform.transform_digital import tranform_data_digital
from tranform.tranform_fisico import tranform_data_fisico


# VARIABLE FOR PROCESS
HOST = os.getenv('HOST', '198.100.154.133')
NAME = os.getenv('HOST', 'admin_servicio')
USER = os.getenv('HOST', 'admin_servicio')
PASSW = os.getenv('HOST', 'ZJv5c7CspU')
PORT = os.getenv('PORT', 3306)

TABLE_DB = 'base_notificaciones'
SCHEMA_DB = 'admin_servicio'
WHERE_COL_DB = 'id_loc'

TABLE_DB_DIG = 'base_digital'
SCHEMA_DB_DIG = 'admin_servicio'
WHERE_COL_DB_DIG = 'file_name'

maria = MariaDbConnection(h_host=HOST, h_db_name=NAME, h_user=USER, h_pass=PASSW, h_port=3306)
maria.open_conn()
engine = maria.open_conn_engine()
try:
    table_file: dict = select_table(maria.conn, table_name=TABLE_FILE, where_col=WHERE_COL_FILE, id_table=ID_TABLE_FILE)

    print(table_file)
    """
    if df_read.empty:
        print("Proceso cancelado: No se encontraron datos para la carga de información")
    else:
        print("Iniciando delete")
        msg_delete = delete_table(maria.conn, table_name=TABLE_DB, where_col=WHERE_COL_DB, file_name =file_name)
        
        print("Inciando insert")
        msg_insert = insert_table(data=df_read, msg_boolean=msg_delete, connect=engine, table_name=TABLE_DB, schema_name=SCHEMA_DB)

        df_digital= tranform_data_digital(df_read)
        df_fisico= tranform_data_fisico(df_read)

        msg_digital = insert_table(data=df_read, msg_boolean=msg_insert, connect=engine, table_name=TABLE_DB, schema_name=SCHEMA_DB)
        msg_digital = insert_table(data=df_read, msg_boolean=msg_insert, connect=engine, table_name=TABLE_DB, schema_name=SCHEMA_DB)

        print('OK: Proceso finalizado')
    """

except Exception as err:
    print(err.__class__, err)
finally:
    maria.close_conn()

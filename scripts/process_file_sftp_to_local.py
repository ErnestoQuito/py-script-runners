import os
from datetime import datetime
from modules.functions_for_tables import select_table
from modules.commons import set_format_path_to_date
from modules.services_db import MariaDbConnection
from modules.services_sftp import ServicesSFTP

# VARIABLE FOR PROCESS
HOST = os.getenv('HOST', '198.100.154.133')
NAME = os.getenv('HOST', 'admin_servicio')
USER = os.getenv('HOST', 'admin_servicio')
PASSW = os.getenv('HOST', 'ZJv5c7CspU')
PORT = os.getenv('PORT', 3306)

ID_TABLE_SFTP = 1
TABLE_SFTP = 'configuracion_sftp'
WHERE_COL_SFTP = 'id_sftp'
ID_TABLE_FILE = 1
TABLE_FILE = 'configuracion_ruta_local'
WHERE_COL_FILE = 'id_loc'


maria = MariaDbConnection(h_host=HOST, h_db_name=NAME, h_user=USER, h_pass=PASSW, h_port=3306)
maria.open_conn()
try:
    table_sftp: dict = select_table(maria.conn, table_name=TABLE_SFTP, where_col=WHERE_COL_SFTP, id_table=ID_TABLE_SFTP)
    format_path: str = set_format_path_to_date(table_sftp['ruta'], unix=True, auto_date=False, my_date=datetime(2023, 2, 1))

    # SFTP
    serv_sftp = ServicesSFTP(host=table_sftp['servidor'], user=table_sftp['usuario'], password=table_sftp['contrasena'])
    serv_sftp.set_cnopts(path_file=table_sftp['ruta_archivo_redes_conocidas'])
    list_path_files: list = serv_sftp.list_files(remote_path_file=format_path)
    # LOCAL
    table_file: dict = select_table(maria.conn, table_name=TABLE_FILE, where_col=WHERE_COL_FILE, id_table=ID_TABLE_FILE)
    format_path_file_target: str = set_format_path_to_date(table_file['ruta_destino'], unix=False, auto_date=False, my_date=datetime(2023, 2, 1))
    result_path_files_saved = serv_sftp.download_files(
        remote_path_file=list_path_files, local_path_file=format_path_file_target
    )
    

except Exception as err:
    print(err.__class__, err)
finally:
    maria.close_conn()

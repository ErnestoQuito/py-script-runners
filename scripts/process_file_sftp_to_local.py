import os
from datetime import datetime
from modules.functions_for_tables import select_table
from modules.functions_for_tables import insert_to_table
from modules.commons import set_format_path_to_date_per
from modules.services_db import MariaDbConnection
from modules.services_sftp import ServicesSFTP
from modules.commons import get_metada_from_file
from modules.commons import create_folders

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
    # CONTAINER EXCEL AND PDF
    format_path: str = set_format_path_to_date_per(table_sftp['ruta'], unix=True, auto_date=False, my_date=datetime(2023, 3, 3))
    format_path_pdf = f'{format_path}/Fisico'
    # SFTP
    serv_sftp = ServicesSFTP(host=table_sftp['servidor'], user=table_sftp['usuario'], password=table_sftp['contrasena'])
    serv_sftp.set_cnopts(path_file=table_sftp['ruta_archivo_redes_conocidas'])
    list_path_files: list = serv_sftp.list_files(remote_path_file=format_path)
    list_path_files_pdf: list = serv_sftp.list_files(remote_path_file=format_path_pdf)

    # LOCAL
    table_file: dict = select_table(maria.conn, table_name=TABLE_FILE, where_col=WHERE_COL_FILE, id_table=ID_TABLE_FILE)
    format_path_file_target: str = set_format_path_to_date_per(
        table_file['ruta_destino'], unix=False, auto_date=False, my_date=datetime(2023, 3, 3)
    )

    # CREATE FOLDER ROOT
    print(format_path_file_target)
    create_folders(new_path=format_path_file_target)
    # DOWNLOAD EXCEL
    result_path_files_saved = serv_sftp.download_files(
        remote_path_file=list_path_files, local_path_file=format_path_file_target
    )
    # DOWNLOAD PDF
    result_path_files_pdf_saved = serv_sftp.download_files(
        remote_path_file=list_path_files_pdf, local_path_file=format_path_file_target
    )
    # CONCAT RESULTS
    result_path_files_saved += result_path_files_pdf_saved
    # SAVE RESULTS
    for item in result_path_files_saved:
        result_meta_data_file = get_metada_from_file(item)
        insert_to_table(maria.conn, get_metada_from_file(item), 'log_archivos')

except Exception as err:
    print(err.__class__, err)
finally:
    maria.close_conn()

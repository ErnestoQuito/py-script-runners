import os
from modules.commons import get_metada_from_file
from modules.functions_for_tables import insert_to_table
from modules.services_db import MariaDbConnection

path_file = "D:\\runners_source_files\\notificaciones\\2023\\02\\01\\Fisico 01.02.2023.xls"
HOST = os.getenv('HOST', '198.100.154.133')
NAME = os.getenv('NAME', 'admin_servicio')
USER = os.getenv('USER', 'admin_servicio')
PASSW = os.getenv('HOPASSWST', 'ZJv5c7CspU')
PORT = os.getenv('PORT', 3306)

maria = MariaDbConnection(h_host=HOST, h_db_name=NAME, h_user=USER, h_pass=PASSW, h_port=PORT)
maria.open_conn()
result_meta_data = get_metada_from_file(path_file=path_file)
# print(result_meta_data['archivo_ruta'])
try:
    insert_to_table(maria.conn, result_meta_data, "log_archivos")
except Exception as err:
    print(err.__class__, err)
finally:
    maria.close_conn()
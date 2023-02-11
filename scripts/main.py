import os
from modules.services_sftp import ServicesSFTP

host = '192.168.18.118'
user = 'sftp'
passw = 'sftp'
known_hosts = 'C:\\Users\\lycan\\.ssh\\known_hosts'
path_remote = '/home/sftp/notificacion/2023/02/01'

services_ftp = ServicesSFTP(
    host=host, user=user, password=passw
)

services_ftp.set_cnopts(known_hosts)

services_ftp.list_files(remote_path_file=path_remote)

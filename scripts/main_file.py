import os
from modules.commons import find_excel
from modules.module_read_files import read_files_excel

path_file=['D:\\runners_source_files\\notificaciones\\2023\\02\\01\\Fisico 01.02.2023.xls', 'D:\\runners_source_files\\notificaciones\\2023\\02\\01\\Fisico 02.02.2023.xls',
'D:\\runners_source_files\\notificaciones\\2023\\02\\01\\BUSINESS ANALYTICS 2021-2.pdf','D:\\runners_source_files\\notificaciones\\2023\\02\\01\\conf_hasber.txt']

lsfiles = find_excel(path_file)

print(lsfiles)

data = read_files_excel(lsfiles)

print(len(data))



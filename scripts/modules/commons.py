import os
import shutil
from datetime import datetime

def finder_files(path_string: str):
    return [os.path.abspath(resource.path) for resource in os.scandir(path_string)]

def copy_files(source: str, target: str):
    """Funcion para copiar archivos de un origen a un destino

    Args:
        source (str): Ruta del archivo completo origen.
        target (str): Ruta del archivo completo destino.

    Returns:
        _type_: Retorna la ruta del archivo copiado en la ruta de destino.
    """
    return shutil.copy2(source, target)

def find_excel(path_file: str):
    """Funcion ´para encontrar los archivos excel de un lista

    Args:
        path_file (str): ruta de archivos

    Returns:
        list: Retorna una lista solo con la ruta de los archivos excel
    """
    files = finder_files(path_file)

    archivos=[]

    for i in files:
        if i.endswith('.xls'):
            archivos.append(i)
    #tail = [os.path.basename(x) for x in  archivos]

    return archivos

def set_format_path_to_date(
    root_path: str,
    auto_date: bool = True,
    unix: bool = False,
    my_date: datetime = datetime.now()
    ):

    if unix:
        format_root_path = f'{root_path}/%Y/%m/%d'
    else:
        format_root_path = os.path.join(os.path.abspath(root_path), '%Y', '%m', '%d')

    if auto_date:
        return my_date.strftime(format_root_path)
    return my_date.strftime(format_root_path)

def get_metada_from_file(path_file: str):
    path_local = os.path.dirname(path_file).replace('\\', '\\\\')
    name_file = os.path.basename(path_file)
    size_file = os.path.getsize(path_file)
    time_created = datetime.fromtimestamp(os.path.getctime(path_file)).strftime('%Y-%m-%d %H:%M:%S.%f')
    time_modified = datetime.fromtimestamp(os.path.getmtime(path_file)).strftime('%Y-%m-%d %H:%M:%S.%f')
    return dict(
        archivo_ruta=path_local,
        archivo_nombre=name_file,
        archivo_tamano_bytes=size_file,
        archivo_tiempo_creado=time_created,
        archivo_tiempo_modificado=time_modified
    )

def create_folders(new_path: str):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path

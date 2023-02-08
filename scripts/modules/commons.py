import os
import shutil

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

def find_excel(path_file):
    """Funcion ´para encontrar los archivos excel de un lista

    Args:
        path_file (list): lista de archivos

    Returns:
        list: Retorna una lista solo con la ruta de los archivos excel
    """
    archivos=[]

    for i in path_file:
        if i.endswith('.xls'):
            archivos.append(i)
    #tail = [os.path.basename(x) for x in  archivos]    
        
    return archivos

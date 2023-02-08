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

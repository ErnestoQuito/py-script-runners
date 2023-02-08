import pandas as pd

def read_files_excel(path_file):
    """Funcion de lectura de archivos excel

    Args:
        path_file (list): lista de archivos

    Returns:
        dataFrame: Retorna el contenido de los archivos excel unificados
    """
    all_files = []
    for file in path_file:
        df=pd.read_excel(file)
        all_files.append(df)
    
    df = pd.concat(all_files,ignore_index='True')  
    
    return df
    
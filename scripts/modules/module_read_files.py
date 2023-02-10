import pandas as pd
import os
from datetime import datetime

def read_files_excel(path_file: str):
    """Funcion de lectura de archivos excel

    Args:
        path_file (str): ruta de archivos

    Returns:
        dataFrame: Retorna el contenido de los archivos excel unificados
    """
    from modules.commons import finder_files

    files = finder_files(path_file)
    
    all_files = []
    for i in files:
        if i.endswith('.xls'):
            df=pd.read_excel(i)
            df['FileName']= os.path.basename(i)
            all_files.append(df)
    
    df = pd.concat(all_files,ignore_index='True')  
    
    df.rename(columns={
        'Guía' : 'Guia',
        'Resolución' : 'Resolucion',
        'Fecha Resolución' : 'FechaResolucion',
        'Expediente' : 'Expediente',
        'Teléfono' : 'Telefono',
        'Nombre Cliente' : 'NombreCliente',
        'Analista' : 'Analista',
        'Fecha Despacho' : 'FechaDespacho',
        'Dirección' : 'Direccion',
        'Distrito' : 'Distrito',
        'Provincia' : 'Provincia',
        'Departamento' : 'Departamento',
        'Anexo' : 'Anexo',
        'Tipo Reenvío' : 'TipoReenvio',
        'Tipo Solucion' : 'TipoSolucion',
        'Número Reenvío' : 'NumeroReenvio',
        'Correo electrónico' : 'CorreoElectronico',
        'Fecha Reclamo' : 'FechaReclamo',
        'Canal Despacho' : 'CanalDespacho',
        'Instancia' : 'Instancia',
        'NOTIFICACION_CORREO' : 'NotificacionCorreo',
        'FileName' : 'FileName',
    }, inplace=True)

    df['LoadDate']= datetime.now()


    return df
    

def read_pdf_paginas(path_file: str):        
    from PyPDF2 import PdfFileReader
    from modules.commons import finder_files

    files = finder_files(path_file)

    df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])

    for f in files:
        if f.endswith(".pdf"):
            pdf=PdfFileReader(open(os.path.join(path_file, f),'rb'), strict=False)
            df2 = pd.DataFrame([[os.path.basename(f), os.path.join(path_file,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
            df = pd.concat([df,df2])
            
    df.reset_index(drop=True, inplace=True)

    return df


def val_pdf_excel(path_file: str):

    # Prueba de validación, el resultado tiene que identificar los registros de diferencia o en su defecto los pdf

    df_exc = read_files_excel(path_file)
    df_pdf = read_pdf_paginas(path_file)

    texcel = len(df_exc)
    tpdf = len(df_pdf)

    if texcel == tpdf :
        print('Ok:: Archivos correctos', texcel)
        return True

    if texcel > tpdf :
        print(f'W:: Excel: {texcel} registros - Pdf: {tpdf} archivos', )
        return False
    else:
        print(f'W:: Pdf: {tpdf} archivos - Excel: {texcel} registros')
        return False
    
     
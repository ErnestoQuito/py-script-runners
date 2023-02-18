import pandas as pd
from pandas import DataFrame
from datetime import datetime

def transform_notificaciones(df_excel: DataFrame,df_pdf: DataFrame):

    df_excel.rename(columns={
                    'Guía' : 'guia',
                    'Resolución' : 'resolucion',
                    'Fecha Resolución' : 'fecha_resolucion',
                    'Expediente' : 'expediente',
                    'Teléfono' : 'telefono',
                    'Nombre Cliente' : 'nombre_cliente',
                    'Analista' : 'analista',
                    'Fecha Despacho' : 'fecha_despacho',
                    'Dirección' : 'direccion',
                    'Distrito' : 'distrito',
                    'Provincia' : 'provincia',
                    'Departamento' : 'departamento',
                    'Anexo' : 'anexo',
                    'Tipo Reenvío' : 'tipo_reenvio',
                    'Tipo Solucion' : 'tipo_solucion',
                    'Número Reenvío' : 'numero_reenvio',
                    'Correo electrónico' : 'correo_electronico',
                    'Fecha Reclamo' : 'fecha_reclamo',
                    'Canal Despacho' : 'canal_despacho',
                    'Instancia' : 'instancia',
                    'NOTIFICACION_CORREO' : 'notificacion_correo',
                    'FileName' : 'file_name',
                }, inplace=True)

    df_excel['load_date']= datetime.now()
    df_excel = df_excel.set_index("resolucion")
    df_pdf = df_pdf.set_index("resolucion")

    df = pd.merge(df_excel, df_pdf, how="left", left_index=True, right_index=True)
    #df_notif=df_excel.merge(df_pdf,how='left',on="resolucion")
    df = df.drop_duplicates()
    #df.set_index('resolucion', inplace=True)
    df=df.reset_index()
    df['fecha_resolucion'] =  pd.to_datetime(df['fecha_resolucion'], format='%d/%m/%Y')
    df['fecha_despacho'] =  pd.to_datetime(df['fecha_despacho'], format='%d/%m/%Y')
    df['fecha_reclamo'] =  pd.to_datetime(df['fecha_reclamo'], format='%d/%m/%Y')

    return df
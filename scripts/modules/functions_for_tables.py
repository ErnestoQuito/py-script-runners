from sqlalchemy import text
import pandas as pd
from datetime import datetime, timedelta

def select_table(connect, table_name, where_col, id_table) -> dict:
    """Funcion para obtener registro de tablas.

    Args:
        connect (conn): Objeto para la conexion de una base de datos.
        table_name (str): Objeto para la conexion de una base de datos.
        id_table (str): Es el identificador de la tabla

    Returns:
        dict: Retorna el resultado de la consulta en formato diccionario.
    """

    cursor = connect.cursor()
    cursor.execute(f'SELECT * FROM {table_name} WHERE {where_col} = {id_table};')
    resultado=cursor.fetchone()
    columns: list = [col[0] for col in cursor.description]
    table_dict: dict = {}

    for idx, i in enumerate(resultado):
        table_dict[columns[idx]] = i
    cursor.close()
    return table_dict

def get_date():
    date_string_ini = (datetime.now() - timedelta(days=0)).strftime('%Y-%m-%d 00:00:00') 
    date_string_fin = (datetime.now() - timedelta(days=0)).strftime('%Y-%m-%d 23:59:59')

    date_start = datetime.strptime(date_string_ini, "%Y-%m-%d %H:%M:%S")
    date_end = datetime.strptime(date_string_fin, "%Y-%m-%d %H:%M:%S")      

    return date_start, date_end

def delete_table(connect, table_name, where_col, file_name: list) -> dict:

    cursor = connect.cursor()
    for i in file_name:
        cursor.execute(f"DELETE FROM {table_name} WHERE {where_col} = '{i}';")
        cursor.commit()
    cursor.close()
    return True

def insert_to_table(conn, data: dict, table_name: str):
    cursor = conn.cursor()
    cols = ', '.join([i for i in data])
    rows = ', '.join([f"'{i}'" for i in data.values()])
    sql_statement = f'INSERT INTO {table_name}({cols}) VALUE ({rows})'
    cursor.execute(sql_statement)
    conn.commit()
    cursor.close()
    return

def ejecutar_sp(connect, query):
    """
    if fechaini == None:
        dates=get_date()
        fechaini = dates[0]
        fechafin   = dates[1]
    start_date=fechaini
    end_date=fechafin
    
    sp=query.replace("p_FechaInicio",(str(start_date))).replace("p_FechaFin",(str(end_date)))
    """
    connect.autocommit = True
    cursor = connect.cursor()
    cursor.execute(query)
    #codigo=cursor.fetchone()
    cursor.close()
    print("SP:: Process successful")

    return True

def select_df_stage(connect, table_name, where_name, id_flag) -> dict:

    query = f""" SELECT * FROM {table_name} WHERE {where_name} = {id_flag} ; """
    df = pd.read_sql_query(text(query), connect)

    return df

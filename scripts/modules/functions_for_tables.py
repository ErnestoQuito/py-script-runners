
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

def delete_table(connect, table_name, where_col, file_name: list) -> dict:

    cursor = connect.cursor()
    for i in file_name:
        cursor.execute(cursor.execute(f"DELETE FROM {table_name} WHERE {where_col} = '{i}';"))
        #cursor.commit()
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

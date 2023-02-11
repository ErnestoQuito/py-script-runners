
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

    return table_dict

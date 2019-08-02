import sqlite3
from sqlite3 import Error
 
# Función para la conexión con la base de datos SQLite 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
# Función para la consulta de los registros completos de la tabla "credential". 
def select_all_in_table(conn, table):
    """
    Query all rows in the credential table
    as list of tuples. \n
    :param conn: the Connection object \n
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM { table };")
    return cur.fetchall()
 
# Función para la consulta del registro específico en la tabla "específica" de acuerdo a un nombre específico.
def select_tables_by_row(conn, table, id):
    """
    Query specific table and  name \n
    :param conn: the Connection object. \n
    :param table_db: table in database. \n
    :param name: id of credential. \n
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM { table } WHERE id=?;", (id,))
 
    rows = cur.fetchall()
 
    for row in rows:
        return row
    cur.close
 
 
# def main():
#     database = "C:\\sqlite\db\pythonsqlite.db"
 
#     # create a database connection
#     conn = create_connection(database)
#     with conn:
#         print("1. Query task by priority:")
#         select_task_by_priority(conn,1)
 
#         print("2. Query all tasks")
#         select_all_tasks(conn)
 
 
# if __name__ == '__main__':
#     main()
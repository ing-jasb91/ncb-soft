import sys
sys.path.append('/home/jasb/python/src/ncb-soft/src/logger')

import sqlite3
from sqlite3 import Error as sqliteError

from logger import Logger

logError = Logger('src/logger/.cfg/logging.cfg')
# Redundancia
logError1 = Logger('src/logger/.cfg/error.cfg')

# Función para la conexión con la base de datos SQLite 

class Databases :
    """
    Databases class handle databases sqlite to connection
    CRUD the API ncb soft.
    """
    # def __init__(self, dbfilepath, table = None, colunm = None, record = None) :
    def __init__(self, dbfilepath) :
        """
        Init class
        """
        self.dbfilepath = dbfilepath

    def connectDB(self) :
        """
        connectDB create a database connection to the SQLite database
        specified by the db_file
        :return: Connection object or None if exists an error
        """
        try :
            return sqlite3.connect(self.dbfilepath)
        except sqliteError as OE :
            logError.log_error("Existe un error con la conexión con la base de datos:\n\t", OE)
            logError1.log_error("Existe un error con la conexión con la base de datos:\n\t", OE)
            
        return None

    def cursorDB(self) :
        """
        cursorDB create a cursor for queries in the SQLite database
        in CRUD API\n
        :return: Cursor object or None if exists an error
        """
        try :
            conn = self.connectDB()
            
            return conn.cursor()
            
        except sqliteError as e :
            logError.log_error(f"Existe un error haciendo un cursor con la base de datos:", e)
            logError1.log_error(f"Existe un error haciendo un cursor con la base de datos:", e)
            
        return None

    def executeQuery(self, query) :
        """
        executeQuery make CRUD queries one sentence
        in CRUD API\n
        :param query: A str like "SELECT * FROM table"
        :return: Cursor object or None if exists an error
        """
        cursor = self.cursorDB()

        try :
            cExec = cursor.execute(query)
        except sqliteError as OE :
            logError.log_error('Error en la base de datos:')
            logError.log_error(OE)
            logError1.log_error('Error en la base de datos:')
            logError1.log_error(OE)
            return None
        return cExec

    def executeQueryScript(self, query) :
        """
        executeQueryScript make CRUD queries of a script file\n
        :param query: A str from a file with open function"\n
        :return: Cursor object or None if exists an error\n
        """
        cursor = self.cursorDB()

        try :
            cExec = cursor.executescript(query)
        except sqliteError as OE :
            logError.log_error('Error en la base de datos: No existe la tabla:')
            logError.log_error('\t', OE)
            logError1.log_error('Error en la base de datos: No existe la tabla:')
            logError1.log_error('\t', OE)
            return None
        return cExec

    def createSchemas(self, scriptPath) :
        """
        createSchemas creates a schemas from script file open\n
        :param scriptPath: A str file that set to open function"\n
        :return: Cursor object or None if exists an error\n
        """
        try :
            with open(scriptPath, 'r') as script :
                cSchemas = self.executeQueryScript(script.read())
                cSchemas.close()
                
        except FileNotFoundError as FileError :
            logError.log_error(f"Ocurrió un error leyendo el script:")
            logError.log_error(FileError)
            logError1.log_error(f"Ocurrió un error leyendo el script:")
            logError1.log_error(FileError)


    def simpleQueries(self, table, column = '*', where = None) :
        """
        qCred rows in the credential table
        as list of tuples. \n
        :param table: table name of query \n
        :param column (optionally): column of the table \n
        :param where if the query has a specify record, set where like:\n
            "where = 'username = "transfer"'"
        :return:
        """

        if where is not None :
            query = self.executeQuery(f"SELECT { column } FROM { table } WHERE { where };")
        else :
            query = self.executeQuery(f"SELECT { column } FROM { table };")

        if query is None :
            listRecords = None
        else :
            listRecords = query.fetchall()
            query.close()

        return listRecords


def main():
    ncbQualcom = Databases(
        dbfilepath = 'database/test1.db'
        
        
    )

    ncbQualcom.createSchemas('src/queries/script.sql')

    rows = ncbQualcom.simpleQueries(
        table = 'devices',
        column = 'deviceType, deviceName, hostname, port'
    )

    for row in rows :
        print(row)
    

if __name__ == '__main__':
    main()
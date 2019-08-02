import sqlite3

# Conectar la base de datos
conection = sqlite3.connect("database/system.db")

# Seleccionar el cursor para realizar la consulta
query = conection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS device_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    deviceName TEXT NOT NULL,
    hostname TEXT NOT NULL,
    deviceType int NOT NULL);
"""
sql2="""
CREATE TABLE IF NOT EXISTS credential (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password VARCHAR(255) NOT NULL);
"""
# Ejecutar la consulta
if (query.execute(sql2)):
    print("Create table sussessfully!")
else:
    print("An error has occurred when creating the table!")

# Terminamos la consulta
query.close()

# Guardamos los cambios
conection.commit()

# Cerramos la conexión
conection.close()
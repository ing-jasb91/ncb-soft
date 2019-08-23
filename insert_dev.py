import sqlite3


# Introducción y validación de datos entrantes
print("*** Script para insertar la información de los equipos ***")

name_dev = input("Introduzca el nombre del dispositivo: ")
ip_dev = input("Introduzca la dirección IP del dispositivo: ")
type_dev = input("Introduzca código del dispositivo: ")

try: name_dev = str(name_dev)
except ValueError:
    print(name_dev, "¡Dato inválido!")
    exit()

try: ip_dev = str(ip_dev)
except ValueError:
    print(ip_dev, "¡Dato inválido!")
    exit()

try: type_dev = int(type_dev)
except ValueError:
    print(type_dev, "¡Dato inválido!")
    exit()


# Conectar la base de datos
conection = sqlite3.connect("database/mysqlite.db")

# Seleccionar el cursor para realizar la consulta
c = conection.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='device_data' ''')

if c.fetchone()[0]==0 :

    c.execute(
    """
    CREATE TABLE IF NOT EXISTS device_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    deviceName TEXT NOT NULL,
    hostname TEXT NOT NULL,
    deviceType int NOT NULL);
    """
    )
    print("Tabla <device_data> creada exitosamente!")

# Valor de los argumentos
arguments = (name_dev, ip_dev, type_dev)

sql = """
INSERT INTO device_data(deviceName, hostname, deviceType)
VALUES (?, ?, ?);
"""

# Realizar la consulta
# Ejecutar la consulta
if (c.execute(sql, arguments)):
    print("¡Registros guardados exitosamente!")
else:
    print("¡Ocurrió un error con la inserción de datos!")

# Terminamos la consulta
c.close()

# Guardamos los cambios
conection.commit()

# Cerramos la conexión
conection.close()


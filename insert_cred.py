import sqlite3
from encryptor import passwrd


# Introducción y validación de datos entrantes
print("*** Script para insertar las credenciales de los equipos ***")

username = input("Introduzca el nombre del usuario: ")
password = input("Introduzca la contraseña: ")

try: username = str(username)
except ValueError:
    print(username, "¡Dato inválido!")
    exit()

try: password = str(password)
except ValueError:
    print(password, "¡Dato inválido!")
    exit()

passenc = passwrd(password)

# Conectar la base de datos
conection = sqlite3.connect("database/system.db")

# Seleccionar el cursor para realizar la consulta
c = conection.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='credential' ''')

if c.fetchone()[0]==0 :

    c.execute(
    """
    CREATE TABLE IF NOT EXISTS credential(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password VARCHAR(255) NOT NULL);
    """
    )
    print("Tabla <credential> creada exitosamente!")

# Valor de los argumentos
arguments = (username, passenc)

sql = """
INSERT INTO credential(username, password)
VALUES (?, ?);
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


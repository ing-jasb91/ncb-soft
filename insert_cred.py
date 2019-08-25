import sqlite3
from encryptor import passwrd
import os
import getpass
import write_log
from write_log import log_error, log_warning, log_info, log_debug

db_dir = os.path.abspath(os.getcwd()) + "/database"
print(db_dir)
if not os.path.exists(db_dir):
    os.makedirs(db_dir)
    log_info("Se creó directorio para guardar la base de datos!")


# Introducción y validación de datos entrantes
print("*** Script para insertar las credenciales de los equipos ***")

username = input("Introduzca el nombre del usuario: ")
password = getpass.getpass("Introduzca la contraseña: ")

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
conection = sqlite3.connect(db_dir + "/schema.db")

# Seleccionar el cursor para realizar la consulta
c = conection.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='credential' ''')

if c.fetchone()[0]==0 :
    log_info("Creando esquemas para la tabla <credencial> ... ")

    c.execute(
    """
    CREATE TABLE IF NOT EXISTS credential(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
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
try :
    if (c.execute(sql, arguments)):
        print("¡Registros guardados exitosamente!")
    else:
        print("¡Ocurrió un error con la inserción de datos!")

except sqlite3.IntegrityError :
    print("Inserción de credenciales inválida: los usuarios debe ser únicos en la base de datos!")
    log_warning("Inserción de credenciales inválida: los usuarios debe ser únicos en la base de datos!")

# Terminamos la consulta
c.close()

# Guardamos los cambios
conection.commit()

# Cerramos la conexión
conection.close()


import sqlite3
import re
from encryptor import passwrd
from os import path, getcwd, makedirs
from getpass import getpass
from write_log import log_error, log_warning, log_info, log_debug

# Directorio donde se resguarda la base de datos sqlite
db_dir = getcwd() + "/database"
print(db_dir)

if not path.exists(db_dir):
    makedirs(db_dir)
    log_info(f"Se creó directorio para guardar la base de datos en { db_dir }")

# Introducción y validación de datos entrantes
print("*** Script para insertar las credenciales de los equipos ***")

username = input("Introduzca el nombre del usuario: ")
i = 0
while bool(re.search(r'^\s*[0-9]',username)) or username == "" or bool(re.search(r'^\s+$', username)):
    print('Nombre de usuario', '"' + username + '"', 'no es válido.\nIntente nuevamente')
    username = input("Introduzca nuevamente nombre del usuario: ")
    i += 1
    if i == 2 :
        print("Más de tres intentos seguidos...")
        print("El programa se cerrará!")
        exit()

    
# password = getpass("Introduzca la contraseña: ")
# try: password = str(password)
# except ValueError:
#     print(password, "¡Dato inválido!")
#     exit()
print('''
Recuerde que la contraseña debe tener al menos 8 caracteres,
al menos una mayúscula, una minúscula, y uno de estos signos #?!@$%^&*-
''')
password = getpass("Introduzca la contraseña: ")
# "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
while not bool(re.search(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$" , password)):
    print('La contraseña no es válida.\nIntente nuevamente')
    password = getpass("Introduzca nuevamente la contraseña: ")
    i += 1
    if i == 2 :
        print("Más de tres intentos seguidos...")
        print("El programa se cerrará!")
        exit()


passenc = passwrd(password)

# Conectar la base de datos
connection = sqlite3.connect(db_dir + "/schema.db")

# Seleccionar el cursor para realizar la consulta
c = connection.cursor()

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
connection.commit()

# Cerramos la conexión
connection.close()


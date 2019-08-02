import sqlite3

# Introducción y validación de datos entrantes
print("*** Script para insertar los registros de los dispositivos de red ***")

deviceName = input("Introduzca el nombre del dispositivo: ")
hostname = input("Introduzca la IP o nombre DNS: ")
deviceType = input("Introduzca número del tipo de dispositivo: ")

try: deviceName = str(deviceName)
except ValueError:
    print(deviceName, "¡Dato inválido!")
    exit()

try: hostname = str(hostname)
except ValueError:
    print(hostname, "¡Dato inválido!")
    exit()

try: deviceType = int(deviceType)
except ValueError:
    print(deviceType, "¡Dato inválido!")
    exit()

# Conectar la base de datos
conection = sqlite3.connect("database/system.db")

# Seleccionar el cursor para realizar la consulta
query = conection.cursor()

# Valor de los argumentos
arguments = (deviceName, hostname, deviceType)

sql = """
INSERT INTO device_data(deviceName, hostname, deviceType)
VALUES (?, ?, ?);
"""

# Realizar la consulta
# Ejecutar la consulta
if (query.execute(sql, arguments)):
    print("¡Registros guardados exitosamente!")
else:
    print("¡Ocurrió un error con la inserción de datos!")

# Terminamos la consulta
query.close()

# Guardamos los cambios
conection.commit()

# Cerramos la conexión
conection.close()
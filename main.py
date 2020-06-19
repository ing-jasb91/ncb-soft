################################################ NCB SOFT #########################################################
# LICENSE MIT
# Create by JASB91 [https://github.com/ing-jasb91/ncb-soft]
# Base on James Preston of The Queen's College, Oxford // Website: https://myworldofit.net/?p=9127
# version 0.1.0 alpha 2020/06/13

# Módulos y clases importadas.
# Internos del paquete
from src.queries import Databases
from src.diff import diffBackup
from src.logger import Logger
from src.sftp import GetFiles
from src.devices import TypeDevice

# Externos built-in y de terceros
from datetime import date, timedelta
from time import time
from os import path, makedirs

# Contador de inicio para el cálculo de la duración del script ncb-soft
start_time = time()

# Conectar la base de datos
# Como parametro se puede configurar una ruta distinta a la establecida por defecto
# En el script se utiliza una ruta relativa, pero puede usarse rutas absolutas
connDB = Databases('database/schema.db')

# Configuración para el archivo de logs
logsMain = Logger('src/config/logging.ini') 

# Archivo parse para detectar la configuración de los dispositivos
# Rutas sftp para descargar los archivos
typeDevices = TypeDevice('src/config/devices.ini')

# Variables para definir la fecha del archivo actual
current = date.today().strftime('%Y-%m-%d')

# Credenciales para autenticar con los dispositivos.
# tenemos la conexión con la base de datos, la tabla de la base de datos, el id (default = 1)
credentials = connDB.simpleQueries(
    table = 'credentials',
    column = 'username, password',
    where = 'id = 1'
)

# Puesto que la sentencia anterior devuelve una lista con un único elemento
# Una tupla, se desgloza el elemento 0 para obtener los datos
credentials = credentials[0]

# Datos de los dispositivos
listDevices  = connDB.simpleQueries(
    table = 'devices',
    column = 'deviceName, hostname, port, deviceTypeName',
)

# Bucle "for" para iterar el respaldo de todo los dispositivos en la tabla "devices"
# También se agrega las credenciales, pero debido a que los dispositivos inician sesión con un AAA, tienen la misma contraseña.
for data in listDevices :
    # Localización de los directorios donde se resguardará el respaldo.
    localDirPath = f'./DATA/{ data[0] }'
    # Ruta local de directorio = localDirPath; Ruta local de archivos = localFilePath
    extension = typeDevices.getInfoDevices(data[3], 'extension')
    localFilePath = f'{ localDirPath }/{ current }{ extension }'

    # Condicional if - else comprueba si existe el archivo de respaldo, de lo contrario finaliza la sentencia.
    if path.exists(localFilePath):
        logsMain.log_warning(f"Archivo de respaldo en dispositivo { data[0] } ya existe!")
    else:

        devicesNetworks = GetFiles(
            host = data[1],
            port = int(data[2]),
            device = data[0],
            username = credentials[0],
            password = credentials[1],
        )

        # Define a que directorio remoto del equipo de red a descargar
        # En el archivo devices.ini se definen atributos [] que indica según la marca y el path sftp.
        remoteFilePath = typeDevices.getInfoDevices(data[3], 'path')
        

        # Comprueba si no existe el directorio local
        if not path.exists(localDirPath):
            makedirs(localDirPath)

        # Realiza el backup interno
        devicesNetworks.backupFile(remoteFilePath, localFilePath, retry = 1)

        # Cierra la conexión
        devicesNetworks.close()

        # Comprobación interna para determinar si los archivos anterior y actual son los mismos o no.
        comparableDevices = typeDevices.getInfoDevices(data[3], 'comparable')
        if comparableDevices == 'yes' :
            diffBackup(localDirPath + '/*', '*', data[0])
        elif comparableDevices == 'no' :
            logsMain.log_info(f"El archivo { remoteFilePath } no se puede comparar. Debe estar estar escrito en binario o cifrado.")

# Variable para el cálculo de la duración total de la ejecución del script.

rtime = (time() - start_time)
logsMain.log_info(f"Tiempo de ejecución del script: { round(rtime, 2) } segundos.")



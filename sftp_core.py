from query_def import create_connection, select_all_in_table, select_tables_by_row
from encryptor import enpass
from devices_def import switch
from write_log import wlog
from datetime import datetime
import time
import os
import pysftp

# Contador de inicio para el cálculo de la duración del script pysftp-core
start_time = time.time()

# Conectar la base de datos
db_path = "database/system.db"
conn = create_connection(db_path)

# Variable para la obviar la SSH Fingerping
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  

# Credenciales para autenticar con los dispositivos;  indice de tupla : [0 = id, 1 = username, 2 = password encrypted]
x = select_tables_by_row(conn, "credential", 2)

# Descifrador de password!
pass_clear = enpass(x[2])

# Datos de los dispositivos; indice de tupla : [0 = id, 1 = Hostname, 2 = IP o nombre DNS, 3 = Tipo de Dispositivo]
y = select_all_in_table(conn, "device_data")

# Bucle "for in" para iterar el respaldo de todo los dispositivos habidos en la tabla "device_data"
# También se agrega las credenciales, pero debido a que los dispositivos están contra un AAA, tienen la misma contraseña.
for it in y:
    # Localización de los directorios donde se resguardará el respaldo.
    # Entre corchetes está la variable de acuerdo al dispositivo.
    # Ruta local de directorio = localDirPath; Ruta local de archivos = localFilePath
    localDirPath = f'./DATA/{ it[1] }'
    localFilePath = f'{ localDirPath }/{ datetime.now().strftime("%Y-%m-%d") }.txt'
    # Condicional if - else comprueba si existe el archivo de respaldo, de lo contrario finaliza la sentencia.
    if os.path.exists(localFilePath):
        # Variable wlog() escribe lo indicado en un archivo log
        wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Archivo de respaldo { it[1] } ya existe!")
    else:
        # Sentencias "try except else" manejan errores si se llegacen a presentar
        try:
            sftp = pysftp.Connection(host=it[2], username=x[1], password=pass_clear, cnopts=cnopts)
        except KeyboardInterrupt:
            wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Script detenido inesperadamente por el usuario")
            wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Tiempo de ejecución del script: { round( (time.time() - start_time), 2) } segundos.")
            quit()
        except:
            wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   No es posible la conexión con { it[1] }: ¡tiempo agotado!")
        else:
            wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Intentando conectar { it[1] } ... ")

            # Define a que directorio remoto del equipo de red debes elegir para descargar
            # En el archivo devices_def.py se definen un diccionario que indica el tipo y el path.
            remoteFilePath = switch(it[3])

        # Define the local path where the file will be saved
        # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"

            # Comprueba si no existe el directorio local, si existe omite la línea que sigue
            if not os.path.exists(localDirPath):
                os.makedirs(localDirPath)
            # Captura el error en caso de ocurrir alguno, y escribe los mensajes en el log.
            try:
                sftp.get(remoteFilePath, localFilePath)
                wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Respaldo del archivo conf en el dispositivo { it[1] } realizado exitosamente!")
            except:
                wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Error en la conexión con el dispositivo { it[1] }. ¿Está habilitado SFTP en este equipo?")
            sftp.close()


# Variable para el cálculo de la duración total de la ejecución del script.
# El resultado es almacenado en el log.
rtime = (time.time() - start_time)
wlog(f"{ datetime.now().strftime('%Y-%m-%d %H-%M-%S') }   Tiempo de ejecución del script: { round(rtime, 2) } segundos.")

# # connection closed automatically at the end of the with-block


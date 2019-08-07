import logging
from os import path, makedirs


# Comprueba si la carpeta 'logs' existe, si no es así, la crea.
logPath = './logs'
if not path.exists(logPath):
       makedirs(logPath)

# Módulo para configurar las opciones del logging.
# Por el momento se le configuró marca de tiempo, nivel de severidad, mensaje y almacenamiento en el archivo 'main_log.txt'
logging.basicConfig(format=u'%(asctime)-2s — %(levelname)-10s %(message)-2s',
                     datefmt='%Y-%m-%d %H:%M:%S', 
                     level=logging.INFO,
                     handlers=[logging.FileHandler(f'{ logPath }/main_log.txt', 'a', 'utf-8')])

# 

# Definición de niveles de severidad [Error, Warning, Info y Debug]
# Leer la documentación 'https://docs.python.org/3/library/logging.html#logging-levels' para conocer otros niveles.
def log_error(mensaje):
       #logging.error(mensaje)
       logging.exception(mensaje)

def log_warning(mensaje):
       logging.warning(mensaje)

def log_info(mensaje):
       logging.info(mensaje)

def log_debug(mensaje):
       logging.debug(mensaje)

    

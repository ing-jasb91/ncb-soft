import logging
from os import path, makedirs

logPath = './logs'

if not path.exists(logPath):
       makedirs(logPath)


logging.basicConfig(format='%(asctime)-2s — %(levelname)-10s %(message)-2s',
                     datefmt='%Y-%m-%d %H:%M:%S', 
                     level=logging.INFO, filename=f'{ logPath }/main_log.txt')

# 

# logging.Formatter("[%(levelname)8s] - %(message)2s)")

def log_error(mensaje):
       #logging.error(mensaje)
       logging.exception(mensaje)

def log_warning(mensaje):
       logging.warning(mensaje)

def log_info(mensaje):
       logging.info(mensaje)

def log_debug(mensaje):
       logging.debug(mensaje)
    

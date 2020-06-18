import glob
from filecmp import cmp, clear_cache
from os import path, remove
from .logger import Logger

logs = Logger('src/config/logging.ini')

def diffBackup(directory, devices, dirDevice):
    """
    diff_file is a function to check difference between two files\n
    of a directory of config backup network devices.\n
    Compare the previous file with the current file, regardless of the date. \n

    :param previous: File before to current backup \n
    :param last: File current backup \n

    """

    # Obtiene las rutas relativas de los archivos de un directorio especificado
    listFiles = glob.glob(directory)

    if len(listFiles) == 0 or len(listFiles) == 1 :
        return logs.log_warning(f'No se puede comparar una directorio con { len(listFiles) } archivo/s.')

    # Ordena por marca de tiempo de los archivos en forma descendente (Del mayor al menor).
    listFiles.sort(key=path.getctime, reverse=True)

    lastFile = listFiles[0]
    previousFile = listFiles[1]

    if cmp(previousFile, lastFile) :
        logs.log_info(f"Los archivos respaldados en { dirDevice } son idénticos!")
        remove(lastFile)
        logs.log_info(f'No es necesario el respaldo actual del archivo de configuración en { dirDevice }.')

    else:
        logs.log_warning(f"Los archivos respaldados en { dirDevice } son distintos!")
        logs.log_info(f'Se realizó el respaldo del archivo de configuración en { dirDevice }.')
    
    # Limpia el cache filecmp
    clear_cache()
    

def main() :

    diffBackup("./DATA/*", "ExampleN.txt", "SW-RRHH")

if __name__ == '__main__' :
    main()
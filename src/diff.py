import glob
from filecmp import cmp, clear_cache
from os import path
import logger

logs = logger.Logger('src/config/logging.ini')

def diffBackup(directory, devices):
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

    print(lastFile, previousFile)
    if cmp(previousFile, lastFile) :
        # return log_debug(f"Los archivos respaldados en { devices } son idénticos!")
        return logs.log_info(f"Los archivos respaldados en { devices } son idénticos!")
    
    else:
        # return log_warning(f"Los archivos respaldados en { devices } son distintos!")
        return logs.log_warning(f"Los archivos respaldados en { devices } son distintos!")
    
    # Limpia el cache filecmp
    clear_cache()
    

def main() :

    diffBackup("./DATA/*", "ExampleN.txt")
    # listFiles = glob.glob('./DATA/*')

    # print(listFiles)


if __name__ == '__main__' :
    main()
from filecmp import cmp, clear_cache
from os import path
from write_log import log_warning, log_info, log_debug


def diffBackup(yesterday, today, devices):
    """
    diff_file is a function to check difference between two files \n
    of config backup network devices. \n
    :param yesterday: File before to current backup \n
    :param today: File current backup \n

    """
    if(path.exists(yesterday) and path.exists(today) != True):
        return log_warning(f"Existe un problema (el actual y/o el anterior) con el archivo de respaldo en { devices }")
    elif(cmp(yesterday, today) == True):
        return log_debug(f"Los archivos respaldados en { devices } son idénticos!")
    else:
        return log_warning(f"Los archivos respaldados en { devices } son distintos!")
    clear_cache()
    
        



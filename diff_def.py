from filecmp import cmp, clear_cache
from datetime import datetime, date, timedelta
from os import path
#from write_log import wlog


today = date.today()
yesterday = today - timedelta(days=1)


def diff_file(yest, tod, devices):
    """
    diff_file is a function to check difference between two files \n
    of config backup network devices. \n
    :param yest: File before backup \n
    :param tod: File current backup \n

    """
    if(path.exists(yest) and path.exists(tod) != True):
        return f"{ datetime.now().strftime('%Y-%m-%d %H:%M:%S') }   En { devices } Existe un problema con el archivo de hoy y/o el archivo de ayer"
    elif(cmp(yest, tod) == True):
        return f"{ datetime.now().strftime('%Y-%m-%d %H:%M:%S') }   Los archivos respaldados en { devices } son idénticos!"
    else:
        return f"{ datetime.now().strftime('%Y-%m-%d %H:%M:%S') }   Los archivos respaldados en { devices } son distintos!"
            

        
        


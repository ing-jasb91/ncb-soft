from paramiko import Transport, SFTPClient
from paramiko import ssh_exception
import time
import errno

from .logger import Logger

## Based in this model:
## https://medium.com/@thapa.parmeshwor/sftp-upload-and-download-using-python-paramiko-a594e81cbcd8

logsMain = Logger('src/config/logging.ini')

class GetFiles :
    _connection = None

    def __init__(self, host, port, device, username, password) :
        self.host = host
        self.port = port
        self.device = device
        self.username = username
        self.password = password

        try :
            self.create_connection(
                self.host, self.port,
                self.username, self.password
                )

        except ssh_exception.AuthenticationException as e :
            logsMain.log_error(f"Autenticación fallida en { self.device }: Más detalles: { e }")
        except:
            logsMain.log_error(f"No es posible la conexión con { self.device }. Más detalles:")
        else:
            logsMain.log_info(f"Intentando conectar con { self.device } ... ")

        
    @classmethod
    def create_connection(cls, host, port, username, password) :
        transport = Transport(sock = (host, port))
        transport.connect(username = username, password = password)
        cls._connection = SFTPClient.from_transport(transport)

    def fileExists(self, remotePath) :
        try :
            if self._connection == None :
                return False
            self._connection.stat(remotePath)
            logsMain.log_info(f'Recuperando respaldo de la ruta { remotePath }')
        except IOError as e :
            if e.errno == errno.ENOENT :
                return False
            raise
        else :
            return True

    def backupFile(self, remotePath, localPath, retry = 3) :
        
        if self.fileExists(remotePath) or retry == 0 :
            try :
                self._connection.get(remotePath, localPath, callback=None)
                return logsMain.log_info(f"Respaldo del archivo conf en el dispositivo { self.device } realizado exitosamente!")
            except:
                return logsMain.log_error(f"Error en la conexión con el dispositivo { self.device }. ¿Está habilitado SFTP en este equipo?")
            
        elif retry > 0 :
            time.sleep(1)
            retry -= 1
            self.backupFile(remotePath, localPath, retry = retry)

    def close(self) :
        if self._connection != None :
            self._connection.close()
        else :
            logsMain.log_warning(f"Cierre de conexión sin efecto!")

def main() :
    switchRRHH = GetFiles('10.0.12.10', 22, 'SW-RRHH', 'anthony', 'Qualc0m3')

    switchRRHH.backupFile('/cfg/startup-config', './DATA/example4.txt')

    switchRRHH.close()
    
    
if __name__ == '__main__' :
    main()
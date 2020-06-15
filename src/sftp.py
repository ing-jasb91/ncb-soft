from paramiko import Transport, SFTPClient
import time
import errno

## Based in this model:
## https://medium.com/@thapa.parmeshwor/sftp-upload-and-download-using-python-paramiko-a594e81cbcd8


class getFileSftp :
    _connection = None

    def __init__(self, host, port, username, password) :
        self.host = host
        self.port = port
        self.username = username
        self.password = password


        self.create_connection(
            self.host, self.port,
            self.username, self.password
            )
        
    @classmethod
    def create_connection(cls, host, port, username, password) :
        transport = Transport(sock = (host, port))
        transport.connect(username = username, password = password)
        cls._connection = SFTPClient.from_transport(transport)



    def fileExists(self, remotePath) :
        try :
            print('Remote Path:', remotePath)
            self._connection.stat(remotePath)
        except IOError as e :
            if e.errno == errno.ENOENT :
                return False
            raise
        else :
            return True
                
            

    def backupFile(self, remotePath, localPath, retry = 5) :
        if self.fileExists(remotePath) or retry == 0 :
            self._connection.get(remotePath, localPath, callback=None)

        elif retry > 0 :
            time.sleep(5)
            retry -= 1
            self.backupFile(remotePath, localPath, retry = retry)
            

    def close(self) :
        self._connection.close()

def main() :
    switchRRHH = getFileSftp('10.0.12.10', 22, 'anthony', 'Qualc0m3')

    switchRRHH.backupFile('/cfg/startup-config', './DATA/example4.txt')

    switchRRHH.close()
    
    
if __name__ == '__main__' :
    main()
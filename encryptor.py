## Resources: https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/
from cryptography import fernet

#Clave simétrica de cifrado y descifrado
# Tener la clave en el código lo hace inseguro
# Asegurese de que los permisos de lectura, escritura sean de un usuario confiables
key = b'KWbqrTvdTAmfEcgB8t5NUntZFibIetEF41H0jKb5IiU='

cipher_suite = fernet.Fernet(key)

# Variable para cifrar
def passwrd(clearPass='Password'):
    return cipher_suite.encrypt(bytes(clearPass, encoding = "utf-8"))

# Variable para descifrar
def enpass(cryptoPass):
    return cipher_suite.decrypt(cryptoPass).decode("utf-8")



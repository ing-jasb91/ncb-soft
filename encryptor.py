## Resources: https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/
from cryptography.fernet import Fernet

#Clave de cifrado y descifrado
key = b'KWbqrTvdTAmfEcgB8t5NUntZFibIetEF41H0jKb5IiU='
cipher_suite = Fernet(key)

# Variable para cifrar
def passwrd(x='Password'):
    return cipher_suite.encrypt(bytes(x, encoding = "utf-8"))

# Variable para descifrar
def enpass(z):
    return cipher_suite.decrypt(z).decode("utf-8")



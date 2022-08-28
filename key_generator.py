import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


passfu = input("Enter Your Password:- ")
password = passfu.encode()

mysalt = b'\xb4\xef\xcf\xcb\xb7\x0eY\xb8D\x10\xec\x9d\xcd\xdc\n\xf9\x16\x96\xd2P\xd5\xb1\x11\x84C\x8e\xdf\xb3O\xeaZ\x88'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512,
    length=32,
    salt=mysalt,
    iterations=10000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)


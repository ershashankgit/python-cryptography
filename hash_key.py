import hashlib
import base64
messg = input("Enter Your message:- ")
enc_messg = hashlib.sha512(messg.encode()).digest()
print(base64.b64encode(enc_messg))


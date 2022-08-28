import sys
from cryptography.fernet import Fernet


key ="l8U1Znglx5S8Hcg1OnrLN2xBq8zfg99eOlb46Aiftxo="

fer= Fernet(key)

user_file= input("Enter your filename:- ")
  
with open(user_file , 'rb') as ef:
    data = ef.read()

selec_ch = input("Do you want to encrypt or decrypt (e/d)? ")

if selec_ch == "e" :
    edata = fer.encrypt(data)
    with open(user_file , 'wb' ) as ef:
        ef.write(edata)
        print("Encrypted Successfully!!")
    
elif selec_ch == "d":
    ddata = fer.decrypt(data)
    with open(user_file , 'wb') as df:
        df.write(ddata)
        print("Decrypted Successfully")
        
else:
    sys.exit("Wrong Choice!!")


   

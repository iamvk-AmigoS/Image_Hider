import base64
with open("3.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)
import pyDes
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(str)
print ("Encrypted: %r" % d)
print ("***************************************************************")
print ("Decrypted: %r" % k.decrypt(d))

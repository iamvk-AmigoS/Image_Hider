import base64
with open("bunny1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
import pyDes
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(str)
print (d)


import base64
import binascii
import optparse
import pyDes
from PIL import Image

with open("3.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)

k = pyDes.des(b"DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
encrypted = k.encrypt(str)
print ("Encrypted: " + repr(encrypted))

def encode(hexcode, digit):
	if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
		hexcode = hexcode[:-1]+digit
		return hexcode
	else:
		return None

def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]
		
def rgb2hex(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
	hexcode = hexcode.lstrip('#')
	hlen = len(hexcode)
	return tuple(int(hexcode[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))
	
def hide(filename, message):
	img = Image.open(filename)
	binary = str2bin(message) + '1111111111111110'
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()
		
		newData = []
		digit = 0
		temp = ''
		for item in datas:
			if(digit < len(binary)):
				newpix = encode(rgb2hex(item[0], item[1], item[2]), binary[digit])
				if newpix == None:
					newData.append(item)
				else:	
					r, g, b = hex2rgb(newpix)
					newData.append((r, g, b, 255))
					digit += 1
			else:
				newData.append(item)
		img.putdata(newData)
		img.save(filename, "PNG")
		return "Completed!"
	return "Incorrect Image mode, couldn't hide"
	
def Main():
	parser = optparse.OptionParser('usage %prog '+\
		'-e/-d <target file>')
	parser.add_option('-e', dest='hide', type='string', \
		help='target picture path to hide text')
			
	(options, args) = parser.parse_args()
	if (options.hide != None):
		text = encrypted
		print (hide(options.hide, text))
	else:
		print (parser.usage)
		exit(0)
		
if __name__ == '__main__':
	Main()


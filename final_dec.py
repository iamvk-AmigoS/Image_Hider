import base64
import binascii
import optparse
import pyDes
from PIL import Image

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

def rgb2hex(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)
	
def bin2str(binary):
	message = binascii.unhexlify('%x' % (int('0b' +binary, 2)))
	return message
	
def retr(filename):
	img = Image.open(filename)
	binary = ''
	
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas =img.getdata()
		
		for item in datas:
			digit = decode(rgb2hex(item[0], item[1], item[2]))
			if digit ==None:
				pass
			else:
				binary = binary + digit
				if (binary[-16:] == '1111111111111110'):
					print ("Success")
					return bin2str(binary[:-16])
		return bin2str(binary)
	return "Incorrect Image mode, couldn't retrieve"
	
def Main():
	parser = optparse.OptionParser('usage %prog '+\
		'-e/-d <target file>')
	parser.add_option('-d', dest='retr', type='string', \
		help='target picture path to retrieve text')
			
	(options, args) = parser.parse_args()
	if (options.retr != None):
		print (retr(options.retr))
		de = retr(options.retr)
		print("*****************************************************")
		print(de)
		print("*****************************************************")
		de=de[2:-1]
		k = pyDes.des(b"DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
		decrypted = k.decrypt(de)
		print ("Decrypted: %r" % decrypted)
	else:
		print (parser.usage)
		exit(0)
		
if __name__ == '__main__':
	Main()

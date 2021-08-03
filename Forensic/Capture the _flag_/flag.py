from PIL import Image
from numpy import asarray

img = Image.open('flag.png')

numpydata = asarray(img)

flatarray =  []
for i in range(0,120):
	for j in range(0,120):
		flatarray.append(list(numpydata[j][i]))

flatarray = flatarray[1337:1500]

pixels = []
for pixel in flatarray:
	del pixel[3]
	pixels += pixel

def lsb(val):
	if val%2 == 0:
		return "0"
	else:
		return "1"


flagstr = ""
for i in range(0 , len(pixels) , 8):
	part = pixels[i:i+8]
	char = ""
	for pixel in part:
		char += lsb(pixel)
	flagstr += chr(int(char , 2))

print(flagstr)


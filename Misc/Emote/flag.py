from PIL import Image
from numpy import asarray

img = Image.open('emote.png')

numpydata = asarray(img)

imgstring = ""

def process(rowlist):
	value= ""
	for pixel in rowlist:
		if pixel == True:
			value += "1"
		else:
			value += "0"
	value = chr(int(value , 2))
	return value

for row in numpydata:
	imgstring += str(process(row[:8]))
	imgstring += str(process(row[8:]))

print(imgstring)
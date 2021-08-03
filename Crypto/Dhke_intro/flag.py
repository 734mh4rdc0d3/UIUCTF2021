import random
from Crypto.Cipher import AES
import itertools

ciphertext = bytes.fromhex("b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6")

gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]

pmax = max([x[1] for x in gpList]) #31

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')

for g, p in gpList:
	for a,b in itertools.product(list(range(1, p+1)) , list(range(1, p+1)) ):
		k = pow(g, a * b, p)
		k = str(k)

		key = ""
		i = 0
		padding = "uiuctf2021uiuctf2021"
		while (16 - len(key) != len(k)):
		    key = key + padding[i]
		    i += 1
		key = key + k
		key = bytes(key, encoding='ascii')

		cipher = AES.new(key, AES.MODE_CFB, iv)

		text = cipher.decrypt(ciphertext)
		text = str(text)
		if ("uiuctf" in text):
			print(text)
			break
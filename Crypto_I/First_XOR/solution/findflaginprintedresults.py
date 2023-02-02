import os
import random

def main():

	with open("message.txt", "r") as m:
		ciphertext = m.read()
		a = []
		for i in range(int(len(ciphertext)/2)):
			a.append(int(ciphertext[2*i:2*i+2], 16))		
	
		for i in range(255):
			s = ""
			for j in range(len(a)):
				s += chr(a[j] ^ i)			
			print(s)	

if __name__ == '__main__':
    main()

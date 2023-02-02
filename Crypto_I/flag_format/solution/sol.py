def main():
	with open("message.txt", "r") as m:
		ciphertext = m.read()
		a = []
		for i in range(int(len(ciphertext)/2)):
			a.append(int(ciphertext[2*i:2*i+2], 16))

		for i1 in range(256):	
			if (i1 ^ a[0]) <> ord("s"): 
				continue
			for i2 in range(256):
				if (i2 ^ a[1]) <> ord("i"):
					continue
				for i3 in range(256):
					if (i3 ^ a[2]) <> ord("g"):
						continue
					for i4 in range(256):
						if (i4 ^ a[3]) <> ord("p"):
							continue
						for i5 in range(256):
							if (i5 ^ a[4]) <> ord("w"):
								continue
							for i6 in range(256):
								if (i6 ^ a[5]) <> ord("n"):
									continue
								for i7 in range(256):
									if (i7 ^ a[6]) <> ord("y"):
										continue
									for i8 in range(256):
										if (i8 ^ a[7]) <> ord("{"):
											continue
										b = [i1, i2, i3, i4, i5, i6, i7, i8]
										s = ""
										for j in range(len(a)):	
											s += chr(a[j] ^ b[j % 8])
										print(s)
										return
if __name__ == '__main__':
    main()

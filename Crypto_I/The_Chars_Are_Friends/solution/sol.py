cipher_arr = [51, 105, 231, 176, 55, 46, 185, 187, 50, 225, 174, 228, 111, 237, 223, 105, 51, 174, 180, 95, 33, 181, 52, 239, 45, 97, 52, 41, 163, 97, 172, 236, 249, 31, 51, 37, 163, 181, 242, 229, 253]

for i in range(len(cipher_arr)):
	a = []
	a.append(chr(cipher_arr[i] ^ 0xc0))
	a.append(chr(cipher_arr[i] ^ 0x80))
	a.append(chr(cipher_arr[i] ^ 0x40))
	a.append(chr(cipher_arr[i] ^ 0x00))
	print(a)

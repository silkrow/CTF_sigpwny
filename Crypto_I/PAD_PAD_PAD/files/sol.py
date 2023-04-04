def sxor(s1, s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

with open("message.txt", "r") as f:
	messages = f.read()

messages = messages.replace("'", " ")
messages = messages.replace("[", " ")
messages = messages.replace("]", " ")
messages = messages.replace(",", " ")

messages = messages.split()

for i in range(len(messages)):
	hex_str = messages[i]
	ascii_str = "".join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])
	messages[i] = ascii_str

guess = ", "

min = 1024
for i in range(len(messages)):
	if len(messages[i]) < min:
		min = len(messages[i])

for i in range(len(messages)):
	print("----------------------------------------------")
	print("cipher string #" + str(i))
	for j in range(min - len(guess) + 1):
		pool = []
		flag = True
		for k in range(len(messages)):
			test = sxor(messages[k][j*2:], guess)
			pool.append(test)
			for l in range(len(test)):
				if (ord(test[l]) < ord('!') or ord(test[l]) > ord('~')):
					flag = False
					break
		if flag:
			print("get at position " + str(j))
			for l in range(len(pool)):
					print(pool[l])

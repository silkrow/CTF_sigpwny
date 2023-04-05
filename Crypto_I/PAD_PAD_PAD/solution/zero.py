def sxor(s1, s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

with open("../files/message.txt", "r") as f:
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

characters = [i for i in range(ord('!'), ord('~')+1)]
characters.append(ord(' '))
guess = "Crib dragging is a known"

i = 0
print("----------------------------------------------")
print("cipher string #" + str(i))
j = 0
pool = []
flag = True
for k in range(len(messages)):
	if j >= min(len(messages[k]), len(messages[i])) - len(guess) + 1:
		continue
	test = sxor(sxor(messages[k][j:], messages[i][j:]), guess)
	assert len(test) == len(guess), "Unmatching length!"
	pool.append((test, k))
	for l in range(len(test)):
		if ord(test[l]) not in characters:
			flag = False
			break
if flag and len(pool) != 0:
	print("get at position " + str(j))
	for l in range(len(pool)):
		print(pool[l])

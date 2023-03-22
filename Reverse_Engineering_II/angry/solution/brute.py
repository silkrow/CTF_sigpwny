import gdb

char_range = ord('~') - ord('!') + 1
# information obtained with Ghidra
for_success = 0x00405465
for_update = 0x00405468
fail = 0x0040544f
flag_len = 31 
# global variables
known_flag = ''
known_len = 0
unknown_len = flag_len - known_len

# Iteration on each character in the flag
for i in range(flag_len):
	# Iteration to find next character
	for j in range(char_range):
		# skip special characters, I bet ' is not in the flag, lol
		if (ord('!')+j == ord("'")):
			continue

		# load the executable
		gdb.execute("file ../files/angry", False, True)

		# set argument
		input = known_flag+chr(ord('!')+j)+(unknown_len-1)*"0"
		gdb.execute("set args '{}'".format(input), False, True)

		# print known flag and input, so that we can see it in the end	
		print(known_flag)
		print(input)

		# set breakpoint and run
		gdb.execute("b *{}".format(fail), False, True)
		gdb.execute("r", False, True)

		# examine eax
		s = gdb.execute("p $eax", False, True)
		
		# parsing
		num = s.split("=")
		s = num[1].split()
		eax = int(s[0], 0)

		if (eax > known_len):
			known_len += 1
			unknown_len -= 1
			known_flag += chr(ord('!')+j)
			gdb.execute("c", False, True)
			break
		print(eax)
		gdb.execute("c", False, True)



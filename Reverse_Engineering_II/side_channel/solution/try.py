import gdb

char_range = ord('~') - ord('!') + 1

obj_z_start = 0x001011a9     
offset = 0x555555454000  

z_start = obj_z_start + offset

for j in range(40):
	# load the executable
	gdb.execute("file ../files/side_channel", False, True)

	# set breakpoint and run
	gdb.execute("b putchar", False, True)
	gdb.execute("r", False, True)

	for i in range(51):
		s = gdb.execute("c", False, True)

	gdb.execute("d breakpoints", False, True)
	gdb.execute("b *{}".format(z_start), False, True)

	gdb.execute("c", False, True)
	s = gdb.execute("p $rip", False, True)

	ctr = 0
	while s.split()[-2] == hex(z_start) and ctr < 100000:
		gdb.execute("c", False, True)
		try:
			s = gdb.execute("p $rip", False, True)
			ctr = ctr + 1
		except:
			break

	with open("temp.txt", "a") as f:
		f.write(str(j+1) + " " + str(ctr) + "\n")

	gdb.execute("d breakpoints", False, True)

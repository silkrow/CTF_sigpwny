import gdb
import sys

char_range = ord('~') - ord('!') + 1

obj_z_start = 0x001011a9     
offset = 0x555555454000  

z_start = obj_z_start + offset

flag_len = 31 

# load the executable
gdb.execute("file ../files/side_channel", False, True)

# set breakpoint and run
gdb.execute("b putchar", False, True)
gdb.execute("r", False, True)

for i in range(51):
	s = gdb.execute("c", False, True)

sys.stdout.write("dabian")

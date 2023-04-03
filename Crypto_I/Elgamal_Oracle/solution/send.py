import socket
from struct import pack
from Crypto.Util.number import inverse

# Define the host and port of the server you want to connect to
HOST = 'chal.sigpwny.com'
PORT = 1986

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
    
	# Receive feedback from the server
	data = s.recv(2048)
	feedback = data.decode()
	print("Feedback from server: ", feedback)

	# Extract p, A, B
	feedback = feedback.split('=')			

	p = feedback[1].split()[0]
	p = int(p[2:],16)
	A = feedback[2].split()[0]
	A = int(A[2:], 16)
	B = feedback[3].split()[0]
	B = int(B[2:], 16)


	c1 = hex(B)[2:]
	payload = c1.encode()
	s.sendall(payload)

	ret = "\n"
	s.sendall(ret.encode())

	# Receive feedback from the server
	data = s.recv(2048)
	feedback = data.decode()
	print("Feedback from server: ", feedback)

	c2 = hex(B)[2:]
	payload = c2.encode()
	s.sendall(payload)
	
	ret = "\n"
	s.sendall(ret.encode())

	# Receive feedback from the server
	data = s.recv(2048)
	feedback = data.decode()
	print("Feedback from server: ", feedback)

	value = feedback.split('0x')[1].split()[0]
	value = int(value, 16)
	
	a = inverse(value, p)
	a = a*B %p

	shared = a
	shared = hex(shared)[2:]
	payload = shared.encode()
	s.sendall(payload)

	ret = "\n"
	s.sendall(ret.encode())

	# Receive feedback from the server
	data = s.recv(2048)
	feedback = data.decode()
	print("Feedback from server: ", feedback)



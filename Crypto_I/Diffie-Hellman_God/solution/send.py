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

	# Extract p and g, at the same time handle the first pair of b and A
	feedback = feedback.split('=')	

	g = int(feedback[1][:-2].split()[0])
	print(g)
	p = int(feedback[2][:-2].split()[0])
	print(p)
	b = int(feedback[3][:-2].split()[0])
	print(b)
	A = int(feedback[4][:-2].split()[0])
	print(A)

	# Calculate the secret
	shared = pow(A, b, p)

	payload = str(shared).encode()

	# Send the output to the server
	s.sendall(payload)
	
	ret = "\n"

	s.sendall(ret.encode())

	# Do the rest 999 times of decryption
	for i in range(999):
		# Receive feedback from the server
		data = s.recv(2048)
		feedback = data.decode()
		print("Feedback from server: ", feedback)

		# Extract p and g, at the same time handle the first pair of b and A
		feedback = feedback.split('=')	

		b = int(feedback[1][:-2].split()[0])
		print(b)
		A = int(feedback[2][:-2].split()[0])
		print(A)

		# Calculate the secret
		shared = pow(A, b, p)

		payload = str(shared).encode()

		# Send the output to the server
		s.sendall(payload)
	
		ret = "\n"

		s.sendall(ret.encode())

	# Grab the flag

	# Receive feedback from the server
	data = s.recv(2048)
	feedback = data.decode()
	print("Feedback from server: ", feedback)



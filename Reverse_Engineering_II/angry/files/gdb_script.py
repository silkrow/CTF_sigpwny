import subprocess

cmd = ["gdb", "--args", "angry", "1234567890123456789012345678901"]

breakpt = "0x0040544f"

num_runs = 1

for i in range(num_runs):
	gdb_process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	#gdb_process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
	
	#gdb_process.stdin.write(("break *{}\n".format(breakpt)).encode())

	#gdb_process.stdin.write(b"run\n")
	
	print(gdb_process.stdout.read().decode())

	#gdb_process.stdin.write(b"quit\n")

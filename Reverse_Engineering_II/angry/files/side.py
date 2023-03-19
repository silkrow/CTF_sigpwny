import subprocess
import time

# Function to measure execution time of the comparison operation
def measure_time(input_string):
    start_time = time.time()
    result = subprocess.call(["./angry", input_string])
    end_time = time.time()
    return end_time - start_time

# Main loop to perform side-channel attack
flag_length = 31
flag = []
for i in range(flag_length):
	flag.append('0')

max_time = 0
for i in range(flag_length):

	max_time = 0
	max_num = 0

	for j in range(ord('~') - ord('!') + 1):
		flag[i] = chr(ord('!') + j)
		flag_str = "".join(flag)
		test_time = measure_time(flag_str)
		if (test_time > max_time):
			max_time = test_time
			max_num = j
	flag[i] = chr(ord('!') + max_num)

print("".join(flag))



with open("../files/eve.txt", "r") as f:
	feedback = f.read()	
	feedback = feedback + "aa"

	feedback = feedback.split('=')

	g = int(feedback[1][:-2].split()[0])
	p = int(feedback[2][:-2].split()[0])
	A = int(feedback[3][:-2].split()[0])
	B = int(feedback[4][:-2].split()[0])

	for i in range(2, 100000):
		if A == (g**i) % p:
			print((B**i)%p)
			break
	

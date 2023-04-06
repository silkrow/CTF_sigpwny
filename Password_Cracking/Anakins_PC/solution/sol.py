from hashlib import md5

h = md5()
s = ['Hackerman123','idocryptoforfun','iamamathmajor,','ihavelonghair','ilikegreenkitkat','ihatediffeq']

for str in s:
	h.update(str.encode())
	if h.hexdigest() == "24426f6211bd68ce7647ebfd7f694b42":
		print(str)
	h = md5()

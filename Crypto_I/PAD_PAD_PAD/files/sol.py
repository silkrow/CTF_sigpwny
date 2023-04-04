with open("message.txt", "r") as f:
	messages = f.read()

messages = messages.replace("'", " ")
messages = messages.replace("[", " ")
messages = messages.replace("]", " ")
messages = messages.replace(",", " ")

messages = messages.split()


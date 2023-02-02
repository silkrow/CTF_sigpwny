def vigenereEncrypt(plaintext, key):
  ciphertext = ""
  for i in range(len(plaintext)):
    ciphertext += chr((ord(plaintext[i]) + ord(key[i % len(key)]) - 2 * ord("a")) % 26 + ord("a"))
  return ciphertext

#TODO: write the decryption function to reverse the above function
def vigenereDecrypt(ciphertext, key):
  plaintext = ""
  for i in range(len(ciphertext)):
    #Fix the below
    plaintext += chr((ord(ciphertext[i]) - ord(key[i % len(key)])) % 26 + ord("a"))
  return plaintext

with open("ciphertext", "r") as c, open("key", "r") as k:
  ciphertext = c.read()
  key = k.read()

  # Cut out the ending byte which is not in the valid alphabet.
  ciphertext = ciphertext[:-1]
  key = key[:-1]

  #TODO: figure out how to decode the ciphertext
  #hint: what are those function names?
  #https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
  #What's the difference between this and the Caesar cipher?

  plaintext = vigenereDecrypt(ciphertext, key)
  print(plaintext)

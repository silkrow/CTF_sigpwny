import os
import random

def encrypt(ciphertext, key):
    return bytes([b ^ key for b in ciphertext])

# The output of this function has been written to message.txt
def main():
    random_byte = random.randint(0, 255)
    flag = "sigpwny{not_the_real_flag}"
    print(encrypt(bytes(flag.encode()), random_byte).hex())

if __name__ == '__main__':
    main()

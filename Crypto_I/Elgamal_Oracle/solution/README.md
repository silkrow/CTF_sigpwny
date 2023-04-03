1. To get the flag, run the python script.

```python3 send.py```

2. The key of solving this problem is to understand ```alice_elgamal_decrypt(g, p, a)``` function in the provided python code. Apparently, the server will provide ```A, B, p``` each time, and ```g = 2``` is fixed. The ```alice_elgamal_decrypt(g, p, a)``` function asks for user input ```c1, c2```, and compute ```pow(pow(c1,a,p), -1, p)*c2 % p```. The goal is to get ```A^b mod p``` or ```B^a mod p```, since ```c1^a mod p``` appears in the ```pow(pow(c1,a,p), -1, p)*c2 % p``` expression, just let ```c1 = B``` will get ```B^a mod p``` inside the expression. Then let ```c2 = B``` as well, so eventually ```pow(pow(c1,a,p), -1, p)*c2 % p``` will give ```B^(1-a) mod p```, which is close enough with ```B^a mod p```.
3. After receiving ```B^(1-a) mod p```, find its inverse, then times B will get the value of shared secret.

1. Give execution permission to ```encryption``` with following command.

```chmod +x encryption```

2. Create a new project in Ghidra and analyze ```encryption``` by default settings.
3. The first while loop in ```main``` is to find the "length" of the hardcoded flag, however I didn't find this to be useful in later codes.
4. The for loop that writes some memory with itself is clearly useless.
5. Infact, there're many weird operations in ```main``` that are just useless (at least I don't know what they do).
6. The useful information to spot is that a input string is read with ```fgets```, passed to ```do_encryption``` and compare with the hardcoded flag.
7. Read ```do_encryption``` function, it's not difficult to find out that it just shift the ascii of input string down by 1. 
8. So, use a simple python code to shift the hardcoded flag up by 1 would give the answer.

```python3 answer.py```

1. Give ```irreversible``` permission to execute with the following command.

```chmod +x irreversible```

2. Create a new Ghidra project to analyze ```irreversible```.
3. The main idea is to put user input (a number) into a ```secret_function``` which takes three parameters, and check if the return value matches with a certain number. 
4. My friend [@MooMooHorse](https://github.com/MooMooHorse) happened to be around when I was solving this puzzle, he took a glance at the reversed ```secret_function``` and said it's but a "fast exponentiation algorithm". LOL
5. So the problem is eventually equivalent with ```q^k = f (mod p)```, where ```q, f, p``` are given (pretty large) and want to know ```k```. Since the numbers are quite large and ```f <> 1``` doesn't have a good property, I have no good way to find ```k``` but to brute force. 
6. I copied the ```secret_function``` result of reverse engineering and added it with a brute forcing for loop, compile the ```bruteforce.c``` and execute will give the answer to feed to ```irreversible``` in a short time. 

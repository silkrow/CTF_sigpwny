1. First thing first, give execution permissions to the ```debugger``` file with the following command.

```chmod +x debugger```

2. Open Ghidra and create a new project, load ```debugger``` inside.  
3. Use Ghidra to analyze the ```debugger``` executable. Go to ```main``` function and investigate what the program does. For details of how to investigate, check out [this video](https://www.youtube.com/watch?v=vKuui7iCOB0). The key is to realize that there's a ```strncpy``` which takes user input string and compare it with the actual flag. There's also a if statement before the ```strncpy``` which requires the input string to be of length 0x15. 
4. With the 0x15 and ```strncpy``` in mind, open ```debugger``` with gdb, set breakpoint at the address of the line in assembly that calls ```strncpy``` (to locate this address, use Ghidra and refer to the assembly code it tells you), and feed the program with a 0x15 length string.
5. Investigate ```rsi,rdi``` registers when breakpoint is reached, to read the addresses of the strings given to ```strncpy``` function. One of the strings contains the real flag, the other one is our input.  

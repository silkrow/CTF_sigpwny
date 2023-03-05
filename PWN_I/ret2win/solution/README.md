1. Open **challenge** with gdb. If failed with permission error, use the command below to enable execute permission.

	chmod +x challenge

2. Set breakpoint for funciton print_flag.
	
	b print_flag

3. From the feedback of gdb, read the address of breakpoint, in my case it's 0x40125b.
4. Overwrite 32 + 8 characters to overflow name[32] and old rbp, than write the address of print_flag to **return address**.
5. The code in send.py has the payload to cause overflow, and some setups to connect to the server and send the payload.
6. Run following command to get the flag.

	python3 send.py

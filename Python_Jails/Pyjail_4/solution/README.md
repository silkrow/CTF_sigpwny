1. Run following command to get the flag.

```python3 send.py```

2. The idea is to define another ```is_bad(user_input)``` function to replace the real one, then call ```main()``` to do whatever you want. Note that when defining the new ```is_bad```, the function parameter shouldn't be ```user_input``` since ```input``` is in the blacklist.

#!/usr/bin/env python3

#Flag is at /flag.txt

def is_bad(user_input):
    banned = '"*'

    for c in banned:
        if c in user_input:
            return True
    
    return False


def main():

    print("You wake up in the jail kitchen. Your head is still sore from the bonk.")
    user_input = input('What do you have to say for yourself? ')

    if is_bad(user_input):
        print('Sorry, not good enough. Go back to jail.')
        return
    
    try:
        exec(user_input)
        print("Ok, we'll consider it.")
    except:
        print('Sorry, not good enough. Go back to jail.')


if __name__ == '__main__':
    main()

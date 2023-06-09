# Your goal is to read the flag at /flag.txt.
# For example, __import__('os').system('cat /flag.txt')
# or print(open('/flag.txt').read()).

def is_input_bad(s):
    # We allow anything for now! Is that a problem?
    return False


def main():
    print('Welcome to my calculator!')
    print('Enter your expression and I will evaluate it for you.')
    print('> ', end='')
    s = input()

    if is_input_bad(s):
        print("Hey what do you think you're doing?!")
        return

    print('Answer: {}'.format(eval(s)))


if __name__ == '__main__':
    main()

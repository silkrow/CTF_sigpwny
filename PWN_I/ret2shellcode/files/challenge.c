#include <stdio.h>
#include <stdlib.h>

// Ignore this function. It is just used to make
// the challenge work over the network.
void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {
    char name[32];

    setup();

    printf("Hey, what's your name? (name is located at %p)\n", name);

    // Put your shellcode in the buffer, and then overwrite the return address
    // with the address of the buffer. The shellcode should spawn a shell so you
    // can cat flag.txt. Google some 64 bit linux shellcode and just use that!
    // Use pwntools to read and write to the remote instead of netcat so that
    // you can parse the address of name.
    gets(name);
    printf("Nice to meet you, %s.\n", name);

    return 0;
}
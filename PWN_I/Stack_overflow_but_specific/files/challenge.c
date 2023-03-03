#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Ignore this function. It is just used to make
// the challenge work over the network.
void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

// Call this function to win!
void print_flag() {
    char c;
    FILE *f = fopen("flag.txt", "r");
    while ((c = fgetc(f)) != EOF) {
        putc(c, stdout);
    }
}

int main() {
    char name[32];
    // This is an 8 byte number which exists after the 32 bytes of name.
    uint64_t number = 0;

    setup();

    puts(
        "If you can change my number to 0x4142434445464748 I will give you a "
        "flag!");

    // Read a lot of input into name. What happens when we put (a lot) more than
    // 32 characters?
    gets(name);

    // Consider endianness! What order do you have to send these
    // characters if the system is little endian?
    // https://www.section.io/engineering-education/what-is-little-endian-and-big-endian/
    if (number == 0x4142434445464748) {
        print_flag();
    } else {
        printf("Not quite. The number is 0x%lx right now.\nTry again!\n",
               number);
    }

    return 0;
}
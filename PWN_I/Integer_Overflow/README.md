---
Added Time: Mar 3 2023
Difficulty: easy
Score: 150
Link: https://ctf.sigpwny.com/challenges#Meetings/Integer%20Overflow-128
---
i is an 8-bit unsigned number, which means it can hold 2^8 = 256 possible values, from 0 to 255 inclusive. atoi will convert your input to an integer. If you try to store something greater than 256 into an 8-bit unsigned integer, it'll wrap around!

So, the question is, what value of x will cause 50 + x > 256 but also 50 + x < 256 + 50?

nc chal.sigpwny.com 1342

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>

void vuln(char *string)
{
  uint8_t i = 50;
  i += atoi(string);
  if (i < 49)
  printf("[flag]\n");
}

int main(int argc, char **argv)
{
  vuln(argv[1]);
}

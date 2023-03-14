#include <stdio.h>

unsigned long secret_function(unsigned long param_1,unsigned long param_2, unsigned long param_3)

{
  unsigned long i;
  unsigned long local_20;
  unsigned long local_10;
  
  if (param_3 == 1) {
    local_10 = 0;
  }
  else {
    local_10 = 1;
    local_20 = param_1 % param_3;
    for (i = param_2; i != 0; i = i >> 1) {
      if ((i & 1) != 0) {
        local_10 = (local_10 * local_20) % param_3;
      }
      local_20 = (local_20 * local_20) % param_3;
    }
  }
  return local_10;
}

int main() {
	unsigned long l;
	unsigned long input;
	
	//input = 1;
	//l = secret_function(0x400000019, input, 0xffffffad5);
	//printf ("%ld\n", 0xffffffad5);
	//printf ("%ld\n", l);
	//printf ("%ld\n", 0x73a63a673);

	for (int i = 0; i < 1000000000; i++){
		unsigned long q = secret_function(0x400000019, i, 0xffffffad5);
		if (q == 0x73a63a673){
			printf("%d\n", i);
		}
	}

	return 0;
}

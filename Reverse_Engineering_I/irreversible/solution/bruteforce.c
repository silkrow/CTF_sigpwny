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
	
	for (unsigned long i = 0; i < 0xffffffad5; i++){
		unsigned long q = secret_function(0x400000019, i, 0xffffffad5);
		if (q == 0x73a63a673){
			printf("%ld\n", i);
			return 0;
		}
	}

	return 0;
}

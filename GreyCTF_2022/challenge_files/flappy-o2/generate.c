#include <stdio.h>

unsigned int key2[25] = {2091533035, 3444833704, 4148299095, 1382543044, 2034135277, 1758572224, 953820139, 1864200113, 961059707, 4109923606, 3982998552, 2329111456, 2938792015, 2156409201, 2261679400, 1133293590, 1468307596, 1270163339, 3218919622, 1843033993, 2968558243, 1433696446, 3279073000, 1084392560, 2824157242};
int lfsr2_seed = 439041101;

unsigned short int lfsr1(int n)
{
  unsigned int uVar1;
  int i;
  int seed;
  int lsb;
  
  seed = 0xabcd;
  for (i = 0; i < n; i = i + 1) {
    uVar1 = seed & 1;
    seed = seed >> 1;
    if (uVar1 != 0) {
      seed = seed ^ 0x82ee;
    }
  }
  return (unsigned short int)seed;
}

unsigned int lfsr2(int n)

{
  unsigned int uVar1;
  int i;
  int lsb;
  
  for (i = 0; i < n; i = i + 1) {
    uVar1 = lfsr2_seed & 1;
    lfsr2_seed = lfsr2_seed >> 1;
    if (uVar1 != 0) {
      lfsr2_seed = lfsr2_seed ^ 0x80000dd7;
    }
  }
  return lfsr2_seed;
}

int genFlag2(int i)

{
  unsigned short uVar1;
  unsigned int uVar2;
  
  uVar1 = lfsr1(i);
  uVar2 = lfsr2((unsigned int)uVar1);
  return key2[i/10000] ^ uVar2;
}

int main(void) 
{
    printf("Start\n");
    for (int i = 1; i <= 250000; i += 1) {
        lfsr2(1);
        if (i % 10000 == 0) {
          printf("%u\n", genFlag2(i-10000));
        }
    }
}
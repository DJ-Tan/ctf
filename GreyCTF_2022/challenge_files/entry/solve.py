import secrets

'''
Since we have the first 4 characters of the message and the ciphertext, we can XOR them to obtain the key

Use the obtained key and XOR with the ciphertext to obtain the flag.
'''

FLAG = b"grey{...}"

CIPHER = bytes.fromhex("982e47b0840b47a59c334facab3376a19a1b50ac861f43bdbc2e5bb98b3375a68d3046e8de7d03b4")

key = bytes([x ^ y for x, y in zip(FLAG,CIPHER[0:4])])

def encrypt(m):
    return bytes([x ^ y for x, y in zip(m,key)])

c = b''
for i in range(0, len(CIPHER), 4):
    c += encrypt(bytes(CIPHER[i : i + 4]))

print(c)
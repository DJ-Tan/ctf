from Crypto.Util.number import bytes_to_long, getPrime, isPrime, long_to_bytes

'''
Since we cubed 2 ** 100 times, the final exponent is given by 3 ** (2 ** 100) mod p - 1 since p is prime
We get the result e using fast exponentiation by starting with 3 and squaring 100 times mod p - 1

In terms of RSA, the value of e that we obtained would be the encryption key, therefore we can in the same
fashion obtain the decryption key d using p as N, resulting in phi of p - 1.

Once we have obtained d, we can decrypt the cipher message c to obtain our original message m just like RSA
'''

p = 147271787827929374875021125075644322658199797362157810465584602627709052665153637157027284239972360505065250939071494710661089022260751215312981674288246413821920620065721158367282080824823494257083257784305248518512283466952090977840589689160607681176791401729705268519662036067738830529129470059752131312559
c = 117161008971867369525278118431420359590253064575766275058434686951139287312472337733007748860692306037011621762414693540474268832444018133392145498303438944989809563579460392165032736630619930502524106312155019251740588974743475569686312108671045987239439227420716606411244839847197214002961245189316124796380

e = 3
for i in range(100):
    e = pow(e,2,p-1)
phi = p - 1
d = pow(e,-1,phi)
FLAG = long_to_bytes(pow(c,d,p)).decode('utf-8')
print(FLAG)

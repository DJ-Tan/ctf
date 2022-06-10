from sklearn.cluster import KMeans
import numpy as np
from pwn import *

with open("data.txt",'r') as f:
    data = np.array(list(map(float,f.read().split(", ")))).reshape(-1,1)
    clusters = KMeans(n_clusters = 3,init = 'k-means++').fit(data)
    centers = clusters.cluster_centers_.reshape(1,-1)[0]
    
r = remote("challs.nusgreyhats.org",10528)
r.recvuntil(b'1: ')
r.sendline(str(centers[0]).encode('utf-8'))
r.recvuntil(b'2: ')
r.sendline(str(centers[1]).encode('utf-8'))
r.recvuntil(b'3: ')
r.sendline(str(centers[2]).encode('utf-8'))
r.recvuntil(b'seconds.\n')
flag = r.recvline().decode('utf-8')
print(flag)
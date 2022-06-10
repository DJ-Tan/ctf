from sklearn.cluster import KMeans
import numpy as np
from pwn import *

'''
The data shows 3 distinct clusters of points, however, we do not know the centers.

We utilise the KMeans function which classifies the points into the desired 3 clusters
from which we can obtain the centers of each cluster.

We then connect to the server and provide the 3 obtained centers to retrieve the flag.
'''

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
import numpy as np
from scipy import linalg as lg
import pandas as pd
import matplotlib.pyplot as plt

N=100;M=N
a=np.zeros((N,M))
for k in range(N):
    if k%2==0:
        a[k,k]=-10
    if k%2!=0:
        a[k,k]=-8
    if k!=0:
        a[k,k-1]=-1
    if k!=(N-1):
        a[k,k+1]=-1
    a[0,N-1]=-1
    a[N-1,0]=-1
print(a)

e_val, e_vec = lg.eig(a)
min=np.min(e_val)
max=np.max(e_val)
range= max-min
band=range/N


plt.hist(e_val.real,bins=N,edgecolor='blue')
plt.title('N={}, beta =-1'.format(N))
plt.xlabel('Eigenvalues')
plt.ylabel('density of eigen states')
plt.show()

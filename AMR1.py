import numpy as np
from scipy import linalg as lg
import matplotlib.pyplot as plt

N=100;M=N
a=np.zeros((N,M))
for k in range(N):
    a[k,k]=-10
    if k!=0:
        a[k,k-1]=-5
    if k!=(N-1):
        a[k,k+1]=-5


e_val, e_vec = lg.eig(a)
min=np.min(e_val)
max=np.max(e_val)
range= max-min
band=range/N


plt.hist(e_val.real,bins=N,edgecolor='blue')
plt.title('N=100, beta =-5')
plt.xlabel('Eigenvalues')
plt.ylabel('density of eigen states')
plt.show()

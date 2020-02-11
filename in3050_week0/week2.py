# Standard import and functions
# Run this cell first
# matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2,3)
#print (x)
def f(x):
    return -np.power(x, 4) + 2 * np.power(x, 3) + 2 * np.power(x, 2) - x

def df(x):
    return -4 * np.power(x, 3) + 6 * np.power(x, 2) + 4 * x - 1
start=-1
step=0.1
x=np.arange(-1,3,step=0.1)
print(x)
for i in x:
    x=f(x)+step*df(x)
kernel = np.arange(25).reshape((5, 5))
kernel = kernel[::-1, ::-1]
Nk, Mk = kernel.shape
print (Nk, Mk)
nk_2 = Nk // 2
print (kernel)
print (nk_2)
#gradas=
#plt.plot(f(x))
#plt.plot(df(x))
#plt.plot(f(x),df(x))
#plt.legend()
#plt.show()
s1 = {2, 3, 1}
s2={'b','a','c'}
zipped=list(zip(s1,s2))
print (zipped)
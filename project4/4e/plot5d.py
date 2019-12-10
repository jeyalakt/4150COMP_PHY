from matplotlib import pyplot as plt
import numpy as np

#filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv100.txt'
#filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000.txt'
filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000_n10_2,8pi.txt'
#filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler10000.txt'
n = 1
with open(filename) as f:
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    plt.figure(1)
    plt.plot(x,y, 'b-', linewidth=2.0, label='N100')
    #plt.hist(y)
"""
with open(filename2) as f2:
    lines = f2.readlines()[1:]
    y2= [float(line.split()[1]) for line in lines]
    z2 = [float(line.split()[2]) for line in lines]
with open(filename3) as f3:
    lines = f3.readlines()[1:]
    y3 = [float(line.split()[1]) for line in lines]
    z3 = [float(line.split()[2]) for line in lines]
"""
plt.figure(1)
#plt.plot(x, y2, 'm:.', linewidth=2.0, label='L =60')
#plt.plot(x, y3, 'g:.', linewidth=2.0, label='L =40')
plt.legend(loc='upper right')
plt.xlabel(r"x[AU] ")
plt.ylabel(r" y[AU]")
plt.title(r"  Euler ")
plt.grid()
plt.savefig("eng.png")
plt.show()

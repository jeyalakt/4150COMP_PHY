from matplotlib import pyplot as plt
import numpy as np
from pylab import *
#filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler100.txt'
#filename2 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler1000.txt'
#filename3 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler10000.txt'
filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv100.txt'
filename2 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000.txt'
filename3 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler10000.txt'

with open(filename) as f:
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    plt.figure(1)
    plt.plot(x,y, 'b-', linewidth=2.0, label='N100')
    #plt.hist(y)

with open(filename2) as f2:
    lines = f2.readlines()[1:]
    x2 = [float(line.split()[0]) for line in lines]
    y2= [float(line.split()[1]) for line in lines]
    #z2 = [float(line.split()[2]) for line in lines]
    plt.plot(x2, y2, 'g-', linewidth=2.0, label='N1000')

with open(filename3) as f3:
    lines = f3.readlines()[1:]
    x3 = [float(line.split()[0]) for line in lines]
    y3 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x3,y3, 'r-', linewidth=2.0, label='N10000')
plt.figure(1)
#plt.plot(x, y2, 'm:.', linewidth=2.0, label='L =60')
#plt.plot(x, y3, 'g:.', linewidth=2.0, label='L =40')
plt.legend(loc='upper right')
plt.xlabel(r"x[AU] ")
plt.ylabel(r" y[AU]")
scatter([0], [0], s=20, color='yellow')
plt.title(r" Velocity Verlet -Sun Earth Model ")
plt.grid()
plt.savefig("VV_SunEarthmodelNall.png")
plt.show()

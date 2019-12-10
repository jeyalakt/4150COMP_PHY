from matplotlib import pyplot as plt
import numpy as np
from pylab import *
#filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler100.txt'
#filename2 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler1000.txt'
#filename3 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler10000.txt'
filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000_n14_2,1pi.txt'
filename2 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000_n14_2,5pi.txt'
filename3 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000_n14_2,7pi.txt'
filename4 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_vv1000_n14_2,8pi.txt'

with open(filename) as f:
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    plt.figure(1)
    plt.plot(x,y, 'b-', linewidth=2.0, label='2.1*pi')
    #plt.hist(y)

with open(filename2) as f2:
    lines = f2.readlines()[1:]
    x2 = [float(line.split()[0]) for line in lines]
    y2= [float(line.split()[1]) for line in lines]
    #z2 = [float(line.split()[2]) for line in lines]
    plt.plot(x2, y2, 'g-', linewidth=2.0, label='2.5*pi')

with open(filename3) as f3:
    lines = f3.readlines()[1:]
    x3 = [float(line.split()[0]) for line in lines]
    y3 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x3,y3, 'r-', linewidth=2.0, label='2.7*pi')

with open(filename4) as f4:
    lines = f4.readlines()[1:]
    x4 = [float(line.split()[0]) for line in lines]
    y4 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x4,y4, 'm-', linewidth=2.0, label='2.8*pi')

plt.figure(1)
#plt.plot(x, y2, 'm:.', linewidth=2.0, label='L =60')
#plt.plot(x, y3, 'g:.', linewidth=2.0, label='L =40')
plt.legend(loc='upper right')
plt.xlabel(r"x[AU] ")
plt.ylabel(r" y[AU]")
scatter([0], [0], s=20, color='yellow')
plt.title(r" Velocity Verlet -Escape velocity of earth ")
plt.grid()
plt.savefig("VV_earthescapevelocitylNallyr14.png")
plt.show()

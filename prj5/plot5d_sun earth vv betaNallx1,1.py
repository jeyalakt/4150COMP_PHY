from matplotlib import pyplot as plt
import numpy as np
from pylab import *
#filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler100.txt'
#filename2 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler1000.txt'
#filename3 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5a_euler10000.txt'
filename = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5d_vv1000_beta2_yr1_x1,1.txt'
filename2 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5d_vv1000_beta2,2_yr1_x1,1.txt'
filename3 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5d_vv1000_beta2,4_yr1_x1,1.txt'
filename4 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5d_vv1000_beta2,6_yr1_x1,1.txt'
filename5 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5d_vv1000_beta2,8_yr1_x1,1.txt'
filename6 = 'C:/Users/Bruker/4150COMP_PHY/prj5/prj5d_vv1000_beta3_yr1_x1,1.txt'
with open(filename) as f:
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    plt.figure(1)
    plt.plot(x,y, 'b-', linewidth=2.0, label='beta =2')
    #plt.hist(y)

with open(filename2) as f2:
    lines = f2.readlines()[1:]
    x2 = [float(line.split()[0]) for line in lines]
    y2= [float(line.split()[1]) for line in lines]
    #z2 = [float(line.split()[2]) for line in lines]
    plt.plot(x2, y2, 'g-', linewidth=2.0, label='beta=2.2')

with open(filename3) as f3:
    lines = f3.readlines()[1:]
    x3 = [float(line.split()[0]) for line in lines]
    y3 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x3,y3, 'r-', linewidth=2.0, label='beta=2.4')

with open(filename4) as f4:
    lines = f4.readlines()[1:]
    x4 = [float(line.split()[0]) for line in lines]
    y4 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x4,y4, 'm-', linewidth=2.0, label='beta=2.6')
with open(filename5) as f5:
    lines = f5.readlines()[1:]
    x5 = [float(line.split()[0]) for line in lines]
    y5 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x4,y4, 'c-', linewidth=2.0, label='beta =2.8')
with open(filename6) as f6:
    lines = f6.readlines()[1:]
    x6 = [float(line.split()[0]) for line in lines]
    y6 = [float(line.split()[1]) for line in lines]
   # z3 = [float(line.split()[2]) for line in lines]
    plt.plot(x4,y4, 'y-', linewidth=2.0, label='beta=3')
''
plt.figure(1)
#plt.plot(x, y2, 'm:.', linewidth=2.0, label='L =60')
#plt.plot(x, y3, 'g:.', linewidth=2.0, label='L =40')
plt.legend(loc='upper right')
plt.xlabel(r"x[AU] ")
plt.ylabel(r" y[AU]")
scatter([0], [0], s=20, color='yellow')
plt.title(r" Velocity Verlet -Sun earth as function of beta in Grav. force ")
plt.grid()
plt.savefig("VV_Sun -Earth model _betax1,1.png")
plt.show()

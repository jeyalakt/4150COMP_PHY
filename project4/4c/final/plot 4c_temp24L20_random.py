import sys, os
from matplotlib import pyplot as plt
import numpy as np
import math
import pylab
import glob
import errno

# folder = 'C:/users/Bruker/FYS-4150-COMP-PHY/build-prjitrial1-Desktop_Qt_5_13_0_minGW_64_bit-debug/'
# gaussian op folder = 'C:/users/Bruker/jeya/com phy prj data/prj 2/*'
# folder = 'C:/Users/Bruker/4150COMP_PHY/op _low upp/*' # LU op
folder = 'C:/Users/Bruker/4150COMP_PHY/project3/MC/'  # gauss op
# C:\Users\Bruker\jeya\com phy prj data\prj 1

# files=glob.glob(folder + "*.txt")
filename = 'C:/Users/Bruker/4150COMP_PHY/project4/4c/prj4c_temp24_L20_ranspin.txt'
# print(files)
# i=111
#for filename in files:
n = 1
# print('filename', filename)
with open(filename) as f:
    # lines=islice(f,1)
    lines = f.readlines()[1:]
    #x = [float(line.split()[2]) for line in lines]
    #print(x)
    y = [float(line.split()[2]) for line in lines]
    print(y)
    z = [float(line.split()[3]) for line in lines]
    #zz= [float(line.split()[11]) for line in lines]
    #print(z)
    plt.figure(1)
    # plt.subplot(i)
    #plt.axis([5000, 10000, 0, 1.0])
    MCbruteplot = plt.plot( y, 'b:.', linewidth=2.0, label='energy')
   # MCbruteplot = plt.plot(z, 'b:.', linewidth=2.0, label='MC brute force')
   # MCexponplot = plt.plot(x, z, 'm:v', linewidth = 2.0, label = 'MCExpon_imporsamp')
    #MCexponplot_jit=plt.plot(x, zz, 'g:o', linewidth = 2.0, label = 'MCExpon_imporsamp _parallel')
    plt.legend(loc='upper right')

    plt.xlabel(r"N X 10")
    plt.ylabel(r" energy")
    plt.title(r" plot of MC cycles vs. energy- temp 2.4,L=20, randomspin")
    plt.grid()
    plt.savefig(filename.replace(".txt", ".png"))
    plt.show()
"""
    x = [float(line.split()[0]) for line in lines]
    print(x)
    y = [float(line.split()[6]) for line in lines]
    print(y)
    z = [float(line.split()[9]) for line in lines]
    zz = [float(line.split()[12]) for line in lines]

    plt.figure(2)
    plt.axis([10000, 10000000, 0, 0.1])
    MCbruteplot = plt.plot(x, y, 'b:.', linewidth=2.0, label='MC brute force')
    MCexponplot = plt.plot(x, z, 'm:v', linewidth=2.0, label='MCExpon_imporsamp')
    MCexponplot_jit = plt.plot(x, zz, 'g:o', linewidth=2.0, label='MCExpon_imporsamp _parallel')
    plt.legend(loc='upper right')
    plt.xlabel(r"N")
    plt.ylabel(r" sigma")
    plt.title(r" plot of N Vs. MC -sigma values")
    plt.grid()
    #plt.savefig(filename.replace(".txt", ".png"))
    plt.show()

    x = [float(line.split()[0]) for line in lines]
    print(x)
    y = [float(line.split()[7]) for line in lines]
    print(y)
    z = [float(line.split()[10]) for line in lines]
    zz = [float(line.split()[13]) for line in lines]
    plt.figure(3)
    plt.axis([10000, 10000000, 0, 200])
    MCbruteplot = plt.plot(x, y, 'b:.', linewidth=2.0, label='MC brute force')
    MCexponplot = plt.plot(x, z, 'm:v', linewidth=2.0, label='MCExpon_imporsamp')
    MCexponplot_jit = plt.plot(x, zz, 'g:o', linewidth=2.0, label='MCExpon_imporsamp _parallel')
    plt.legend(loc='upper right')
    plt.xlabel(r"N")
    plt.ylabel(r" exe time(sec)")
    plt.title(r" plot of N Vs. MC -Exe time values")
    plt.grid()
    # plt.savefig(filename.replace(".txt", ".png"))
    plt.show()
"""
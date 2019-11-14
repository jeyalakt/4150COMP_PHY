from matplotlib import pyplot as plt

filename = 'C:/Users/Bruker/4150COMP_PHY/project4/4c/final/prj4c_temp1_L20_random_mc25000_plot.txt'
filename2 = 'C:/Users/Bruker/4150COMP_PHY/project4/4c/final/prj4c_temp24_L20_ranspin11_mcs25000_plot.txt'
#filename3 = 'C:/Users/Bruker/4150COMP_PHY/project4/4e/prj4e_temp2_26_01_L40_ranspin_mcs10000.txt'
#filename4 = 'C:/Users/Bruker/4150COMP_PHY/project4/4e/prj4e_temp2_26_01_L20_ranspin_mcs100000_time.txt'
n = 1
# print('filename', filename)
with open(filename) as f:
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    z=[float(line.split()[2]) for line in lines]
    s=[float(line.split()[3]) for line in lines]
    #m = [float(line.split()[4]) for line in lines]
    plt.figure(1)
    plt.plot(x,y, 'b:.', linewidth=2.0, label='Temp=1')
    #plt.hist(y)
with open(filename2) as f2:
    lines = f2.readlines()[1:]
    x2 = [float(line.split()[0]) for line in lines]
    y2= [float(line.split()[1]) for line in lines]
   # plt.plot(x, y2, 'b:.', linewidth=2.0, label='L=80')
    z2 = [float(line.split()[2]) for line in lines]
    s2 = [float(line.split()[3]) for line in lines]
    #m2= [float(line.split()[4]) for line in lines]
    """
with open(filename3) as f3:
    lines = f3.readlines()[1:]
    y3 = [float(line.split()[1]) for line in lines]
    z3 = [float(line.split()[2]) for line in lines]
    s3 = [float(line.split()[3]) for line in lines]
    m3 = [float(line.split()[4]) for line in lines]
    """
    plt.figure(1)
    plt.plot(x2, y2, 'm:.', linewidth=2.0, label='temp=2.4')
    #plt.plot(x, y3, 'g:.', linewidth=2.0, label='L =40')
    plt.legend(loc='upper right')
    plt.xlabel(r"MC ")
    plt.ylabel(r"  accept cycles")
    plt.title(r" MC =25000, random spin")
    plt.grid()
    plt.savefig("rand_acept.png")
    plt.show()
    #axes=plt.gca()
    #axes.set_ylim(0,3)
    #plt.ylim = (0, 3)
    plt.figure(2)

    plt.plot(x,z, 'b-', linewidth=2.0, label='Temp=1')
    plt.plot(x2, z2, 'm-', linewidth=2.0, label='Temp =2.4')

    #plt.plot(x, z3, 'g-', linewidth=2.0, label='L =40')
    plt.legend(loc='upper right')
    plt.xlabel(r"MC")
    plt.ylabel(r" energy")
    plt.title(r" MC =25000, random spin")
    plt.grid()
    plt.savefig("rand_eng.png")
    plt.show()
    plt.figure(3)
    plt.plot(x, s, 'b:', linewidth=2.0, label='Temp=1')
    plt.plot(x2, s2, 'm:', linewidth=2.0, label='Temp=2.4')

    #plt.plot(x, s3, 'g:', linewidth=2.0, label='L =40')
    plt.legend(loc='upper right')
    plt.xlabel(r"MC")
    plt.ylabel(r" Susceptibility")
    plt.title(r" MC =25000, random spin")
    plt.grid()
    plt.savefig("rand_suscep.png")
    plt.show()
    """
    plt.plot(x, m, 'b:', linewidth=2.0, label='L=80')
    plt.plot(x, m2, 'm:', linewidth=2.0, label='L =60')
    plt.plot(x, m3, 'g:', linewidth=2.0, label='L =40')
    plt.legend(loc='upper right')
    plt.xlabel(r"temp")
    plt.ylabel(r" |M|")
    plt.title(r" temp vs |M| , MCS =10000, randomspin")
    plt.grid()
    plt.savefig("meanmag.png")
    plt.show()
   
   """
"""
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
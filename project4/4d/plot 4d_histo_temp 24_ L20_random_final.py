from matplotlib import pyplot as plt
filename = 'C:/Users/Bruker/4150COMP_PHY/project4/4d/prj4d_temp24_L20_ranspin_final_100000.txt'
n = 1
# print('filename', filename)
with open(filename) as f:
    lines = f.readlines()[1:]
    #x = [float(line.split()[2]) for line in lines]
    #print(x)
    y = [float(line.split()[0]) for line in lines]
   # print(y)
    plt.figure(1)
    plt.hist(y)
    plt.legend(loc='upper right')
    plt.xlabel(r"energy bin")
    plt.ylabel(r"  energy")
    plt.title(r"  temp= 2.4, L =20, randomspin")
    plt.grid()
    plt.savefig(filename.replace(".txt", ".png"))
    plt.show()
"""
    plt.figure(2)

    MCbruteplot = plt.plot(z, 'b:.', linewidth=2.0, label='Magnetisation')
   # MCbruteplot = plt.plot(x, y, 'b:.', linewidth=2.0, label='MC brute force')
    #MCexponplot = plt.plot(x, z, 'm:v', linewidth=2.0, label='MCExpon_imporsamp')
    #MCexponplot_jit = plt.plot(x, zz, 'g:o', linewidth=2.0, label='MCExpon_imporsamp _parallel')
    plt.legend(loc='upper right')
    plt.xlabel(r"N")
    plt.ylabel(r" M")
    plt.title(r" plot of N Vs. Magnetisation")
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
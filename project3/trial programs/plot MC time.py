from matplotlib import pyplot as plt
filename = 'C:/Users/Bruker/4150COMP_PHY/project3/MC/MC all.txt'
with open(filename) as f:
    # lines=islice(f,1)
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    print(x)
    y = [float(line.split()[7]) for line in lines]
    print(y)
    z = [float(line.split()[9]) for line in lines]
    print(z)
    plt.axis([10000, 10000000, 0, 150])
    MCbruteplot = plt.plot(x, y, 'b:.', linewidth=2.0, label='MC brute force')
    MCexponplot = plt.plot(x, z, 'm:v', linewidth = 2.0, label = 'MCExpon_imporsamp')
    plt.legend(loc='upper right')

    plt.xlabel(r"N")
    plt.ylabel(r" exe time (sec)")
    plt.title(r" plot of  Exe time MC -brute force & exponential with importance sampling")
    plt.grid()
    #plt.savefig(filename.replace(".txt", ".png"))
    plt.show()

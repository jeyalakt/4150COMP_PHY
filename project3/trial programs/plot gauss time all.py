
from matplotlib import pyplot as plt
filename = 'C:/Users/Bruker/4150COMP_PHY/project3/final results/gauss all_table.txt'
with open(filename) as f:
    # lines=islice(f,1)
    lines = f.readlines()[1:]
    x = [float(line.split()[0]) for line in lines]
    print(x)
    y = [float(line.split()[6]) for line in lines]
    print(y)

    z = [float(line.split()[9]) for line in lines]

    print(z)

    plt.figure(1)

    plt.axis([5, 25, 0, 500])
    legentime = plt.plot(x, y, 'b:.', linewidth=2.0, label='Gauss Legendre')
    lagurretime = plt.plot(x, z, 'm:v', linewidth = 2.0, label = 'Gauss Laguerre')
    plt.legend(loc='upper right')
    plt.xlabel(r"N")
    plt.ylabel(r" Exe time(sec)")
    plt.title(r"  N & Exe time of Gauss Legendre and Laguerre")
    plt.grid()
   # plt.savefig(filename.replace(".txt", ".png"))
    plt.show()


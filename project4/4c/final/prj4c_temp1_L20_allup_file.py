from numpy import *
from random import random
from random import seed
from numba import jit
outf = open('prj4c_temp24_L20_allup.txt', 'w+')
outf.write("{:20s}{:20s}{:24s}{:24s}{:20s}{:20s}{:20s}" .format("n","spin_accpt","Ecalc"," Mabs_calc"))
outf.write("\n")
outf.close()

@jit
def periodic(curr,max,change):
    return int (curr+max+change)%max
@jit
def init(n_spin,E,M,lat):
    n_spin = 20
    a = (n_spin, n_spin)
    lat = zeros(a)
    E = 0
    M = 0
    for i in range(n_spin):
        for j in range(n_spin):
            lat[i][j] = 1
            #if (random()>=0.5):
              #  lat[i][j]=1
            #else:
             #   lat[i][j] =-1
            M+=lat[i][j]
    #print (lat)
    for i in range(n_spin):
        for j in range(n_spin):
            itemp=periodic(i,n_spin,-1)
            jtemp=periodic(j,n_spin,-1)
            E-=lat[i][j]*(lat[itemp][j]+lat[i][jtemp])
            #print ("E",E)
            #print("m",M)
    return E,M,lat
@jit
def Metropolis(n_spin, lat, E, M, w,accept):
    for i in range (0,n_spin):
        for j in range(0,n_spin):
            ix=int( random()*n_spin)
            jy=int(random() *n_spin)
            #print("ix,iy", ix, jy)
            left = lat[periodic(ix, n_spin, -1)][jy]
            right = lat[periodic(ix, n_spin, 1)][jy]
            up = lat[ix][periodic(jy, n_spin, -1)]
            down = lat[ix][periodic(jy, n_spin, 1)]
            own = lat[ix][jy]
            localE = 2 * own * (left + right + up + down)
            deltaE=localE
            if (w[int(deltaE+8)]>=random()):
                lat[ix][jy]*=-1
                # change the spin
                M+=2*lat[ix][jy]
                E+=deltaE
                accept+=1

    #print("E,M",E,M)
    #print("accpet",accept)
    return E,M,accept
    #print ("lat",lat)

def main():
    n_spin = 20
    temp = 1
    a=(n_spin,n_spin)
    lat=zeros(a)
    E=0
    M=0
    de=0
    accept=0
    #change of energy
    w=zeros(17)
    average=zeros(5)
    #for de in range (-8,8):
       # w[de+8]=0
    for de in range(-8,9,4):
        w[de+8]=exp(-de/temp)
    #print("w",w)
    for i in range (0,5):
        average[i]=0
    E, M, lat = init(n_spin,E,M,lat)
    initial_Eaverage = E / n_spin / n_spin
    initial_Mabsaverage = fabs(M) / n_spin / n_spin
    #print("lat after init", lat)
    accept=0
    for cycles in range (1,mcs+1):
        E,M,accept=Metropolis(n_spin, lat, E, M, w,accept)
       # print("e,M",E,M)
        average[0] += E
        #print("avg E",average[0])
        average[1] += E * E
        average[2] += M
        average[3] += M * M
        average[4] += abs(M)
    output(n_spin, mcs, temp, average, accept)
def output(n_spin, mcs, temp, average, accept):
    norm = 1 / mcs
    # norm2 = 1.0 / (n_n_spins * n_n_spins); // divide
    norm2 = 1.0;
    T = temp;
    Eaverage = average[0] * norm;
    #print("eavg",Eaverage)
    #E2average = average[1] * norm;
    #print("e2avg",E2average)
    Maverage = average[2] * norm;
    #M2average = average[3] * norm;
    Mabsaverage = average[4] * norm;
    #Evariance = (E2average - Eaverage * Eaverage) * norm2;
    #Mvariance = (M2average - Mabsaverage * Mabsaverage) * norm2;
    #print("Evariance", Evariance)
    #print("Mvariance", Mvariance)
    #print(Mabsaverage)


    """
    print(" Eaverage", Eaverage)
    print("E_exact", E_exact)
    print("CV_calc",Evariance / temp / temp )
    print("Cv_exact", Cv_exact)
    print("suscalc",Mvariance / temp)
    print("Suscept_exact", Suscept_exact)
    print("mag",Maverage*norm2)
    print("mag _exact",0)
    print("Mabs calc",Mabsaverage * norm2)
    print("absM_exact", absM_exact)
    print()
    print("Diff_E", Diff_E)
    print("Diff_CV", Diff_CV)
    print("Diff_chi", Diff_Chi)
    print("Diff_absM", Diff_absM)
    """
    outf = open('prj4c_temp24_L20_allup.txt', 'a')
    outf.write(str(mcs))
    outf.write("\t")
    outf.write(str(accept))
    outf.write("\t")
    outf.write("{:.6f}".format(Eaverage))
    outf.write("\t")
    #outf.write("{:.6f}".format(Evariance / temp / temp))
    #outf.write("\t\t")
    #outf.write("{:.6f}".format(Mvariance / temp))
    #outf.write("\t\t")
    outf.write("{:.6f}".format(Mabsaverage * norm2))
    outf.write("\n")
    outf.close()


#n=linspace(1 , 100, 1)
for i in range (1,250000,10):
    if __name__ == "__main__":
        mcs = i
        print("mcs",mcs)
        main()



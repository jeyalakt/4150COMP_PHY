from numpy import *
import time as time
from random import random
from random import seed
from numba import jit
from numpy.core._multiarray_umath import ndarray

outf = open('prj4e_temp1_L20_ranspin.txt', 'w+')
outf.write("temp`t\tEavg\t\tEvariance\t\tMaverage\t\tMvariance`\t\tMabsaverge \n")
outf.close()
"""
outf.write("{:.6f}".format(Eaverage/n_spin / n_spin)
    outf.write("\t\t")
    outf.write("{:.6f}".format(Evariance / temp / temp))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Maverage / n_spin / n_spin)
    outf.write("\t\t")
    outf.write("{:.6f}".format(Mvariance / temp))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Mabsaverage / n_spin / n_spin)
    outf.write("\t\t")
    outf.write(exetime)
"""
@jit
def periodic(curr,max,change):
    return int (curr+max+change)%max
@jit
def init(n_spin,E,M,lat,temp):
    n_spin = 20
    a = (n_spin, n_spin)
    lat = zeros(a)
    E = 0

    M = 0
    for i in range(n_spin):
        for j in range(n_spin):
            if (random()>=0.5):
                lat[i][j]=1
            else:
                lat[i][j] =-1
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
def Metropolis(n_spin, lat, E, M, w):
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

    #print("E,M",E,M)
    #print("accpet",accept)
    return E,M
    #return E, M, accept
    #print ("lat",lat)

def main():
    n_spin = 20
    temp_init=2.0
    temp_final=2.5
    temp_step=0.1
    temp = temp_init
    a=(n_spin,n_spin)
    lat=zeros(a)
    E=0
    M=0
    meanE = 0
    meanE2 = 0
    norm2=1
    de=0
    accept=0
    #change of energy
    w=zeros(17)
    average: ndarray=zeros(5)
    for temp in arange (temp_init,temp_final,temp_step):
        for de in range (-8,8):
            w[de+8]=0
        for de in range(-8,9,4):
             w[de+8]=exp(-de/temp)
    #print("w",w)
        for i in range (0,5):
            average[i]=0

    E, M, lat = init(n_spin,E,M,lat, temp)
    initial_Eaverage = E / n_spin / n_spin
    initial_Mabsaverage = fabs(M) / n_spin / n_spin
    #print("lat after init", lat)
    accept=0
    steadystecyle=5000
    start=time.process_time()
    for cycles in range (1,mcs+1):
        E,M=Metropolis(n_spin, lat, E, M, w)
        if cycles>steadystecyle:
            average[0] += E
            average[1] += E * E
            average[2] += M
            average[3] += M * M
            average[4] += abs(M)
    finish=time.process_time()
    exetime=finish-start
    out(n_spin,temp,average,exetime)
    meanE += E * norm2
    meanE2 += E * E * norm2 * norm2
    eff_cycle=mcs - steadystecyle
    norm = 1 / ((double)(eff_cycle + 1))
    meanE *= norm
    meanE2 *= norm
    print("mean E per spin:   " , meanE)
    print("mean E2 per spin:   ", meanE2)
    Evariance = meanE2 - meanE * meanE
    print("evar",Evariance)

def out(n_spin,temp,average,exetime):
    norm = 1 / mcs
    # norm2 = 1.0 / (n_n_spins * n_n_spins); // divide
    norm2 = 1.0

    Eaverage = average[0] * norm

    E2average = average[1] * norm

    Maverage = average[2] * norm

    M2average = average[3] * norm

    Mabsaverage = average[4] * norm
    
    Evariance = (E2average - Eaverage * Eaverage) / n_spin / n_spin;

    Mvariance = (M2average - Mabsaverage * Mabsaverage) / n_spin / n_spin;
    #Energy=E*norm2
    
    outf = open('prj4e_temp1_L20_ranspin.txt', 'a')
    outf.write(str(temp))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Eaverage/n_spin / n_spin))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Evariance / temp / temp))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Maverage / n_spin / n_spin))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Mvariance / temp))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Mabsaverage / n_spin / n_spin))
    outf.write("\t\t")
    outf.write(str(exetime))
    outf.write("\n")
    outf.close()


n=[100,1000]
for i in range (len(n)):
    if __name__ == "__main__":
        mcs = n[i]
        print("mcs",mcs)
        main()



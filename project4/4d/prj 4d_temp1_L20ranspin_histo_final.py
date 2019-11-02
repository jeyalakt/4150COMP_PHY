from numpy import *
import time as time
import sys
import matplotlib.pyplot as plt
from scipy.stats import uniform
from random import random
from random import seed
from numba import jit
outf = open('prj4d_temp1_L20_ranspin.txt', 'w+')
outf.write("energy \n")
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
    temp = 1
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
    steadystecyle=5000
    for cycles in range (1,mcs+1):
        E,M=Metropolis(n_spin, lat, E, M, w)
        if cycles>steadystecyle:
            out(n_spin, E)
            meanE += E * norm2;
            meanE2 += E * E * norm2 * norm2;
    norm = 1 / ((double)(mcs - steadystecyle + 1));
    meanE *= norm;
    meanE2 *= norm;
    print("mean E per spin:   " , meanE)
    print("mean E2 per spin:   ", meanE2)
    Evariance = meanE2 - meanE * meanE;
    print("evar",Evariance)

def out(n_spin, E):
    norm = 1 / mcs
    # norm2 = 1.0 / (n_n_spins * n_n_spins); // divide
    norm2 = 1.0;
    Energy=E*norm2
    outf = open('prj4d_temp1_L20_ranspin.txt', 'a')
    outf.write("{:.6f}".format(Energy))
    outf.write("\n")
    outf.close()


n=[100000]
for i in range (len(n)):
    if __name__ == "__main__":
        mcs = n[i]
        print("mcs",mcs)
        main()



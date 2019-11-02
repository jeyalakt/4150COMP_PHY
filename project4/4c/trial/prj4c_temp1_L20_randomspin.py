from numpy import *
import time as time
import sys
import matplotlib.pyplot as plt
from scipy.stats import uniform
from random import random
from random import seed
from numba import jit

def periodic(curr,max,change):
    return int (curr+max+change)%max

def init(n_spin,E,M,lat):
    n_spin = 20
    temp = 1
    a = (n_spin, n_spin)
    lat = zeros(a)
    E = 0
    M = 0
    de = 0
    # change of energy
    w = zeros(17)
    average = zeros(5)
    for i in range(n_spin):
        for j in range(n_spin):
            if (random()<0.5):
                lat[i][j] = 1
            else:
                lat[i][j] = -1
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

def Metropolis(n_spin, lat, E, M, w):
    #print(w)
    #print("lat1",lat)
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
            #print("own", own)
            #print("others",(left + right + up + down))
            deltaE=localE
            #deltaE=localengy(lat, ix, iy)
            #print("deltaE",deltaE)
            if (w[int(deltaE+8)]>=random()):
                lat[ix][jy]*=-1
                # change the spin
                M+=2*lat[ix][jy]
                E+=deltaE

    #print("E,M",E,M)
    return E,M
    #print ("lat",lat)

def main():
    n_spin = 20
    temp = 1
    idum = -1
    a=(n_spin,n_spin)
    lat=zeros(a)
    E=0
    M=0
    de=0
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
    #print("lat after init", lat)
    for cycles in range (0,mcs):
        E,M=Metropolis(n_spin, lat, E, M, w)
       # print("e,M",E,M)
        average[0] += E
        #print("avg E",average[0])
        average[1] += E * E
        average[2] += M
        average[3] += M * M
        average[4] += fabs(M)
    #output(n_spin, mcs, temp, average)
    norm = 1. / mcs
    print("mcs",mcs)
    # norm2 = 1.0 / (n_n_spins * n_n_spins); // divide
    norm2 = 1.0;
    T = temp;
    Eaverage = average[0] * norm;
    #print("eavg",Eaverage)
    E2average = average[1] * norm;
    #print("e2avg",E2average)
    Maverage = average[2] * norm;
    M2average = average[3] * norm;
    Mabsaverage = average[4] * norm;
    Evariance = (E2average - Eaverage * Eaverage) * norm2;
    Mvariance = (M2average - Mabsaverage * Mabsaverage) * norm2;
    #print("Evariance", Evariance)
    #print("Mvariance", Mvariance)
    #print(Mabsaverage)

    # Exact results for T = 1.0 (J = 1):
    cosh_fac = (3.0 + cosh(8 / T))
    # cosh_fac = (1.0+(3.0*cosh(8/T)))
    E_exact = -8.0 * sinh(8 / T) / cosh_fac * norm2
    # E_exact = 8.0*sinh(8/T)/cosh_fac*norm2
    Cv_exact = (8.0 / T) * (8.0 / T) * (1.0 + 3 * cosh(8 / T)) / (cosh_fac * cosh_fac) * norm2
    Suscept_exact = 1 / T * (12.0 + 8.0 * exp(8.0 / T) + 8 * cosh(8.0 / T)) / (cosh_fac * cosh_fac) * norm2
    absM_exact = (2.0 * exp(8.0 / T) + 4.0) / cosh_fac * norm2
    Diff_E = abs(Eaverage * norm2 - E_exact) / abs(E_exact)
    Diff_CV = abs(Evariance / temp / temp - Cv_exact) / Cv_exact
    Diff_Chi = abs(Mvariance / temp - Suscept_exact) / Suscept_exact
    Diff_absM = abs(Mabsaverage * norm2 - absM_exact) / absM_exact

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


n=[100]
for i in range (len(n)):
    if __name__ == "__main__":
        mcs = n[i]
        print("mcs",mcs)
        main()



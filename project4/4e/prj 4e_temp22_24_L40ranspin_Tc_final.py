from numpy import *
import time as time
from random import random
from random import seed
from numba import jit
import multiprocessing
p=multiprocessing.cpu_count()
print("cpu count",p)
# choose lattice size , mcs and temp_init, temp_final. temp-step
#steady state is 50 % of mcs  you can change the %

outf = open('prj4e_temp1_L80_ranspin_tc.txt', 'w+')
outf.write("{:20s}{:20s}{:24s}{:24s}{:20s}{:20s}{:20s}" .format("temp","Eavg","Heatcapacity","Maverage","Susceptibility","Mabsaverge","exetime"))
outf.write("\n")
#(temp,Eavg,Heatcapacity,Maverage,Susceptibility,Mabsaverge)
#format(temp`,Eavg\t\tHeatcapacity\t\tMaverage\t\tSusceptibility`\t\tMabsaverge \n")
outf.close()
@jit
def periodic(curr,max,change):
    return int (curr+max+change)%max
@jit
def init(n_spin,E,M,lat,temp):
    n_spin = 80
    # change the lattice size here
    a = (n_spin, n_spin)
    lat = zeros(a)
    E = 0
    M = 0
    for i in range(n_spin):
        for j in range(n_spin):
            if ((random()*n_spin)>=0.5):
                lat[i][j]=1
            else:
                lat[i][j] =-1
            M+=lat[i][j]
            #M=0
    #print (lat)
    for i in range(n_spin):
        for j in range(n_spin):
            itemp=periodic(i,n_spin,-1)
            jtemp=periodic(j,n_spin,-1)
            E-=lat[i][j]*(lat[itemp][j]+lat[i][jtemp])
            #print ("E",E)
            #print("m",M)
           # E=0
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
                #print(E)

    #print("E,M",E,M)
    #print("accpet",accept)
    return E,M
    #return E, M, accept
    #print ("lat",lat)

def main():
    n_spin = 80
    temp_init=2.20
    temp_final=2.40
    temp_step=0.001
    a=(n_spin,n_spin)
    lat=zeros(a)
    E=0
    M=0
    de=0
    #change of energy
    w=zeros(17)
    average=zeros(5)
    totalstart=time.process_time()
    for temp in arange (temp_init,temp_final,temp_step, float):
        #print (temp)
        for de in range(-8,8):
            w[de+8]=0
        for de in arange(-8,12,4):
             w[de+8]=exp(-de/temp)
        #print("w",w)
        for i in range(0,5):
            average[i]=0

        E, M, lat = init(n_spin,E,M,lat, temp)
        #print (E)
        #print(M)
        #print(lat)
        #print("lat after init", lat)
        accept=0
        steadystecyle=mcs*0.5
        #steady state assumed 15%
        start=time.process_time()
        for cycles in range(1,mcs+1):
            E,M=Metropolis(n_spin, lat, E, M, w)
            if cycles>steadystecyle:
                average[0] += E
                #print("average",average[0])
                average[1] += E * E
                average[2] += M
                average[3] += M * M
                average[4] += abs(M)
                #out(n_spin, temp, average)

        finish=time.process_time()
        exetime=finish-start
        #print("exetime",exetime)
        out(n_spin, temp, average,exetime)
    totalfinish=time.process_time()
    totaltime=totalfinish-totalstart
    print("toral time",totaltime)
        #out(n_spin,temp,average,exetime)
    #meanE += E * norm2
    #meanE2 += E * E * norm2 * norm2
    #eff_cycle=mcs - steadystecyle
    #norm = 1 / ((double)(eff_cycle + 1))
    #meanE *= norm
    #meanE2 *= norm
    #print("mean E per spin:   " , meanE)
    #print("mean E2 per spin:   ", meanE2)
    #Evariance = meanE2 - meanE * meanE
    #print("evar",Evariance)

def out(n_spin,temp,average,exetime):
    steadystecyle = mcs * 0.5
    norm = 1 / (mcs-steadystecyle)
    norm2 = 1.0 / (n_spin * n_spin)
    #// divide
    #norm2 = 1.0
    Eaverage = average[0] * norm
    #print(Eaverage)
    E2average = average[1] * norm
    #print(E2average)
    Maverage = average[2] * norm
    M2average = average[3] * norm
    Mabsaverage = average[4] * norm
    Evariance = (E2average - Eaverage * Eaverage)*norm2
    heatcapacity=Evariance/(temp*temp)
                #/ n_spin / n_spin
    #print(Evariance)
    Mvariance = (M2average - Mabsaverage * Mabsaverage) *norm2
                #/ n_spin / n_spin
    suscep=Mvariance/temp
    #Energy=E*norm2
    outf = open('prj4e_temp1_L80_ranspin_tc.txt', 'a')
    outf.write("{:.3f}".format(temp))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Eaverage*norm2))
    outf.write("\t\t")
    outf.write("{:.6f}".format(heatcapacity))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Maverage *norm2))
    outf.write("\t\t")
    outf.write("{:.6f}".format(suscep))
    outf.write("\t\t")
    outf.write("{:.6f}".format(Mabsaverage *norm2))
    outf.write("\t\t")
    outf.write(str(exetime))
    outf.write("\n")
    outf.close()


n=[10000]
for i in range (len(n)):
    if __name__ == "__main__":
        mcs = n[i]
        print("mcs",mcs)
        main()



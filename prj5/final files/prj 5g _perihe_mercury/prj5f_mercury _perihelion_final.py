from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
#outf = open('prj5a_euler100.txt', 'w+')
outf = open('prj5f_final.txt', 'w+')
outf.write(" potential\t\tkinetic\t\ttotal\t\tang_momen\n")
outf.close()
AU = 1.5E11  # 1 AU in Meters
sun_mass = 2E30  # Sun mass in kg
G = 4 * np.pi ** 2
#dt = 0.001
# dt is final time % by N 1 % 1000 , final = 1 ,dt=0.001
#dt is final time % by N 1 % 1000 , final = 10 , dt=0.01
N = int(1E3)
yr=10
dt=yr/N
#print(dt)
m_sun = 1
m_mer=1.65E-7 # if m_sun=1

x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
ax = np.zeros(N)
ay = np.zeros(N)
x[0] = 1
y[0] = 0
vx[0] = 0
# change vy to get escape velocity
vy[0] = 2.0 * np.pi
t1 = time.time()
p=[]
k=[]
tot=[]
angmom=[]
tan=[]
def Acc_Grav_mer(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    A_x = -G  * x*m_sun / r ** 3
    A_y = -G  *y* m_sun / r ** 3
    pot_x=-G  * m_sun*m_mer / r
    pot=pot_x
    #print(pot)
    return A_x, A_y, r,pot
A_x0,A_y0 ,r ,pot= Acc_Grav_mer(x[0],y[0])
ax[0] =  A_x0
ay[0] =  A_y0

#"""
# VelocityVerlet
c = 173 * 365
for j in range (yr):
    #print("j",j)
    dt=j/N
    #print("dt",dt)
    for i in range(N-1):
        x[i+1] = x[i] + vx[i]*dt + 0.5*ax[i]*dt**2
        y[i+1] = y[i] + vy[i]*dt + 0.5*ay[i]*dt**2
        A_x, A_y,r,pot= Acc_Grav_mer(x[i+1], y[i+1])
        pot+=pot
        ax[i+1] = A_x
        ay[i+1] =  A_y
        vx[i+1] = vx[i] + 0.5*dt*ax[i] +  0.5*dt*ax[i+1]
        vy[i+1] = vy[i] + 0.5*dt*ay[i] +  0.5*dt*ay[i+1]
        keteng = 0.5 * m_sun * m_mer * ((vx[i + 1]) ** 2 + (vy[i + 1]) ** 2)
        am=m_sun * m_mer *(vx[i+1]+vy[i+1])*r*0.39*AU /m_mer
        am = 1 + (3 * am ** 2) / (r ** 2 * c ** 2)
        angle=y[i]/x[i]
        #print(t)

        #am+=am
        keteng += keteng
        t = pot + keteng
   # print("pot+:", pot)
    p.append(pot)
    k.append(keteng)
    tot.append(t)
    angmom.append(am)
    tan.append(angle)
    print("x,y,tan",x,y,angle)
    print("\n")
    print( tan[0])
    #print("ke", k)
    #print("tot", tot)
    #print("ang mom",angmom)
    outf = open('prj5f_final.txt', 'a')
    outf.write("{:.6f}".format(p[j]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(k[j]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(tot[j]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(angmom[j]))
    outf.write("\n")
    outf.close()
plt.figure(1)

plt.plot(p, label='potential eng')
plt.plot(k, label='kinetic eng')
plt.plot(tot, label="total eng")
#plt.plot(angmom,label="ang mom")
plt.xlabel("year")
plt.legend(loc='upper right')
plt.title("eng _prj 5f ")
plt.savefig("eng_prj5f.png")
# plt.plot(tot)
# plt.plot(yr,keteng)
plt.show()
plt.figure(2)
plt.plot(angmom,label="ang mom")
plt.xlabel("year")
plt.legend(loc='upper right')
plt.title("ang mom- prj 5f ")
plt.savefig("angmom_prj5f.png")
plt.show()
plt.figure(3)
#plt.plot(x,y)
plt.plot(tan)
plt.xlabel("year")
plt.legend(loc='upper right')
plt.title("Mercury_Perihelion ")
plt.savefig("Mercury_Perihelion.png")
plt.show()
#"""
#"""
if __name__ == "__main__":

    t2 = time.time()
    #print(t2 - t1)

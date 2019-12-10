from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
from pylab import *
#outf = open('prj5a_euler100.txt', 'w+')
outf = open('prj5e_ear_mars.txt', 'w+')
outf.write(" x\t\ty\n")
outf.close()
AU = 1.5E11  # 1 AU in Meters
sun_mass = 2E30  # Sun mass in kg
G = 4 * np.pi ** 2
#dt = 0.001
# dt is final time % by N 1 % 1000 , final = 1 ,dt=0.001
#dt is final time % by N 1 % 1000 , final = 10 , dt=0.01
N = int(1E4)
yr=10
dt=yr/N
print(dt)
m_sun = 1 #2e30
m_earth=3e-6 # if m_sun=1
#m_earth=6e24 # in  kg
#m_jupiter=2e27
#m_mars=6.6e23 in kg distance 1.52 AU

m_jupiter=2e3 #if m_sun=1

m_mars=3.33e-7


x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
ax = np.zeros(N)
ay = np.zeros(N)

xj = np.zeros(N)
yj = np.zeros(N)
vxj = np.zeros(N)
vyj = np.zeros(N)
axj = np.zeros(N)
ayj = np.zeros(N)

xm = np.zeros(N)
ym = np.zeros(N)
vxm = np.zeros(N)
vym = np.zeros(N)
axm = np.zeros(N)
aym = np.zeros(N)

x[0] = 1
xj[0]=5.2
xm[0]=1.2
y[0] = 0
yj[0]=0
ym[0]=0
#x[0]=5.2 -0 , 0-0 jupiter x and y minus earth x, y
#x2[0]=5.2
#y2[0]=0
vx[0] = 0
vy[0] = (2.0 * (np.pi))
vxj[0] = 0
vyj[0] = (2.0 * (np.pi))*(5.2)
vxm[0]=0
vym[0]=(2.0 * (np.pi))*(1.2)
#vy2[0]=2.0 * np.pi- 2.0 * np.pi/np.sqrt(5.2)
#vx2[0]=0
#vy2[0]=2.0 * np.pi/np.sqrt(5.2)

t1 = time.time()
def Acc_Grav_earth(x,y):
    r = np.sqrt((x) ** 2 + (y) ** 2)
    A_x = -G  * x*m_sun/ r ** 3
    A_y = -G  *y* m_sun / r ** 3
    return A_x, A_y, r
def Acc_Grav_jup(x,y):
    rj = np.sqrt((xj) ** 2 + (yj) ** 2)
    A_xj= -G  * x*m_sun/ r ** 3
    A_yj = -G  *y* m_sun / r ** 3
    return A_xj, A_yj, rj
def Acc_Grav_mars(x,y):
    rm = np.sqrt((xj) ** 2 + (yj) ** 2)
    A_xm= -G  * x*m_sun/ r ** 3
    A_ym = -G  *y* m_sun / r ** 3
    return A_xm, A_ym, rm
A_x0,A_y0 ,r = Acc_Grav_earth((x[0]),(y[0]))
ax[0] =  A_x0
ay[0] =  A_y0

A_xj0,A_yj0 ,rj = Acc_Grav_earth((xj[0]),(yj[0]))
axj[0] =  A_xj0
ayj[0] =  A_yj0

A_xm0,A_ym0 ,rm = Acc_Grav_earth((xm[0]),(ym[0]))
axm[0] =  A_xm0
aym[0] =  A_ym0

#"""
# VelocityVerlet
for i in range(N-1):
    x[i+1] = x[i] + vx[i]*dt + 0.5*ax[i]*dt**2
    y[i+1] = y[i] + vy[i]*dt + 0.5*ay[i]*dt**2
    A_x, A_y,r= Acc_Grav_earth(x[i+1], y[i+1])
    ax[i + 1] = A_x
    ay[i + 1] = A_y
    vx[i+1] = vx[i] + 0.5*dt*ax[i] +  0.5*dt*ax[i+1]
    vy[i+1] = vy[i] + 0.5*dt*ay[i] +  0.5*dt*ay[i+1]


    xj[i + 1] = xj[i] + vxj[i] * dt + 0.5 * axj[i] * dt ** 2
    yj[i + 1] = yj[i] + vyj[i] * dt + 0.5 * ayj[i] * dt ** 2
    A_xj, A_yj, rj = Acc_Grav_jup(xj[i + 1], yj[i + 1])
    axj[i + 1] = A_xj
    ayj[i + 1] = A_yj
    vxj[i + 1] = vxj[i] + 0.5 * dt * axj[i] + 0.5 * dt * axj[i + 1]
    vyj[i + 1] = vyj[i] + 0.5 * dt * ayj[i] + 0.5 * dt * ayj[i + 1]

    xm[i + 1] = xm[i] + vxm[i] * dt + 0.5 * axm[i] * dt ** 2
    ym[i + 1] = ym[i] + vym[i] * dt + 0.5 * aym[i] * dt ** 2
    A_xm, A_ym, rm = Acc_Grav_jup(xm[i + 1], ym[i + 1])
    axm[i + 1] = A_xm
    aym[i + 1] = A_ym
    vxm[i + 1] = vxm[i] + 0.5 * dt * axm[i] + 0.5 * dt * axm[i + 1]
    vym[i + 1] = vym[i] + 0.5 * dt * aym[i] + 0.5 * dt * aym[i + 1]


    outf = open('prj5e_ear_mars.txt', 'a')
    outf.write("{:.6f}".format(x[i]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(y[i]))
    outf.write("\n")
    outf.close()
"""
"""
if __name__ == "__main__":
    t2 = time.time()
    print(t2 - t1)
    plt.figure(1)
    plt.plot(x,y, label='earth')
    plt.plot(xj,yj, label='jupiter')
    plt.plot(xm, ym, label='mars')
    plt.xlabel("x[AU]")
    plt.ylabel("y[AU]")
    plt.legend(loc='upper right')
    plt.title("sun-earth-jupitereff(original mass)model")
    scatter([0], [0], s=20, color='yellow')
    plt.savefig("sun-earth-jupitereff(original mass)model.png")
    plt.show()
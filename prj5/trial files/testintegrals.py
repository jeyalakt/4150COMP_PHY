from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
outf = open('prj5a_vv100000_p01.txt', 'w+')
outf.write(" x\t\ty\n")
outf.close()
AU = 1.5E11  # 1 AU in Meters
sun_mass = 2E30  # Sun mass in kg
G = 4 * np.pi ** 2
#dt = 0.001
# dt is final time % by N 1 % 1000 , final = 1 ,dt=0.001
#dt is final time % by N 1 % 1000 , final = 10 , dt=0.01
N = int(1E2)
yr=1
dt=yr/N
print(dt)
m_sun = 1
#m_earth=3E-6

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
#vy[0] = 8.89
#vy[0] = 8.5
#vy[0] = 8.2

t1 = time.time()
def Grav_earth(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
   # F_x=-G*m_sun*m_earth/r**3
    #F_y =-G *m_sun* m_earth /r ** 3
    #F_x = -G * x*m_sun / r ** 2
    #F_y = -G * y *m_sun/ r ** 2
    F_x = -G  * m_sun / r ** 3
    F_y = -G  * m_sun / r ** 3
    return F_x, F_y, r
F_x0,F_y0 ,r = Grav_earth(x[0],y[0])
ax[0] =  F_x0
ay[0] =  F_y0
#"""
# Euler-cromer
for i in range(N - 1):
    F_x, F_y, r = Grav_earth(x[i], y[i])
    vx[i + 1] = vx[i] + F_x *x[i]* dt  # F_x = ax
    vy[i + 1] = vy[i] + F_y *y[i]* dt  # F_y =ay
    #x[i + 1] = x[i] + vx[i + 1] * dt
    x[i + 1] = x[i] + vx[i ] * dt
    #y[i + 1] = y[i] + vy[i + 1] * dt
    y[i + 1] = y[i] + vy[i ] * dt
    outf = open('prj5a_euler100000_p01.txt', 'a')
    outf.write("{:.6f}".format(x[i]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(y[i]))
    outf.write("\n")
    outf.close()
#"""
"""
# VelocityVerlet
for i in range(N-1):
    x[i+1] = x[i] + vx[i]*dt + 0.5*ax[i]*dt**2
    y[i+1] = y[i] + vy[i]*dt + 0.5*ay[i]*dt**2
    F_x, F_y,r= Grav_earth(x[i+1], y[i+1])
    ax[i+1] = F_x
    ay[i+1] =  F_y
    vx[i+1] = vx[i] + 0.5*dt*ax[i] +  0.5*dt*ax[i+1]
    vy[i+1] = vy[i] + 0.5*dt*ay[i] +  0.5*dt*ay[i+1]
    outf = open('prj5a_vv100000_p01.txt', 'a')
    outf.write("{:.6f}".format(x[i]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(y[i]))
    outf.write("\n")
    outf.close()
"""
#"""
if __name__ == "__main__":
    csfont = {'fontname':'Times New Roman'}
    #plt.plot(x,y)
    plt.rcParams.update({'font.size': 22})
    plt.xlabel('x[AU]',**csfont)
    plt.ylabel('y[AU]',**csfont)
    #plt.title('Earth-Sun System Euler-Cromer[dt=0.0001]',**csfont)
    t2 = time.time()
    print(t2 - t1)
    plt.plot(x,y)
    plt.show()
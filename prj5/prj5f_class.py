from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
from pylab import *
from planet import Planet

#outf = open('prj5a_euler100.txt', 'w+')
outf = open('prj5e_jupeff_class.txt', 'w+')
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
m_sun = 1
m_earth=3e-6 # if m_sun=1
#m_earth=6e24 # in  kg
#m_jupiter=2e27
m_jupiter=2e3 #if m_sun=1

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

class gen:
    def _init_(self):
        self.x = np.zeros(N)
        self.y = np.zeros(N)
        self.vx = np.zeros(N)
        self.vy = np.zeros(N)
        self.ax = np.zeros(N)
        self.ay = np.zeros(N)
        self.A_x
        self.A_y
        self.r
        self.G=4*np.pi**2
        self.m_sun=1
        self.m_earth=3e-6
        #self.m_jupiter=2e3
        self.N=1e4
        self.yr=10
        self.AU = 1.5E11
        self.dt=self.yr/self.N

    def Acc_grav(self,planet):
        x=self.Planet.x_position()
        y=self.Planet.y_position()
        r = np.sqrt((x) ** 2 + (y) ** 2)
        A_x = -G * x * m_sun / r ** 3
        A_y = -G * y * m_sun / r ** 3
        return A_x, A_y, r

    def vv(self,planet,N):
        for i in range(N - 1):
            N = int(N)
            x = np.zeros(N)
            y = np.zeros(N)
            vx = np.zeros(N)
            vy = np.zeros(N)
            ax = np.zeros(N)
            ay = np.zeros(N)
            x[0] = planet.x_position()
            y[0] = planet.y_position()
            vx[0] = planet.velocity_x()
            vy[0] = planet.velocity_y()
            #        a_x0,a_y0  = self.new_accelaration_x_y(x[0],y[0])
            a_x0, a_y0 = self.Acc_grav(planet)
            ax[0] = a_x0
            ay[0] = a_y0
            for i in range(0, N - 1):
                x[i + 1] = x[i] + vx[i] * dt + 0.5 * ax[i] * dt ** 2
                y[i + 1] = y[i] + vy[i] * dt + 0.5 * ay[i] * dt ** 2

                A_x, A_y, r = self.Acc_grav(planet.x_position(), planet.y_position())
                #A_x, A_y, r = self.Acc_grav(x[i + 1], y[i + 1])
                ax[i + 1] = A_x
                ay[i + 1] = A_y
                vx[i + 1] = vx[i] + 0.5 * dt * ax[i] + 0.5 * dt * ax[i + 1]
                vy[i + 1] = vy[i] + 0.5 * dt * ay[i] + 0.5 * dt * ay[i + 1]

p1 = Planet(0, 0, 0.0, 0.0, 1, 'sun')
p2 = Planet(1, 0, 0, 2 * np.pi, 3e-6, 'earth')
G=gen()
x=G.vv(p1,100)
print("x",x)
"""
x[0] = 1
xj[0]=5.2
y[0] = 0
yj[0]=0
#x[0]=5.2 -0 , 0-0 jupiter x and y minus earth x, y
#x2[0]=5.2
#y2[0]=0
vx[0] = 0
vy[0] = (2.0 * (np.pi))
vxj[0] = 0
vyj[0] = (2.0 * (np.pi))*(5.2)
#vy2[0]=2.0 * np.pi- 2.0 * np.pi/np.sqrt(5.2)
#vx2[0]=0
#vy2[0]=2.0 * np.pi/np.sqrt(5.2)


A_x0,A_y0 ,r = Acc_Grav_earth((x[0]),(y[0]))
ax[0] =  A_x0
ay[0] =  A_y0

A_xj0,A_yj0 ,r = Acc_Grav_earth((xj[0]),(yj[0]))
axj[0] =  A_xj0
ayj[0] =  A_yj0
"""

if __name__ == "__main__":
    t2 = time.time()
    print(t2 - t1)
    plt.figure(1)
    plt.plot(x,y, label='earth')
    plt.plot(xj,yj, label='jupiter')
    plt.xlabel("x[AU]")
    plt.ylabel("y[AU]")
    plt.legend(loc='upper right')
    plt.title("sun-earth-jupitereff(original mass)model")
    scatter([0], [0], s=20, color='yellow')
    plt.savefig("sun-earth-jupitereff_class.png")
    plt.show()
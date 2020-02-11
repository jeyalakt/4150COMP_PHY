from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
from pylab import *
from planet import Planet

#outf = open('prj5a_euler100.txt', 'w+')
outf = open('prj5e_ear_mars_classtrial_1.txt', 'w+')
outf.write(" x\t\ty\n")
outf.close()
AU = 1.5E11  # 1 AU in Meters
sun_mass = 2E30  # Sun mass in kg
G = 4 * np.pi ** 2
#dt = 0.001
# dt is final time % by N 1 % 1000 , final = 1 ,dt=0.001
#dt is final time % by N 1 % 1000 , final = 10 , dt=0.01
N = int(1E4)
nop=1  # no of planets
yr=200
dt=yr/N
print(dt)
m_sun = 1 #2e30
m_earth=3e-6 # if m_sun=1
#m_earth=6e24 # in  kg
#m_jupiter=2e27
#m_mars=6.6e23 in kg distance 1.52 AU

m_jupiter=2e3 #if m_sun=1

m_mars=3.33e-7

class  solarsys:
    def __init__(self):
        self._planets=[]
        self._A_x=0
        self._A_y= 0
        self._r=0

    def add_planet(self, planet):
        self._planets.append(planet)
        return self._planets

    def Acc_Grav(self, obj):
        x=obj.x_position()
        #print("x",x)
        y=obj.y_position()
        self._r = np.sqrt((x) ** 2 + (y) ** 2)
        self._A_x = -G * x * m_sun /self._r ** 3
        self._A_y = -G * y * m_sun / self._r ** 3
        #print("self",self._A_x)
        return self._A_x, self._A_y, self._r
list=[]
s=solarsys()
#p1=Planet(0, 0, 0.0, 0.0,0, 1, 'sun')
p2 = Planet(1, 0, 0, 2 * np.pi, 3e-6,AU, 'earth')
p3 = Planet(5.2,0,0.0,(2.0 * np.pi/np.sqrt(5.2)),2e3,(AU*5.2),'jupiter')
p4=Planet(1.52,0,0.0,(2.0 * np.pi/np.sqrt(1.52)),3.33e-7,(AU*1.52),'mars')
p5=Planet(0.72,0,0.0,(2.0 * np.pi/np.sqrt(0.72)),2.45e-6,(AU*0.72),'venus')
p6=Planet(9.54,0,0.0,(2.0 * np.pi/np.sqrt(9.54)),2.75e-4,(AU*9.54),'saturn')
p7=Planet(0.39,0,0.0,(2.0 * np.pi/np.sqrt(0.39)),1.66e-7,(AU*0.39),'mercury')
p8=Planet(19.19,0,0.0,(2.0 * np.pi/np.sqrt(19.19)),4.4e-5,(AU*19.19),'uranus')
p9=Planet(30.06,0,0.0,(2.0 * np.pi/np.sqrt(30.06)),1.65e8,(AU*30.06),'neptune')
#list.append(p1)
list.append(p2)
list.append(p3)
list.append(p4)
list.append(p5)
list.append(p6)
list.append(p7)
list.append(p8)
list.append(p9)

t1 = time.time()

# VelocityVerlet
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
ax = np.zeros(N)
ay = np.zeros(N)

for obj in list:
    x[0] = obj.x_position()
    print("x0",x[0])
    y[0] = 0
    print("yo",y[0])
    vx[0] = 0
    vy[0] = obj.velocity_y()

    A_x0, A_y0, r = s.Acc_Grav(obj)
    ax[0] = A_x0
    ay[0] = A_y0
    for i in range(N-1):
        #p=p2
        x[i+1] = x[i] + vx[i]*dt + 0.5*ax[i]*dt**2
        y[i+1] = y[i] + vy[i]*dt + 0.5*ay[i]*dt**2
        obj._x=x[i+1]
        obj._y = y[i+1]
        A_x, A_y, r = s.Acc_Grav(obj)
        ax[i + 1] = A_x
        ay[i + 1] = A_y
        vx[i+1] = vx[i] + 0.5*dt*ax[i] +  0.5*dt*ax[i+1]
        vy[i+1] = vy[i] + 0.5*dt*ay[i] +  0.5*dt*ay[i+1]

        outf = open('prj5e_ear_mars_classtrial_1.txt', 'a')
        outf.write("{:.6f}".format(x[i]))
        outf.write("\t\t")
        outf.write("{:.6f}".format(y[i]))
        outf.write("\n")
        outf.close()
    nam=obj.name()
    plot(x, y, label=nam)
    plt.xlabel("x[AU]")
    plt.ylabel("y[AU]")
    plt.legend(loc='upper right')
    plt.title("solar sys model")
    scatter([0], [0], s=20, color='yellow')
    plt.savefig("solar sys model.png")
plt.show()

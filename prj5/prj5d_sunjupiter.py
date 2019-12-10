from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
#outf = open('prj5a_euler100.txt', 'w+')
outf = open('prj5e.txt', 'w+')
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
x[0] = 5.2
y[0] = 0
#x[0]=5.2 -0 , 0-0 jupiter x and y minus earth x, y
#x2[0]=5.2
#y2[0]=0
vx[0] = 0
vy[0] = (2.0 * (np.pi))/np.sqrt(5.2)
#vy2[0]=2.0 * np.pi- 2.0 * np.pi/np.sqrt(5.2)
#vx2[0]=0
#vy2[0]=2.0 * np.pi/np.sqrt(5.2)

t1 = time.time()
def Acc_Grav_earth(x,y):
    r = np.sqrt((x) ** 2 + (y) ** 2)
    A_x = -G  * x*m_sun/ r ** 3
    A_y = -G  *y* m_sun / r ** 3
    return A_x, A_y, r
def Acc_Grav_earth_jup1(x,y):
    r1 = np.sqrt((4.2+x) ** 2 + (0+y) ** 2)
    A_x1 = -G  * x*m_earth*m_jupiter/ r ** 3
    A_y1 = -G  *y* m_earth*m_jupiter / r ** 3
    return A_x, A_y, r
A_x0,A_y0 ,r = Acc_Grav_earth((x[0]),(y[0]))
ax[0] =  A_x0
ay[0] =  A_y0
#"""
# VelocityVerlet
for i in range(N-1):
    x[i+1] = x[i] + vx[i]*dt + 0.5*ax[i]*dt**2
    y[i+1] = y[i] + vy[i]*dt + 0.5*ay[i]*dt**2
    A_x, A_y,r= Acc_Grav_earth(x[i+1], y[i+1])
    #A_x1, A_y1, r1 = Acc_Grav_earth_jup1(x[i + 1], y[i + 1])
    #ax[i+1] = A_x+A_x1
    #ay[i+1] =  A_y+A_y1
    ax[i + 1] = A_x
    ay[i + 1] = A_y
    vx[i+1] = vx[i] + 0.5*dt*ax[i] +  0.5*dt*ax[i+1]
    vy[i+1] = vy[i] + 0.5*dt*ay[i] +  0.5*dt*ay[i+1]
    outf = open('prj5e.txt', 'a')
    outf.write("{:.6f}".format(x[i]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(y[i]))
    outf.write("\n")
    outf.close()
"""
"""
if __name__ == "__main__":
    csfont = {'fontname':'Times New Roman'}
    #plt.plot(x,y)
    #plt.rcParams.update({'font.size': 22})
    plt.xlabel('x[AU]',**csfont)
    plt.ylabel('y[AU]',**csfont)
    #plt.title('Earth-Sun System Euler-Cromer[dt=0.0001]',**csfont)
    t2 = time.time()
    print(t2 - t1)
    plt.plot(x,y)
    plt.show()
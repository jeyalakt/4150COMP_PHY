from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import time
#outf = open('prj5a_euler100.txt', 'w+')
outf = open('prj5a_vv1000_n10_peri.txt', 'w+')
outf.write(" x\t\ty\n")
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
print(dt)
m_sun = 1
#m_mer=1.65E-7

x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
ax = np.zeros(N)
ay = np.zeros(N)
x[0] = 1
y[0] = 0
vx[0] = 0

r_mer=[]
v_mer=[]
l=[]

# change vy to get escape velocity
vy[0] = 2.0 * np.pi

t1 = time.time()
def Acc_Grav_mer(x, y):
    r_mer = [x, y]
    #print ("r_mer",r_mer)
    v_mer = [vx, vy]
    l = abs(np.cross(r_mer, v_mer))
    #l = abs(np.cross((x,y),(vx,vy)))
    c = 173 * 365
    r = np.sqrt(x ** 2 + y ** 2)
    peri = 1 + (3 * l ** 2) / (r ** 2 * c ** 2)
    r = np.sqrt(x ** 2 + y ** 2)
    A_x = -G  * x*m_sun *peri/ r ** 3
    A_y = -G  *y* m_sun*peri / r ** 3
    return A_x, A_y, r

#A_x0,A_y0 ,r = Acc_Grav_mer(x[0],y[0])
#ax[0] =  A_x0
#ay[0] =  A_y0

ax[0] =  0
ay[0] =  0


#"""
# VelocityVerlet
for i in range(N-1):
    x[i+1] = x[i] + vx[i]*dt + 0.5*ax[i]*dt**2
    y[i+1] = y[i] + vy[i]*dt + 0.5*ay[i]*dt**2
    A_x, A_y, r = Acc_Grav_mer(x, y)
    #A_x, A_y,r= Acc_Grav_mer(x[i+1], y[i+1])
    ax[i+1] = A_x
    ay[i+1] =  A_y
    vx[i+1] = vx[i] + 0.5*dt*ax[i] +  0.5*dt*ax[i+1]
    vy[i+1] = vy[i] + 0.5*dt*ay[i] +  0.5*dt*ay[i+1]
    outf = open('prj5a_vv1000_n10_peri.txt', 'a')
    outf.write("{:.6f}".format(x[i]))
    outf.write("\t\t")
    outf.write("{:.6f}".format(y[i]))
    outf.write("\n")
    outf.close()
"""
"""
if __name__ == "__main__":

    #plt.plot(x,y)
    #plt.rcParams.update({'font.size': 22})
    plt.xlabel('x[AU]')
    plt.ylabel('y[AU]')
    #plt.title('Mercury-Sun System ')
    t2 = time.time()
    print(t2 - t1)
    plt.plot(x,y)
    plt.show()
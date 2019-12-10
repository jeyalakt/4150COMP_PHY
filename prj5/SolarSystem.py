import numpy as np
from planet import Planet
import matplotlib.pyplot as plt

outf = open('prj5c.txt', 'w+')
outf.write(" energy\n")
outf.close()

class SolarSystem:
    def __init__(self):
        self._potential_energy = []
        self._kenetic_energy = []
        self._planets = []
        self._G = 4 * np.pi ** 2
        self._acc_y = 0
        self._acc_x = 0
        self._gravitational_force = 0

    def add_planet(self, planet):
        self._planets.append(planet)
        return self._planets

    def number_of_planets(self):
        return len(self._planets)

    def kenetic_energy(self, planet):
        #vx, vy = self.updated_velocity_using_verlet(planet, 0.01, 1E3)
        vx, vy = self.euler(planet, 0.01, 1E3)
        v = []
        m = planet.mass()
        #print (m)
        for i in range(0, len(vx)):
            v.append(np.sqrt(vx[i] ** 2 + vy[i] ** 2))
            k1=self._kenetic_energy.append(0.5 * m * v[i] ** 2)
        #plt.plot(k1)
        #plt.show()
        return self._kenetic_energy

    def potential_energy(self, planet1, planet2):
        #rx, ry = self.Velocity_verlet(planet2, 0.01, 1E3)
        rx, ry = self.euler(planet2, 0.01, 1E3)
        r = []
        for i in range(0, len(rx)):
            r.append(np.sqrt(rx[i] ** 2 + ry[i] ** 2))
            self._potential_energy.append(-self._G * planet1.mass() * planet2.mass() / r[i])
            #outf = open('prj5c.txt', 'a')
            #outf.write("{:.6f}".format(potential_energy[i]))
            #outf.write("\t\t")
        #plt.plot(potential_energy[i])
        #plt.show()
        return self._potential_energy

    def total_energy(self, planet1, planet2):
        total_k = S.kenetic_energy(planet2)
        total_p = S.potential_energy(planet1, planet2)
        total = []
        for i in range(0, len(total_k)):
            total.append(total_k[i] + total_p[i])
            outf = open('prj5c.txt', 'a')
            outf.write("{:.6f}".format(total[i]))
            outf.write("\t\t")
        #print (total)
        plt.plot(total)
        plt.show()
        return total

    def angular_momentum(self, planet, h, n):
        rx, ry = self.Velocity_verlet(planet, h, n)
        #rx, ry = self.euler(planet, h, n)
        vx, vy = self.updated_velocity_using_verlet(planet, h, n)


        l = []
        r = []
        v = []
        for i in range(0, len(vx)):
            v.append(np.sqrt(vx[i] ** 2 + vy[i] ** 2))
            r.append(np.sqrt(rx[i] ** 2 + ry[i] ** 2))
            l.append(r[i] * v[i])
            #print(l)
        #print(l)
        plt.plot(l)
        plt.show()
        return l

    def accelaration_vs_sun(self, planet_n):

        x = planet_n.x_position()
        #print(x)
        y = planet_n.y_position()
        r = np.sqrt(x ** 2 + y ** 2)
        #print(r)
        acc_x = -self._G * x / r ** 3
        acc_y = -self._G * y / r ** 3
        return acc_x, acc_y

    def accelaration_mercury(self, planet):
        v = [planet.velocity_x(), planet.velocity_y()]
        r = [planet.x_position(), planet.y_position()]
        l = abs(np.cross(r, v))
        c = 173 * 365
        r = np.sqrt(planet.x_position() ** 2 + planet.y_position() ** 2)
        p_multiple = 1 + (3 * l ** 2) / (r ** 2 * c ** 2)
        #acc_x = -self._G * planet.x_position() * p_multiple / r ** 3
       # acc_y = -self._G * planet.y_position() * p_multiple / r ** 3
        return acc_x, acc_y

    def accelaration(self, planet_n):
        acc_x, acc_y = 0, 0

        for planet in self._planets:
            if planet.name() == 'sun':
                acc_x, acc_y = self.accelaration_vs_sun(planet_n)
            if planet.name() != planet_n.name():
                x = planet.x_position()
                y = planet.x_position()
                x_n = planet_n.x_position()
                y_n = planet_n.y_position()
                r = np.sqrt((x_n - x) ** 2 + (y_n - y) ** 2)
               # acc_x += -self._G * (x_n - x) * planet.mass() / r ** 3
               # acc_y += -self._G * (y_n - y) * planet.mass() / r ** 3
        return acc_x, acc_y

    def Gravitational_force(self, planet1, planet2):
        r1 = planet1.x_position() - planet2.x_position()
        r2 = planet1.y_position() - planet2.y_position()
        r = np.sqrt(r1 ** 2 + r2 ** 2)
        self._gravitational_force = self._G * planet1.mass() * planet2.mass() / r ** 2
        return self._gravitational_force

    def euler(self, planet, h, n):
        N = int(n)
        x = np.zeros(N)
        y = np.zeros(N)
        vx = np.zeros(N)
        vy = np.zeros(N)
        x[0] = planet.x_position()
        y[0] = planet.y_position()
        vx[0] = planet.velocity_x()
        vy[0] = planet.velocity_y()
        for i in range(0, N - 1):
            ax, ay = self.accelaration(planet)
            planet.update_position(x[i + 1], y[i + 1])
            vx[i + 1] = vx[i] + ax * h
            vy[i + 1] = vy[i] + ay * h
            x[i + 1] = x[i] + vx[i + 1] * h
            y[i + 1] = y[i] + vy[i + 1] * h

        return x, y

    def updated_velocity_using_verlet(self, planet, h, n):
        N = int(n)
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
        a_x0, a_y0 = self.accelaration_vs_sun(planet)
        ax[0] = a_x0
        ay[0] = a_y0
        for i in range(0, N - 1):
            x[i + 1] = x[i] + vx[i] * h + 0.5 * ax[i] * h ** 2
            y[i + 1] = y[i] + vy[i] * h + 0.5 * ay[i] * h ** 2
            planet.update_position(x[i + 1], y[i + 1])
            a_x, a_y = self.accelaration_vs_sun(planet)
            ax[i + 1] = a_x
            ay[i + 1] = a_y
            vx[i + 1] = vx[i] + 0.5 * h * ax[i] + 0.5 * h * ax[i + 1]
            vy[i + 1] = vy[i] + 0.5 * h * ay[i] + 0.5 * h * ay[i + 1]
        return vx, vy

    def Velocity_verlet(self, planet, h, n):
        N = int(n)
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
        a_x0, a_y0 = self.accelaration(planet)
        ax[0] = a_x0
        ay[0] = a_y0
        for i in range(0, N - 1):
            x[i + 1] = x[i] + vx[i] * h + 0.5 * ax[i] * h ** 2
            y[i + 1] = y[i] + vy[i] * h + 0.5 * ay[i] * h ** 2
            planet.update_position(x[i + 1], y[i + 1])
            a_x, a_y = self.accelaration(planet)
            ax[i + 1] = a_x
            ay[i + 1] = a_y
            vx[i + 1] = vx[i] + 0.5 * h * ax[i] + 0.5 * h * ax[i + 1]
            vy[i + 1] = vy[i] + 0.5 * h * ay[i] + 0.5 * h * ay[i + 1]

        return x, y

    def prehelion_with_VV(self, planet, h, n):
        N = int(n)
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
        a_x0, a_y0 = self.accelaration_mercury(planet)
        ax[0] = a_x0
        ay[0] = a_y0
        for i in range(0, N - 1):
            x[i + 1] = x[i] + vx[i] * h + 0.5 * ax[i] * h ** 2
            y[i + 1] = y[i] + vy[i] * h + 0.5 * ay[i] * h ** 2
            planet.update_position(x[i + 1], y[i + 1])

            a_x, a_y = self.accelaration_mercury(planet)
            ax[i + 1] = a_x
            ay[i + 1] = a_y
            vx[i + 1] = vx[i] + 0.5 * h * ax[i] + 0.5 * h * ax[i + 1]
            vy[i + 1] = vy[i] + 0.5 * h * ay[i] + 0.5 * h * ay[i + 1]
            planet.update_velocity(vx[i + 1], vy[i + 1])

        return x, y

    def Center_of_mass(self):
        total_mass = 0
        center_of_mass_x = 0
        center_of_mass_y = 0
        for planet in self._planets:
            x1 = planet.x_position()
            y1 = planet.y_position()
            total_mass += planet.mass()
            center_of_mass_x += x1 * planet.mass() / total_mass
            center_of_mass_y += y1 * planet.mass() / total_mass
        return center_of_mass_x, center_of_mass_y

    def total_momentum(self):
        total_momentum_x = 0
        total_momentum_y = 0
        mass = 0
        vx = 0
        vy = 0
        for planet in self._planets:
            vx = planet.velocity_x()
            vy = planet.velocity_y()
            mass = planet.mass()
            total_momentum_x += mass * vx
            total_momentum_y += mass * vy
        return total_momentum_x, total_momentum_y
S=SolarSystem()
p1 = Planet(0, 0, 0.0, 0, 1, 'sun')
p2 = Planet(1, 0, 0, 2 * np.pi, 3e-6, 'earth')
angular_momentum = S.angular_momentum(p2,0.01,1E4)
eng=S.total_energy(p1,p2)
#ke=kenetic_energy(p2)
#po=potential_energy(p1,p2)
#print(angular_momentum)
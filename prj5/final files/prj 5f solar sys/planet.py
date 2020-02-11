class Planet:
    def __init__(self, x, y, vx, vy, mass,AU, name):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
        self._mass = mass
        self._name = name
        self.m_sun=1
        self._AU=AU

    def x_position(self):
        return self._x

    def y_position(self):
        return self._y

    def velocity_x(self):
        return self._vx

    def velocity_y(self):
        return self._vy

    def mass(self):
        return self._mass
    def AU(self):
        return self._AU

    def name(self):
        return self._name

    def update_position(self, x, y):
        self._x = x
        self._y = y

    def update_velocity(self, vx, vy):
        self._vx = vx
        self._vy = vy
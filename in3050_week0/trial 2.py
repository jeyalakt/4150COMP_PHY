import numpy as np
import matplotlib.pyplot as plt
#import math
"""
x_scatter = np.random.normal(size=100)
y_scatter = np.random.normal(loc=5, scale=10, size=100)
plt.plot(x_scatter,y_scatter)
plt.show()
"""
x_line = np.linspace(0,2*np.pi)
print(x_line)
# TODO:  Create two arrays with sin and cos values from using the values in x_line
y1_line = np.sin(x_line)
y2_line = np.cos(x_line)
plt.plot(x_line,y1_line,label='sin')
r=np.random.normal(size=1000)
plt.legend()
plt.show()
plt.hist(r)
plt.show()
# 3d graph

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def f(x, y):
    return np.cos(x ** 2 + y ** 2) / (1 + x ** 2 + y ** 2)


def f1(x, y):
    return (np.sin(5 * x) * np.cos(5 * y)) / 5


xgrid = np.linspace(-3, 3, 50)
ygrid = xgrid
x, y = np.meshgrid(xgrid, ygrid)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, f(x, y), rstride=1, cstride=1, cmap=cm.jet, alpha=0.7, linewidth=0.25)
ax.set_zlim(-0.5, 1)

plt.show()

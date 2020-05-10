import matplotlib.pyplot as plt
import numpy as np


def f(x, o):
    return np.cos(np.pi * o * x) * np.exp(-x)


o_range = np.linspace(0, 2, 10)
x = np.linspace(0, 5, 200)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

for o in o_range:
    ax.plot(x, f(x, o))

plt.show()

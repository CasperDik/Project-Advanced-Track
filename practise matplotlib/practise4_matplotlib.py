from matplotlib import pyplot as plt
import numpy as np

x_begin = 0
x_end = 100
x_interval = 1

x_data = np.arange(x_begin, x_end, x_interval)
y_data = []
y2_data = []

for x in np.arange(x_begin, x_end, x_interval):
    y = x ** 2
    y_data.append(y)

for x in np.arange(x_begin, x_end, x_interval):
    a = 20
    b = 800
    y2 = a * x + b
    y2_data.append(y2)

plt.plot(x_data, y_data, "--", label="exponential")
plt.plot(x_data, y2_data, "--", label="linear")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()

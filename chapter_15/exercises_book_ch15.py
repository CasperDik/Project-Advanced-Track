#combined ex 1&2
from matplotlib import pyplot as plt

x_data1 = [0.1, 0.2, 0.3, 0.4]
y_data1 = [1, 2, 3, 4]

x_data2 = [0.1, 0.2, 0.3, 0.4]
y_data2 = [1, 4, 9, 16]

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.plot(x_data1, y_data1, "--", label='data 1')
ax2.plot(x_data2, y_data2, "-", marker="s", label='data 2')
ax1.legend()
ax2.legend()

plt.savefig("plot2.pdf")
plt.show()
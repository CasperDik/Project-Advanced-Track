from matplotlib import pyplot as plt

plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4], "rx", label = "first plot")
plt.plot([0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16],"b-.", label = "second plot")
plt.xlabel("Time (s)")
plt.ylabel("Scale (Bananas)")
plt.legend()
plt.xlim(0,0.5)
plt.ylim(0,20)
plt.show()

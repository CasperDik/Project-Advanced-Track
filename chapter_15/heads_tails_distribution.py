# central limit theorem?

import random
from matplotlib import pyplot as plt

probability_tails = 0.5
n = 500

count = []
tails = 0

for i in range(1, n):
    ran = random.random()
    if ran > probability_tails:
        tails += 1
    else:
        tails -= 1
    expected_tails = tails / i
    count.append(expected_tails)

x_range = list(range(len(count)))

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(x_range, count, color="b", label="expected tails")
ax1.set_xlabel("n")
ax1.set_ylabel("expected tails")
ax1.set_xlim(5, n)
ax1.set_ylim(-1, 1)
ax1.axhline(0, color='black', ls='--')

ax2.hist(count, bins=30)

plt.show()

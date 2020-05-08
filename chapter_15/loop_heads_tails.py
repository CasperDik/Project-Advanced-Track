import random
from matplotlib import pyplot as plt

nested_list = []
probability_tails = 0.5
n = 1000
n_lines = 5

for i in range(n_lines):

    count = []
    tails = 0

    for i in range(1, n):
        ran = random.random()
        if ran < probability_tails:
            tails += 1
        else:
            tails -= 1
        expected_tails = tails / i
        count.append(expected_tails)
    nested_list.append(count)

x_range = list(range(len(count)))

for i in range(n_lines):
    plt.plot(x_range, nested_list[i])

plt.xlim(5, n)
plt.ylim(-1, 1)
plt.axhline(0, color="black", ls="--")
plt.show()

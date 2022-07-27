import numpy as np
import matplotlib.pyplot as plt



labels = ["Google Chrome", "Opera", "Safari"]
shares = np.array([
    [0.5, 0.3, 0.2],    # 2016
    [0.4, 0.35, 0.25],  # 2017
    [0.35, 0.4, 0.25],  # 2018
    [0.4, 0.35, 0.2],   # 2019
    [0.5, 0.3, 0.2],    # 2020
    [0.6, 0.25, 0.15],  # 2021
    [0.7, 0.25, 0.05]   # 2022
])

years = [2016 + i for i in range(8)]

plot_steps = np.array([shares[0]])
last_shares = shares[0]
for i in range(1, len(shares)):
    differences = shares[i] - last_shares
    differences /= 100

    for j in range(101):
        plot_steps = np.append(plot_steps, [last_shares + differences * j], 0)
    last_shares = shares[i]

print(plot_steps)

years = iter(years)
year = next(years)

for i, step in enumerate(plot_steps):
    if i % 100 == 0:
        year = next(years)
    plt.xlim(0, 1)
    plt.barh(labels, step, color=["green", "red", "blue"])

    plt.text(0.8, 0.2, year, fontsize=14)
    plt.pause(0.01)

plt.show()
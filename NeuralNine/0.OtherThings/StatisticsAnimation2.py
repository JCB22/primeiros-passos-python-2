"""

Tarefa:
Pegar um arquivo do banco mundial que mostra o gdp per capita ao invez do gdp todal

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

years = [str(1960 + i) for i in range(53)]

countries = ["United States", "Canada", "Germany", "United Kingdom", "Portugal", "Brazil"]

# df == "Data Frame"
df = pd.read_csv("gdp_mundo.csv")
df = df.query("`Country Name`==@countries")

countries = df['Country Name']

df = df[['Country Name'] + years].dropna(axis=1)

data = np.empty((1, 6))

for year in df.columns[1:]:
    data = np.append(data, [df[year].to_numpy()], 0)

plot_steps = np.array([data[0]])
last_gdp = data[0]

for i in range(1, len(data)):
    # no primeiro loop: last_gdp está com o data[0], enquanto
    # o data[i] está com o data[1], fazendo data[1] - data[0]
    # Falando "Eu quero a segunda informação menos a primeira"
    differences = data[i] - last_gdp
    differences /= 100
    for j in range(100):
        plot_steps = np.append(plot_steps, [last_gdp + differences * j], 0)
    last_gdp = data[i]

colors = ["#ff5555", "#55ff55", "#5555ff", "#55ccff", "#ffaa55", "#ff55ff"]

years = iter(df.columns[1:])
for i, step in enumerate(plot_steps):
    if i % 100 == 0:
        try:
            year = next(years)
        except StopIteration:
            pass

    list_sorted = step.copy()
    list_sorted.sort()

    list_index = []
    for x in list_sorted:
        list_index.insert(0, list(step).index(x))

    country_names = df['Country Name'].to_numpy()
    ordered_names = [country_names[i] for i in list_index]
    ordered_colors = [colors[i] for i in list_index]

    plt.title("GDP per Capita")
    plt.barh(ordered_names[::-1], list_sorted, color=ordered_colors[::-1])
    plt.text(50000, 0.2, year, fontsize=18)
    plt.xlim(0, 70000000000)
    plt.pause(0.001)
    plt.clf()

plt.show()

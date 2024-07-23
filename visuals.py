from webscraper import *
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(figsize=(8,6))
plt.style.use("seaborn-v0_8-dark")
axes = fig.add_subplot(1,1,1)
axes.set_xlim(0,500)
palette = ['black', 'yellow', 'blue', 'red']


y1, y2, y3, y4 = [], [], [], []
def animate(i):
    y1 = sequences[0][i]
    y2 = sequences[1][i]
    y3 = sequences[2][i]
    y4 = sequences[3][i]

    axes.cla()
    plt.grid(axis='x')
    plt.xlabel("Points")
    plt.xticks(np.arange(0, 500, 50))
    plt.barh(['Cardinals', 'Rams', 'Seahawks', '49ers'], [y1, y2, y3, y4], color=palette)
    plt.bar_label(plt.gca().containers[0], label_type='edge', padding=2)

    plt.title("NFC West Total Points Scored 2023-2024 | Week {} ".format(df['Week'][i]))
    axes.set_xlim(0,500)

visual = FuncAnimation(fig, animate, frames=len(sequences[0]), interval=1000)
plt.show()
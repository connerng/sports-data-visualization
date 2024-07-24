from data import *
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
    az_score = sequences[0][i]
    la_score = sequences[1][i]
    sea_score = sequences[2][i]
    sf_score = sequences[3][i]

    sorted_scores = sorted([az_score, la_score, sea_score, sf_score])
    sorted_indices = []

    if i > 0:
        for score in sorted_scores:
            for ind in range(0, len(sequences)):
                if sequences[ind][i] == score and ind not in sorted_indices:
                    sorted_indices.append(ind)
        sorted_teams = [teams[idx] for idx in sorted_indices]
        sorted_colors = [palette[idx] for idx in sorted_indices]
    else:
        sorted_teams = teams
        sorted_colors = palette
    
    axes.cla()
    plt.grid(axis='x')
    plt.xlabel("Points")
    axes.set_xlim(0, 500)
    plt.barh(sorted_teams, sorted_scores, color=sorted_colors)
    plt.bar_label(plt.gca().containers[0], label_type='edge', padding=2)

    plt.title("NFC West Total Points Scored 2023-2024 | Week {} ".format(df['Week'][i]))
    axes.set_xlim(0,500)

visual = FuncAnimation(fig, animate, frames=len(sequences[0]), interval=1000)
plt.show()
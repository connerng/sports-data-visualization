from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

df = pd.read_csv('NFC West 2023-24 Points Scored Animation/pointsbyweek.csv')
teams = [
    "Arizona Cardinals",
    "Atlanta Falcons",
    "Baltimore Ravens",
    "Buffalo Bills",
    "Carolina Panthers",
    "Chicago Bears",
    "Cincinnati Bengals",
    "Cleveland Browns",
    "Dallas Cowboys",
    "Denver Broncos",
    "Detroit Lions",
    "Green Bay Packers",
    "Houston Texans", 
    "Indianapolis Colts",
    "Jacksonville Jaguars",
    "Kansas City Chiefs",
    "Las Vegas Raiders",
    "Los Angeles Chargers",
    # "Los Angeles Rams",
    # "Miami Dolphins",
    # "Minnesota Vikings",
    # "New England Patriots",
    # "New Orleans Saints",
    # "New York Giants",
    # "New York Jets",
    # "Philadelphia Eagles",
    # "Pittsburgh Steelers",
    # "San Francisco 49ers",
    # "Seattle Seahawks",
    # "Tampa Bay Buccaneers",
    # "Tennessee Titans",
    # "Washington Commanders"
]

fig = plt.figure(figsize=(10,7))
plt.style.use("seaborn-v0_8-dark")
axes = fig.add_subplot(1,1,1)
axes.set_xlim(0,500)
palette = ['black', 'black', 'purple', 'blue', 'gray', 'blue', 'orange', 'orange', 'gray', 'orange', 'blue', 'green', 
           'red', 'white', 'yellow', 'red', 'black', 'yellow']


def animate(i):
    curWeek = "Week " + str(i)
    print(curWeek)
    scores = df[curWeek].values.tolist()
    
    sorted_indices = []
    sorted_scores = sorted(scores)[:10]

    if i > 0:
        for score in sorted_scores:
            for ind in range(0, len(scores)):
                if scores[ind] == score and ind not in sorted_indices:
                    sorted_indices.append(ind)
        sorted_teams = [teams[idx] for idx in sorted_indices][:10]
        sorted_colors = [palette[idx] for idx in sorted_indices][:10]
    else:
        sorted_teams = teams[:10]
        sorted_colors = palette[:10]
    
    axes.cla()
    plt.grid(axis='x')
    plt.xlabel("Points")
    axes.set_xlim(0, 500)
    plt.barh(sorted_teams, sorted_scores, color=sorted_colors)
    plt.bar_label(plt.gca().containers[0], label_type='edge', padding=2)

    plt.title("NFC West Total Points Scored 2023-2024 | Week " + str(i))
    axes.set_xlim(0,500)

visual = FuncAnimation(fig, animate, frames=19, interval=1000)
plt.show()
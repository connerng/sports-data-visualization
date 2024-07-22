from webscraper import *
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

fig = plt.figure(figsize=(7,5))
axes = fig.add_subplot(1,1,1)
axes.set_xlim(0,500)



y1, y2, y3 = [], [], []
def animate(i):
    y1 = pts_seq[i]
    axes.cla()
    plt.barh([0], y1, color=['blue'])
    # td = {"Points":y1}
    # tcks = [i[0] for i in td]

    plt.title("Seattle Seahawks 2023-2024 Total Points by Week: {} ".format(df['Week'][i]))
    axes.set_xlim(0,500)
    plt.gca().tick_params(left=False)
    print(i, pts_seq[i])

visual = FuncAnimation(fig, animate, frames=len(pts_seq), interval=500)
plt.show()
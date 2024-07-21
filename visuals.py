from webscraper import *
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

fig = plt.figure(figsize=(7,5))
axes = fig.add_subplot(1,1,1)
axes.set_xlim(0,2000)

palette = ['red', 'yellow', 'purple']

y1, y2, y3 = [], [], []
def animate(i):
    y1 = pts_seq[i]
    y2 = reb_seq[i]
    y3 = ast_seq[i]
    plt.barh(range(3), sorted([y1, y2, y3]), color=palette)

    td = {"Points":y1, "Rebounds":y2, "Assists":y3}
    tcks = [i[0] for i in td]

    plt.title("Lebron James Rookie Season Stats by Date: {} ".format(df['Date'][i]))

visual = FuncAnimation(fig, animate, interval=100)
plt.show()
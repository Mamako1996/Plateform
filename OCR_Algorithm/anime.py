from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('Testing22.csv')
    x = data['Number']
    y1 = data['UV Transmission']
    y2 = data['IR Transmission']
    y3 = data['VL Transmission']

    plt.cla()

    plt.plot(x, y1, label='UV Transmission')
    plt.plot(x, y2, label='IR Transmission')
    plt.plot(x, y3, label='VL Transmission')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

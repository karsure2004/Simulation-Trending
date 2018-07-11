# importing required modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import random
import time
# User defined modules.
import Initglobal
import Update


class Trending(object):
    def __init__(self, ax, xmax=-30):
        self.ax = ax
        self.xmax = xmax
        self.xdata = []
        self.ydata = []
        self.line = Line2D(self.xdata, self.ydata, 1, '-', 'r')   # Xdata, ydata and line width
        self.ax.add_line(self.line)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlim(self.xmax, 0)
        ax.set_title('Trending')
        ax.set_xlabel('Time')
        ax.set_ylabel('Values')
        ax.yaxis.set_label_position('right')
        ax.yaxis.tick_right()
        ax.xaxis.tick_bottom()

    def update(self, idx):
        x = 2 * idx
        y = random.uniform(0, 1)

        if idx == 0:
            # Get the current time from the module constant
            previous_time = Initglobal.previous_time
        else:
            is_display = False

            while not is_display:
                current_time = int(time.time())
                previous_time = Update.get_value()

                if current_time >= (previous_time + 2):
                    is_display = True
                    # Update the time into the module constant
                    Update.update_value(current_time)
                else:
                    time.sleep(0.010)

        self.xdata.append(x)
        self.ydata.append(y)

        # re-assign the x axis limits
        self.ax.set_xlim((self.xmax + self.xdata[-1]), max(self.xdata))
        self.ax.figure.canvas.draw()

        self.line.set_data(self.xdata, self.ydata)
        return self.line,


fig, ax = plt.subplots()
trending = Trending(ax)

ax.set_xticklabels('')


anim = animation.FuncAnimation(fig, trending.update,
                               frames=500, interval=10, blit=True)

# show the plot
plt.show()
plt.close(1)

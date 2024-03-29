import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist


class InteractivePlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []

        self.fig.set_figheight(4.5)
        self.fig.set_figwidth(8)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.set_title("Linear Regression")

        self.regression_line, = self.ax.plot([], [], color="black", alpha=0.7, linestyle="-")

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)

    def add_new_point(self, x, y):
        if x is None or y is None:
            return
        self.xdata.append(x)
        self.ydata.append(y)
        self.ax.plot([x], [y], "oc", picker=True, pickradius=5)

        coef = np.polyfit(self.xdata, self.ydata, 1)
        poly1d = np.poly1d(coef)(self.xdata)

        self.regression_line.set_data(self.xdata, poly1d)

        self.fig.canvas.draw()

    def on_click(self, event):
        if event.button == 1:
            print("click")
            self.add_new_point(event.xdata, event.ydata)

    def on_pick(self, event):
        if event.mouseevent.button == 3:
            print("pick")
            Artist.update(event.artist, {"color": "red"})
            self.fig.canvas.draw()

    def show(self):
        plt.show()


if __name__ == "__main__":
    plot = InteractivePlot()
    plot.show()

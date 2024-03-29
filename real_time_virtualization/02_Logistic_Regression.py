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
        self.ax.set_ylim(-0.1, 1.1)

        self.main_line, = self.ax.plot([], [], "oc", picker=True, pickradius=5)
        self.regression_line, = self.ax.plot([], [], color="black", alpha=0.7, linestyle=":")

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)

    @staticmethod
    def logistic(x, x0, k, L):
        return L / (1 + np.exp(-k * (x - x0)))

    def add_new_point(self, x, y):
        self.xdata.append(x)
        self.ydata.append(round(y))

        x0 = max(int(np.sum(np.multiply(self.xdata, self.ydata)) / np.sum(self.xdata) * 100) - 13, 0)
        k = 0.21

        logic_x = np.arange(0, 100, 0.5)
        l = self.logistic(logic_x, x0, k, L=1)

        self.main_line.set_data(self.xdata, self.ydata)
        self.regression_line.set_data(logic_x, l)

        self.main_line.figure.canvas.draw()
        self.regression_line.figure.canvas.draw()

    def on_click(self, event):
        if event.button == 1:
            print("click")
            if event.inaxes != self.main_line.axes:
                return
            self.add_new_point(event.xdata, event.ydata)

    def on_pick(self, event):
        if event.mouseevent.button == 3:
            print("pick")
            Artist.update(event.artist, {"color": "red"})

    def show(self):
        plt.show()


if __name__ == "__main__":
    plot = InteractivePlot()
    plot.show()

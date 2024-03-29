import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier


class InteractivePlot:
    def __init__(self):
        centers = np.array([[-7, 6], [5, 0], [-1, 0]])
        x, y = make_blobs(n_samples=200, centers=centers, cluster_std=3)
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.knn.fit(x, y)

        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4.5)
        self.fig.set_figwidth(8)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        self.values = {0: {'x': [], 'y': [], 'color': 'm.'},
                       1: {'x': [], 'y': [], 'color': 'y.'},
                       2: {'x': [], 'y': [], 'color': 'c.'}}

        self.lines = [self.ax.plot([], [], data['color'])[0] for data in self.values.values()]

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)

    @staticmethod
    def logistic(x, x0, k, L):
        return L / (1 + np.exp(-k * (x - x0)))

    def add_new_point(self, x, y):
        score = self.knn.predict([[x, y]])[0]

        self.values[score]['x'].append(x)
        self.values[score]['y'].append(y)

        for line, data in zip(self.lines, self.values.values()):
            line.set_data(data['x'], data['y'])
            line.figure.canvas.draw()

    def on_click(self, event):
        if event.button == 1:
            print("click")
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

# TODO: Fix when NaN

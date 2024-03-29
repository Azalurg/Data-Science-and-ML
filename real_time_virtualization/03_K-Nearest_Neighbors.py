import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier


class InteractivePlot:
    def __init__(self):
        centers = np.array([[-7, 6], [5, 0], [-1, 0]])
        x, y = make_blobs(n_samples=500, centers=centers, cluster_std=5)
        self.knn = KNeighborsClassifier(n_neighbors=10)
        self.knn.fit(x, y)

        self.fig, self.ax = plt.subplots()
        self.fig.set_figheight(4.5)
        self.fig.set_figwidth(8)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_title("K-Nearest Neighbors")

        self.colors = {0: "c.", 1: "m+", 2: "y*"}

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)

    def add_new_point(self, x, y):
        if x is None or y is None:
            return
        score = self.knn.predict([[x, y]])[0]

        self.ax.plot([x], [y], self.colors[score], picker=True, pickradius=5)
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
    for i in range(100):
        plot.add_new_point(np.random.randint(-10, 10)+np.random.random(), np.random.randint(-10, 10)+np.random.random())
    plot.show()

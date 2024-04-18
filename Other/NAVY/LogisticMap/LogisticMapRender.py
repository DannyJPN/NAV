from matplotlib import pyplot as plt


class LogisticMapRender:
    def plot(self, values, x_range: tuple = (1, 4), y_range: tuple = (0, 1)):
        x, y = values
        plt.scatter(x, y, s=.01)
        plt.xlim(x_range)
        plt.ylim(y_range)
        plt.show()

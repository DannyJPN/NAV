import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap


class ForestFireRender:
    def render(self, forest_snapshots: list, iteration_count: int, animation_time: int = 20000):
        def update(i):
            forest.set_array(forest_snapshots[i])

        fig, ax = plt.subplots()
        cmap = ListedColormap(['grey', 'green', 'red'])
        forest = ax.matshow(forest_snapshots[0], cmap=cmap)
        ani = animation.FuncAnimation(fig, update, interval=animation_time / iteration_count)
        plt.show()

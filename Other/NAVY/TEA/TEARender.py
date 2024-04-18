from matplotlib import pyplot as plt
import numpy as np


class TEARender:
    def on_xlims_change(self, event_ax):
        print("updated xlims: ", event_ax.get_xlim())

    def on_ylims_change(self, event_ax):
        print("updated ylims: ", event_ax.get_ylim())

    def render(self, matrix, x_boundaries: tuple, y_boundaries: tuple):
        x_range = abs(x_boundaries[0] - x_boundaries[1])
        # abs(y_boundaries[0] - y_boundaries[1])
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.imshow(matrix, cmap="inferno", extent=[x_boundaries[0], x_boundaries[1], y_boundaries[0], y_boundaries[1]])
        # plt.imshow(matrix, cmap="inferno")
        # fig.canvas.mpl_connect('draw_event', self.on_resize)
        ax.callbacks.connect('xlim_changed', self.on_xlims_change)
        ax.callbacks.connect('ylim_changed', self.on_ylims_change)
        # plt.axis("off")
        plt.show()

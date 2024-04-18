from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


class IFSRender:
    def render(self, x, y, z):
        fig = pyplot.figure()
        ax = Axes3D(fig)
        ax.scatter(x, y, z, marker='^', color='g')
        pyplot.show()

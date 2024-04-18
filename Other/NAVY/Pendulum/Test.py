import numpy as np
import matplotlib.pyplot as plt
level = 5
resolution = 2**level
terrain_size = 32
terrain = np.zeros((resolution+1, resolution+1))
x_points = range(0, resolution+1)
y_points = range(0, resolution+1)
subdivisions = 4
for d in range(level):
    for y in range(0, resolution + 1, level - d):  # iterate throught y points  with step which is level-d
        for x in range(0, resolution + 1, level - d):  # iterate throught x points
            # menit vysku, ppokud jeste doted zmenena nebyla
            if terrain[x][y] == 0:
                l = x - level - d
                r = y - level - d
                t = x + level - d
                b = y + level - d
                if x - level - d >= 0 and y - level - d >= 0 and x + level - d <= resolution and y + level - d <= resolution:
                    average = (terrain[x - level - d][y - level - d] + terrain[x + level - d][
                        y + level - d]) / 2  # set averege from height of corner points
                else:
                    average = 0
                terrain[x][y] = average + (np.random.random() - 0.5) * (
                            level - d)  # set random height which is multiply by level-d (decreasing of perturbation)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x_points, y_points)
ax.set_zlim(-10, level*10)
ax.plot_surface(X, Y, terrain, cmap='terrain')
plt.show()
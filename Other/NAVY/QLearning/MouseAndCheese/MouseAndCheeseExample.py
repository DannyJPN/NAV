from QLearning.MouseAndCheese.MouseAndCheese import MouseAndCheese
from QLearning.MouseAndCheese.MouseAndCheeseRender import MouseAndCheeseRender
import numpy as np

# 0 = space
# 1 = mouse
# 2 = trap
# 3 = cheese

map = np.array([
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0]
])

# map = np.array([
#     [0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 2],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 3, 0],
#     [0, 0, 0, 0, 0]
# ])

qLearning = MouseAndCheese(map)
qLearning.train(5000)
path = qLearning.test()
print(path)

# print(list(zip(*np.where(map == 2))))
qGame = MouseAndCheeseRender(map)
qGame.play(path)
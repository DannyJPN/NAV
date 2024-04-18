import numpy as np

# np.array([
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0]
# ])
from HopfieldNetwork import HopfieldNetwork
from PlotUtils import PlotUtils

pattern1 = np.array([
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0]
])

pattern2 = np.array([
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]
])

pattern3 = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
])

damaged_pattern1 = np.array([
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0]
])

damaged_pattern2 = np.array([
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
])

hopfield = HopfieldNetwork(5)
hopfield.train(pattern1)
hopfield.train(pattern2)
hopfield.train(pattern3)

PlotUtils.plot_matrix(pattern1, "train pattern")
PlotUtils.plot_matrix(pattern2, "train pattern")
PlotUtils.plot_matrix(pattern3, "train pattern")

PlotUtils.plot_matrix(damaged_pattern1, "damaged pattern 1")
PlotUtils.plot_matrix(damaged_pattern2, "damaged pattern 2")
# sync
sync_predicted_pattern1 = hopfield.predict_sync(damaged_pattern1)
sync_predicted_pattern2 = hopfield.predict_sync(damaged_pattern2)
PlotUtils.plot_matrix(sync_predicted_pattern1, "sync predicted pattern 1")
PlotUtils.plot_matrix(sync_predicted_pattern2, "sync predicted pattern 2")

# async
async_predicted_pattern1 = hopfield.predict_async(damaged_pattern1)
async_predicted_pattern2 = hopfield.predict_async(damaged_pattern2)
PlotUtils.plot_matrix(async_predicted_pattern1, "async predicted pattern 1")
PlotUtils.plot_matrix(async_predicted_pattern2, "async predicted pattern 2")

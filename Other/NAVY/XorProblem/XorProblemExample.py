from PlotUtils import PlotUtils
from Utils import Utils
from XorProblem import XorProblem
import numpy as np

limits = [-30, 30]
test_set = Utils.generate_random_points(500, limits)
xorProblem = XorProblem()
xorProblem.train(1000)
result = xorProblem.test(test_set)
print(result)

PlotUtils.plot_xor_result(test_set, limits, result)
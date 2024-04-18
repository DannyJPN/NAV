from Perceptron import Perceptron
from Utils import Utils
from PlotUtils import PlotUtils


def line_function(x):
    return 4 * x - 5

limits = [-30, 30]
perceptron = Perceptron()
train_set = Utils.generate_random_points(100, limits)
test_set = Utils.generate_random_points(50, limits)
perceptron.train(train_set, line_function)
result = perceptron.test(test_set)

for point, guess in zip(test_set, result):
    print(f'{str(point)}: {guess}')

PlotUtils.plot_line(train_set, line_function, limits)
PlotUtils.plot_perceptron_result(test_set, line_function, limits, result)


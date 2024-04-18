from typing import Callable

import numpy as np

from Utils import Utils


class Perceptron:
    def __init__(self, dimension: int = 2):
        self.dimension = dimension
        self.bias = np.random.uniform()
        self.weights = np.random.uniform(size=dimension)

    def train(self, points: list, func: Callable, iteration_count: int = 1000, learning_rate: float = 0.1):
        for _ in range(iteration_count):
            changed = False
            for point in points:
                predicted_output = np.sign(np.dot(point, self.weights) + self.bias)
                is_correct = Utils.is_above_line(func(point[0]), point[1])
                if predicted_output == is_correct:
                    continue
                else:
                    error = is_correct - predicted_output
                    self.weights = self.weights + point + error * learning_rate
                    self.bias = self.bias + error * learning_rate
                    changed = True
            if not changed:
                break

    def test(self, points: list) -> dict:
        result = []
        for point in points:
            predict = np.sign(np.dot(point, self.weights) + self.bias)
            result.append(predict)
        return result

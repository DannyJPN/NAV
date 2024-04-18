import random

import numpy as np
from numpy import ndarray


class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.size = pattern_size ** 2
        self.W = np.zeros((self.size, self.size))
        pass

    def train(self, image_pattern: ndarray):
        image_pattern[image_pattern == 0] = -1
        self.W += np.outer(image_pattern, image_pattern) / self.size
        np.fill_diagonal(self.W, 0)

    def predict_sync(self, input_pattern: ndarray):
        input_pattern_shape = input_pattern.shape
        predicted_pattern = np.matmul(self.W, input_pattern.flatten())
        predicted_pattern = np.reshape(predicted_pattern, input_pattern_shape)
        predicted_pattern = np.sign(predicted_pattern)
        predicted_pattern[predicted_pattern == -1] = 0
        return predicted_pattern

    def predict_async(self, input_pattern: ndarray, repeat_count: int = 10):
        input_pattern_shape = input_pattern.shape
        # indexes = list(range(input_pattern.size))
        # random.shuffle(indexes)
        predicted_pattern = input_pattern.flatten()

        for _ in range(repeat_count):
            for i in range(input_pattern.size):
                predicted_pattern[i] = np.sign(np.matmul(self.W[i], predicted_pattern))

        predicted_pattern = np.reshape(predicted_pattern, input_pattern_shape)
        predicted_pattern[predicted_pattern == -1] = 0
        return predicted_pattern

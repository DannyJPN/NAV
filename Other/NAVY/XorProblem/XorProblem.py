import numpy as np


class XorProblem:
    def __init__(self):
        self.inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        self.target_output = np.array([[0], [1], [1], [0]])
        self.weights_H = np.random.uniform(size=(2, 2))
        self.bias_H = np.random.uniform(size=(1, 2))
        self.weights_O = np.random.uniform(size=(2, 1))
        self.bias_O = np.random.uniform(size=(1, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, iteration_count: int = 1000, learning_rate: float = 0.1):
        for _ in range(iteration_count):
            out_H = self.sigmoid(np.dot(self.inputs, self.weights_H) + self.bias_H)
            out_O = self.sigmoid(np.dot(out_H, self.weights_O) + self.bias_O)

            # error = self.target_output - out_O
            error = 0.5 * (self.target_output - out_O) ** 2
            out_O_d = error * self.sigmoid_derivative(out_O)
            error_H = np.dot(out_O_d, self.weights_O.T)
            h_d = error_H * self.sigmoid_derivative(out_H)

            self.weights_O += np.dot(out_H.T, out_O_d) * learning_rate
            self.bias_O += np.sum(out_O_d) * learning_rate
            self.weights_H += np.dot(self.inputs.T, h_d) * learning_rate
            self.bias_H += np.sum(h_d) * learning_rate

    def test(self, points):
        out_H = self.sigmoid(np.dot(points, self.weights_H) + self.bias_H)
        out_O = self.sigmoid(np.dot(out_H, self.weights_O) + self.bias_O)
        return out_O

from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray

from Utils import Utils


class PlotUtils:
    @staticmethod
    def plot_line(points: list, line: Callable, limits: list):
        x = np.linspace(-50, 50, 1000)
        y = line(x)
        plt.plot(x, y, '-r', color="green")
        plt.title("Learning")
        plt.grid()
        for point in points:
            is_above_line = Utils.is_above_line(line(point[0]), point[1])
            if is_above_line == 0:
                color = "black"
            elif is_above_line == 1:
                color = "red"
            else:
                color = "blue"
            plt.scatter(point[0], point[1], c=color)
        plt.xlim([limits[0], limits[1]])
        plt.ylim([limits[0], limits[1]])
        plt.show()

    @staticmethod
    def plot_perceptron_result(points: list, line: Callable, limits: list, prediction: list):
        x = np.linspace(-50, 50, 1000)
        y = line(x)
        plt.plot(x, y, '-r', color="green")
        plt.title("Prediction")
        plt.grid()
        for i, point in enumerate(points):
            if prediction[i] == 0:
                color = "black"
            elif prediction[i] == 1:
                color = "red"
            else:
                color = "blue"
            plt.scatter(point[0], point[1], c=color)
        plt.xlim([limits[0], limits[1]])
        plt.ylim([limits[0], limits[1]])
        plt.show()

    @staticmethod
    def plot_xor_result(points: list, limits: list, prediction: list):
        plt.title("Prediction")
        plt.grid()
        color = "blue"
        x, y = zip(*points)
        plt.scatter(x, y, c=prediction)
        plt.xlim([limits[0], limits[1]])
        plt.ylim([limits[0], limits[1]])
        plt.show()

    @staticmethod
    def plot_matrix(matrix: ndarray, title):
        fig, ax = plt.subplots()
        ax.matshow(matrix, cmap="binary")
        ax.set_title(title)
        plt.show()
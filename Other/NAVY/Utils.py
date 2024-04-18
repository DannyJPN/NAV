import numpy as np


class Utils:
    @staticmethod
    def generate_random_points(count: int, limits: list = [-50, 50], dimension: int = 2) -> list:
        return [np.random.uniform(low=limits[0], high=limits[1], size=dimension) for _ in range(count)]

    @staticmethod
    def is_above_line(y1: int, y2: int) -> int:
        if y1 == y2:
            return 0
        elif y1 < y2:
            return 1
        else:
            return -1


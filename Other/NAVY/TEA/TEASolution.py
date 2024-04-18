import numpy as np


class TEASolution:
    def iterate(self, x0: float, y0: float, limit: float, iteration_count: int) -> int:
        i = 0
        x = 0
        y = 0
        while x ** 2 + y ** 2 < limit and i < iteration_count:
            x_temp = x ** 2 - y ** 2 + x0
            y = 2 * x * y + y0
            x = x_temp
            i += 1
        return i

    def calculate(self, x_boundaries: tuple = (-2.0, 1), y_boundaries: tuple = (-1.3, 1.3),
                  size: int = 1000, iteration_count: int = 100, limit: float = 4):
        x_step = abs(x_boundaries[0] - x_boundaries[1]) / size
        y_step = abs(y_boundaries[0] - y_boundaries[1]) / size

        result = np.full((size, size), 255)
        for x in range(size):
            for y in range(size):
                x0 = x * x_step + x_boundaries[0]
                y0 = y * y_step + y_boundaries[0]

                result[y, x] = result[y, x] - self.iterate(x0, y0, limit, iteration_count)

        return result

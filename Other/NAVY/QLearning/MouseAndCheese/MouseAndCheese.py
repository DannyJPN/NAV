import numpy as np
from numpy import ndarray


class MouseAndCheese:
    SPACE = 0
    MOUSE = 1
    TRAP = 2
    CHEESE = 3

    def __init__(self, map_matrix: ndarray):
        # self.memory = np.zeros((size, size))
        self.map_matrix = map_matrix
        self.shape = (map_matrix.shape[0] ** 2, map_matrix.shape[1] ** 2)
        self.agent_memory = np.zeros(self.shape)
        self.environment = self.get_environment(map_matrix)

    def get_environment(self, map_matrix: ndarray) -> ndarray:
        def out_of_range(coords):
            return coords[0] < 0 or coords[0] >= np.size(map_matrix, axis=0) \
                   or coords[1] < 0 or coords[1] >= np.size(map_matrix, axis=1)

        environment = np.full(self.shape, -1)

        for i, row in enumerate(map_matrix):
            for j, val in enumerate(row):
                top = (i - 1, j)
                right = (i, j + 1)
                bottom = (i + 1, j)
                left = (i, j - 1)
                available_moves = [top, right, bottom, left]

                for move in available_moves:
                    x = move[0]
                    y = move[1]
                    if not out_of_range(move):
                        if map_matrix[x, y] == MouseAndCheese.SPACE:
                            environment[i * np.size(map_matrix, axis=0) + j, x * np.size(map_matrix, axis=0) + y] = 0
                        elif map_matrix[x, y] == MouseAndCheese.CHEESE:
                            environment[i * np.size(map_matrix, axis=0) + j, x * np.size(map_matrix, axis=0) + y] = 100

        return environment

    def train(self, iteration_count: int = 1000, learning_rate: float = 0.8):
        for _ in range(iteration_count):
            current_index = np.random.randint(0, np.size(self.environment, axis=0))
            current_row = self.environment[current_index]
            current_available_moves = np.argwhere(current_row >= 0).flatten()

            next_index = np.random.choice(current_available_moves)
            next_row = self.agent_memory[next_index]
            next_available_moves = next_row[next_row >= 0]
            self.agent_memory[current_index, next_index] = self.environment[current_index, next_index] + \
                                                           learning_rate * np.max(next_available_moves)

    def test(self, start_position: tuple = (0, 0)) -> list:
        path = [start_position]
        current_position = start_position
        reward_position = np.argwhere(self.map_matrix == MouseAndCheese.CHEESE).flatten()
        while not all(current_position == reward_position):
            x, y = current_position
            current_row = self.agent_memory[x * np.size(self.map_matrix, axis=0) + y]
            # current_row[x * np.size(self.map_matrix, axis=0) + y] = -1
            next_step_index = np.argmax(current_row)
            next_column = np.mod(next_step_index, np.size(self.map_matrix, axis=1))
            next_row = int((next_step_index - next_column) / np.size(self.map_matrix, axis=0))
            current_position = (next_row, next_column)
            path.append(current_position)

        return path

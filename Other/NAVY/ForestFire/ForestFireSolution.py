import copy
import random
from enum import Enum

import numpy as np


class State(Enum):
    Empty = 0
    Tree = 1
    Fire = 2


class ForestFireSolution:

    def calculate(self, iteration_count: int = 500, forest_shape: tuple = (100, 100),
                  p_grow: float = 0.007, p_burn: float = 0.0001) -> list:
        forest = np.array([
            np.random.choice([State.Empty.value, State.Tree.value], size=forest_shape[0], p=[0.4, 0.6])
            for _ in range(forest_shape[1])
        ])
        forest[0, 0] = State.Fire.value

        forest_snapshots = []

        for i in range(iteration_count):
            forest_snapshots.append(forest)
            original_forest = forest
            forest = copy.deepcopy(forest)

            for x in range(forest_shape[0]):
                for y in range(forest_shape[1]):
                    rnd = random.uniform(0, 1)

                    if original_forest[x, y] == State.Empty.value and rnd < p_grow:  # grow
                        forest[x, y] = State.Tree.value
                    elif original_forest[x, y] == State.Tree.value:
                        if x != 0 and original_forest[x - 1, y] == State.Fire.value:  # burn
                            forest[x, y] = State.Fire.value
                        elif x != forest_shape[0] - 1 and original_forest[x + 1, y] == State.Fire.value:
                            forest[x, y] = State.Fire.value
                        elif y != 0 and original_forest[x, y - 1] == State.Fire.value:
                            forest[x, y] = State.Fire.value
                        elif y != forest_shape[1] - 1 and original_forest[x, y + 1] == State.Fire.value:
                            forest[x, y] = State.Fire.value
                        elif rnd < p_burn:
                            forest[x, y] = State.Fire.value
                    elif original_forest[x, y] == State.Fire.value:  # clear
                        forest[x, y] = State.Empty.value
        return forest_snapshots

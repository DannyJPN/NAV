import random

import numpy as np


class LogisticMapSolution:
    def get_population_ratio(self, generation: int, grow_rate: float, initial_population_rate: float) -> float:
        population_rate = initial_population_rate
        for i in range(generation):
            population_rate = population_rate * grow_rate * (1 - population_rate)
        return population_rate

    def calculate(self, growth_rate_range: tuple = (0, 4), step: float = 0.00001,
                  generation_count: int = 100, generation_deviation: int = 10,
                  initial_population_rate: float = 0.5) -> tuple:
        growth_rates = np.arange(growth_rate_range[0], growth_rate_range[1], step)
        print(max(growth_rates))
        grow_rates = []
        population_rates = []

        for grow_rate in growth_rates:
            generation = random.randint(generation_count - generation_deviation,
                                        generation_count + generation_deviation)
            population_rate = self.get_population_ratio(generation, grow_rate, initial_population_rate)
            grow_rates.append(grow_rate)
            population_rates.append(population_rate)

        return grow_rates, population_rates

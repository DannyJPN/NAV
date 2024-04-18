import random

from IFS.IFSRule import IFSRule


class IFSSolution:
    def __init__(self):
        pass

    def get_rule(self, rules) -> IFSRule:
        r = random.random()
        for rule in rules:
            if r < rule.p:
                return rule

    def perform(self, rules: list, iteration_count: int = 10000) -> tuple:
        x = 0
        y = 0
        z = 0
        x_coords = []
        y_coords = []
        z_coords = []

        for i in range(iteration_count):
            rule = self.get_rule(rules)
            evaluation = rule.evaluate(x, y, z)
            x, y, z = evaluation.flatten()
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)

        return x_coords, y_coords, z_coords

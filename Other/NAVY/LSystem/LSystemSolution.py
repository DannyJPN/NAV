from LSystem.LSystemModel import LSystemModel


class LSystemSolution:
    def __init__(self):
        pass

    def calculate(self, iteration_count: int, model: LSystemModel):
        s = model.axiom
        for i in range(iteration_count):
            new = ""
            for char in s:
                new = new + (model.rule if char == 'F' else char)
            s = new

        model.instructions = s

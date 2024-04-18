import string


class LSystemModel:
    def __init__(self, axiom: string, rule: string, angle: float, distance: float = 5, start_pos: tuple = (0, 0)):
        self.axiom = axiom
        self.rule = rule
        self.angle = angle
        self.distance = distance
        self.start_pos = start_pos
        self.instructions = None

from LSystem.LSystemModel import LSystemModel
from LSystem.LSystemRender import LSystemRender
from LSystem.LSystemSolution import LSystemSolution
import math


l_system = LSystemSolution()
l_system_render = LSystemRender(False)


# model = LSystemModel("F+F+F+F", "F+F-F-FF+F+F-F", 60, 1)
# l_system.calculate(3, model)
# l_system_render.render(model)
#
# model = LSystemModel("F++F++F", "F+F--F+F", 60, 5)
# l_system.calculate(4, model)
# l_system_render.render(model)

# model = LSystemModel("F", "FF+[+F-F-F]-[-F+F+F]", math.degrees(math.pi / 8), 15, (-500, 0))
# l_system.calculate(4, model)
# print(model.instructions)
# l_system_render.render(model)
#
# model = LSystemModel("F+F+F+F", "FF+F+F+F+FF", 90, 5, (-300, 300))
# l_system.calculate(4, model)
# l_system_render.render(model)
#
# model = LSystemModel("F++F++F++F", "-F++F-", 45, 5, (-400, 200))
# l_system.calculate(12, model)
# l_system_render.render(model)
#
# model = LSystemModel("F++F++F+++F--F--F", "FF++F++F++FFF", 60, 3, (-400, 200))
# l_system.calculate(4, model)
# l_system_render.render(model)
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pendulum.PendulumRender import PendulumRender
from Pendulum.PendulumSolution import PendulumSolution
import numpy as np

time_step = 0.01

render = PendulumRender()
solution = PendulumSolution()
result = solution.calculate(2 * np.pi / 6, 5 * np.pi / 8, 30, time_step)
render.render(time_step, *result)

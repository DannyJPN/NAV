import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TEA.TEARender import TEARender
from TEA.TEASolution import TEASolution

solution = TEASolution()
render = TEARender()

extent1 = [(-2.0, 1), (-1.3, 1.3)]
extent2 = [(-0.22, -0.219), (-0.7, -0.699)]
extent3 = [(-0.745431, -0.745426), (0.113006, 0.113012)]

result1 = solution.calculate(extent1[0], extent1[1], 500, 30)
result2 = solution.calculate(extent2[0], extent2[1], 300, 100)
result3 = solution.calculate(extent3[0], extent3[1], 300, 500)

# result1 = solution.calculate(extent1[0], extent1[1], 1000, 100)
# result2 = solution.calculate(extent2[0], extent2[1], 1000, 200)
# result3 = solution.calculate(extent3[0], extent3[1], 1000, 700)

render.render(result1, extent1[0], extent1[1])
render.render(result2, extent2[0], extent2[1])
render.render(result3, extent3[0], extent3[1])

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LogisticMap.LogisticMapRender import LogisticMapRender
from LogisticMap.LogisticMapSolution import LogisticMapSolution

solution = LogisticMapSolution()
render = LogisticMapRender()

growth_rate_range = (0, 4)
result = solution.calculate(growth_rate_range)
render.plot(result, growth_rate_range)

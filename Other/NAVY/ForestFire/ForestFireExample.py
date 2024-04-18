import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ForestFire.ForestFireRender import ForestFireRender
from ForestFire.ForestFireSolution import ForestFireSolution

render = ForestFireRender()
solution = ForestFireSolution()

iteration_count = 500
forest_snapshots = solution.calculate(iteration_count)
render.render(forest_snapshots, iteration_count)

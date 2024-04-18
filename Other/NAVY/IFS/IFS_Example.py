import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from IFS.IFSRender import IFSRender
from IFS.IFSRule import IFSRule
from IFS.IFSSolution import IFSSolution

render = IFSRender()
solution = IFSSolution()

model1 = [
    IFSRule(0.00, 0.00, 0.01, 0.00, 0.26, 0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.25),
    IFSRule(0.20, -0.26, -0.01, 0.23, 0.22, -0.07, 0.07, 0.00, 0.24, 0.00, 0.80, 0.00, 0.5),
    IFSRule(-0.25, 0.28, 0.01, 0.26, 0.24, -0.07, 0.07, 0.00, 0.24, 0.00, 0.22, 0.00, 0.75),
    IFSRule(0.85, 0.04, -0.01, -0.04, 0.85, 0.09, 0.00, 0.08, 0.84, 0.00, 0.80, 0.00, 1)
]

model2 = [
    IFSRule(0.05, 0.00, 0.00, 0.00, 0.60, 0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.25),
    IFSRule(0.45, -0.22, 0.22, 0.22, 0.45, 0.22, -0.22, 0.22, -0.45, 0.00, 1.00, 0.00, 0.5),
    IFSRule(-0.45, 0.22, -0.22, 0.22, 0.45, 0.22, 0.22, -0.22, 0.45, 0.00, 1.25, 0.00, 0.75),
    IFSRule(0.49, -0.08, 0.08, 0.08, 0.49, 0.08, 0.08, -0.08, 0.49, 0.00, 2.00, 0.00, 1)
]

result1 = solution.perform(model1, 20000)
render.render(*result1)

result2 = solution.perform(model2, 10000)
render.render(*result2)

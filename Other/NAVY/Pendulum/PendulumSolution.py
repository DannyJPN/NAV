import numpy as np
from scipy import integrate


class PendulumSolution:

    def calculate(self, start_angle1: float, start_angle2: float,
                  t_max: float = 30, time_step: float = 0.01,
                  m1: float = 4, m2: float = 1,
                  l1: float = 1, l2: float = 2,
                  g: float = 9.81):
        time_steps = np.arange(0, t_max, time_step)

        def get_derivate(params, t):
            theta1, z1, theta2, z2 = params
            c = np.cos(theta1 - theta2)
            s = np.sin(theta1 - theta2)
            angle1 = z1
            new_z1 = (m2 * g * np.sin(theta2) * c - m2 * s * (l1 * z1 ** 2 * c + l2 * z2 ** 2)
                      - (m1 + m2) * g * np.sin(theta1)) / l1 / (m1 + m2 * s ** 2)
            angle2 = z2
            new_z2 = ((m1 + m2) * (l1 * z1 ** 2 * s - g * np.sin(theta2) + g * np.sin(
                theta1) * c) + m2 * l2 * z2 ** 2 * s * c) / l2 / (
                             m1 + m2 * s ** 2)
            return angle1, new_z1, angle2, new_z2

        res = integrate.odeint(get_derivate, [start_angle1, 0, start_angle2, 0], time_steps)
        x1 = l1 * np.sin(res[:, 0])
        x2 = x1 + l2 * np.sin(res[:, 2])
        y1 = -l1 * np.cos(res[:, 0])
        y2 = y1 + -l2 * np.cos(res[:, 2])

        return x1, x2, y1, y2

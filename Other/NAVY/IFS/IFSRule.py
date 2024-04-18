import numpy as np


class IFSRule:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, p):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.p = p
        self.matrix1 = np.array([
            [a, b, c],
            [d, e, f],
            [g, h, i]
        ])
        self.matrix2 = np.array([
            [j],
            [k],
            [l]
        ])

    def evaluate(self, x, y, z):
        matrix3 = np.array([
            [x],
            [y],
            [z]
        ])

        return np.matmul(self.matrix1, matrix3) + self.matrix2

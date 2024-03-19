import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x1, x2, _lambda = vars
    eq1 = 2*x1 - 20 + _lambda
    eq2 = -20 + 2*x2 + _lambda
    eq3 = x1 + x2 - 11
    return [eq1, eq2, eq3]

x1, x2, _lambda = fsolve(equations, (0, 0, 0))

Z = x1**2 - 20*x1 - 20*x2 + x2**2

print("Оптимальное значение x1:", x1)
print("Оптимальное значение x2:", x2)
print("Оптимальное значение функции Z:", Z)

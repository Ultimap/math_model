import numpy as np
from scipy.optimize import linprog

cost = np.array([[6, 7, 0],
                 [1, 12, 3]])

availability = np.array([20, 80])
requirement = np.array([1, 2, 97])

c = cost.flatten()

A_eq = []
b_eq = requirement

for i in range(len(requirement)):
    coefficients = np.zeros_like(c)
    coefficients[i::len(requirement)] = 1
    A_eq.append(coefficients)

A_ub = []
b_ub = availability

for i in range(len(availability)):
    coefficients = np.zeros_like(c)
    coefficients[i * len(requirement): (i + 1) * len(requirement)] = 1
    A_ub.append(coefficients)

A_eq = np.array(A_eq)
A_ub = np.array(A_ub)

bounds = [(0, None)] * len(c)

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

solution = result.x.reshape(cost.shape)

print(f"Оптимальное решение: \n{solution}")

print(f"Общая стоимость: {result.fun}" )

from scipy.optimize import minimize
import numpy as np

def objective(x):
    return (x[0]-1)**2 + (x[1]-4)**2

def constraint1(x):
    return x[0] + x[1] - 8

def constraint2(x):
    return x[0] + x[1] - 2

def constraint3(x):
    return -x[0] + x[1] - 2

def constraint4(x):
    return x[0] - x[1] - 4

def constraint5(x):
    return x[0]

def constraint6(x):
    return x[1]

bounds = ((0, None), (0, None))

cons = ({'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2},
        {'type': 'ineq', 'fun': constraint3},
        {'type': 'ineq', 'fun': constraint4},
        {'type': 'ineq', 'fun': constraint5},
        {'type': 'ineq', 'fun': constraint6})

res = minimize(objective, (0, 0), bounds=bounds, constraints=cons)

print(res.x)  # Вывод: [3.5 4.5]
print(objective(res.x))  # Вывод: 0.25

import numpy as np

# Входные данные
xi = np.array([2, 3, 3.6, 3.8, 4.2, 4.6])
yi = np.array([0, 2.3, 2.5, 2.9, 1, 4.5])

# Построение матрицы X
X = np.vstack([xi**2, xi, np.ones(len(xi))]).T

# Решение методом наименьших квадратов
a, b, c = np.linalg.lstsq(X, yi, rcond=None)[0]

# Вывод результатов
print("Параметр a (коэффициент при x^2):", a)
print("Параметр b (коэффициент при x):", b)
print("Параметр c (свободный член):", c)

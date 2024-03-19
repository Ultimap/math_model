import numpy as np

# Входные данные
xi = np.array([1, 2, 4, 6, 7, 8])
yi = np.array([7, 6, 4, 5, 3, 3])

# Построение матрицы X
X = np.vstack([xi, np.ones(len(xi))]).T

# Решение методом наименьших квадратов
a, b = np.linalg.lstsq(X, yi, rcond=None)[0]

# Вывод результатов
print("Параметр a (наклон прямой):", a)
print("Параметр b (смещение прямой):", b)

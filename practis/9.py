import numpy as np

# Время восстановления (в секундах)
x_ti = np.array([1, 2, 3, 4, 5, 6, 7])

# Пропускная способность (в байтах в секунду)
y_ti = np.array([11250000, 10750000, 10000000, 10625000, 11000000, 10000000, 9500000])

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x_ti, y_ti, marker='o', linestyle='-', color='b')
plt.title('Зависимость пропускной способности от времени восстановления')
plt.xlabel('Время восстановления (с)')
plt.ylabel('Пропускная способность (байт/с)')
plt.grid(True)
plt.show()

from scipy.optimize import curve_fit

# Определение квадратичной функции
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Обучение модели (подгонка кривой)
popt, pcov = curve_fit(quadratic_function, x_ti, y_ti)

# Получение оптимальных параметров
a_opt, b_opt, c_opt = popt

print("Оптимальные параметры модели:")
print("a =", a_opt)
print("b =", b_opt)
print("c =", c_opt)

# Новые значения времени восстановления для прогноза
x_new = np.linspace(0, 8, 100)

# Прогнозирование пропускной способности
y_new = quadratic_function(x_new, a_opt, b_opt, c_opt)

# Визуализация прогноза
plt.figure(figsize=(10, 6))
plt.plot(x_ti, y_ti, marker='o', linestyle='-', color='b', label='Данные')
plt.plot(x_new, y_new, linestyle='--', color='r', label='Прогноз')
plt.title('Прогноз пропускной способности')
plt.xlabel('Время восстановления (с)')
plt.ylabel('Пропускная способность (байт/с)')
plt.legend()
plt.grid(True)
plt.show()

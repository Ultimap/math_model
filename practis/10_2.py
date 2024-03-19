import numpy as np
import matplotlib.pyplot as plt

# Функция полезности (в примере - квадратичная функция)
def utility_function(x):
    return -0.5 * (x - 10) ** 2 + 100

# Создаем массив значений для аргументов функции
x_values = np.linspace(0, 20, 100)

# Вычисляем значения функции полезности для каждого значения аргумента
y_values = utility_function(x_values)

# Строим график функции полезности
plt.plot(x_values, y_values, label='Utility Function')

# Строим нейтральную прямую (прямая равновесия)
neutral_line = np.linspace(0, 20, 100)
plt.plot(neutral_line, neutral_line, linestyle='--', color='gray', label='Neutral Line')

# Добавляем подписи осей и легенду
plt.xlabel('Money')
plt.ylabel('Utility')
plt.legend()

# Отображаем график
plt.title('Utility Function and Neutral Line')
plt.grid(True)
plt.show()

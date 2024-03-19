import numpy as np

# Метод аналитического решения для матричной игры 2x2
def solve_2x2_matrix_game(matrix):
    # Находим оптимальную стратегию для игрока A
    p_opt_A = (matrix[1, 1] - matrix[1, 0]) / (matrix[0, 0] + matrix[1, 1] - matrix[0, 1] - matrix[1, 0])
    
    # Находим оптимальную стратегию для игрока B
    p_opt_B = (matrix[0, 0] - matrix[0, 1]) / (matrix[0, 0] + matrix[1, 1] - matrix[0, 1] - matrix[1, 0])
    
    # Находим оптимальное значение игры
    game_value = 1 / (matrix[0, 0] + matrix[1, 1] - matrix[0, 1] - matrix[1, 0])
    
    return p_opt_A, p_opt_B, game_value

# Пример использования для матричной игры 2x2
matrix_2x2 = np.array([[4, 3], [2, 6]])
p_opt_A, p_opt_B, game_value = solve_2x2_matrix_game(matrix_2x2)
print("Оптимальная стратегия игрока A:", p_opt_A)
print("Оптимальная стратегия игрока B:", p_opt_B)
print("Оптимальное значение игры:", game_value)

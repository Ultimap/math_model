import numpy as np
# Метод итераций Робинсона-Брауна для матричной игры 3x3
def solve_3x3_matrix_game(matrix, tol=1e-6, max_iter=1000):
    m, n = matrix.shape
    p = np.ones(m) / m  # начальная смешанная стратегия первого игрока
    q = np.ones(n) / n  # начальная смешанная стратегия второго игрока

    for _ in range(max_iter):
        q_new = matrix.T.dot(p)  # вычисляем новую смешанную стратегию второго игрока
        p_new = matrix.dot(q_new)  # вычисляем новую смешанную стратегию первого игрока

        # нормализуем смешанные стратегии
        p_new /= p_new.sum()
        q_new /= q_new.sum()

        # проверяем насколько изменились смешанные стратегии
        if np.linalg.norm(p_new - p) < tol and np.linalg.norm(q_new - q) < tol:
            break

        p = p_new
        q = q_new
    game_value = p.dot(matrix.dot(q))
    return p, q, game_value

# Пример использования для матричной игры 3x3
matrix_3x3 = np.array([[4, 1, 1], [7, 0, 5], [4, 8, 8]])
p_opt, q_opt, game_value = solve_3x3_matrix_game(matrix_3x3)
print("Оптимальная смешанная стратегия первого игрока:", p_opt)
print("Оптимальная смешанная стратегия второго игрока:", q_opt)
print("Оптимальное значение игры:", game_value)

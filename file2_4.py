import numpy as np
import matplotlib.pyplot as plt

def random_matrix_stats(m, n):
    matrix = np.random.randn(m, n)

    # Подсчет математического ожидания и дисперсии по строкам и столбцам
    row_means = np.mean(matrix, axis=1)  # Среднее по строкам
    row_vars = np.var(matrix, axis=1)    # Дисперсия по строкам

    col_means = np.mean(matrix, axis=0)  # Среднее по столбцам
    col_vars = np.var(matrix, axis=0)    # Дисперсия по столбцам

    print("Мат. ожидание по строкам:", row_means)
    print("Дисперсия по строкам:", row_vars)
    print("Мат. ожидание по столбцам:", col_means)
    print("Дисперсия по столбцам:", col_vars)

    # Построение гистограмм для каждой строки
    for i in range(m):
        plt.figure(figsize=(6, 4))
        plt.hist(matrix[i, :], bins=10, color='blue', alpha=0.7)
        plt.title(f'Гистограмма строки {i+1}')
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.show()

    # Построение гистограмм для каждого столбца
    for j in range(n):
        plt.figure(figsize=(6, 4))
        plt.hist(matrix[:, j], bins=10, color='green', alpha=0.7)
        plt.title(f'Гистограмма столбца {j+1}')
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.show()

random_matrix_stats(3, 4)

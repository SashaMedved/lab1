import numpy as np

def unique_in_rows(matrix):
    return [list(set(row)) for row in matrix]

matrix = np.array([[1, 2, 2],
                   [3, 3, 4],
                   [5, 5, 5]])

result_rows = unique_in_rows(matrix)
print(f"Уникальные элементы в строках: {result_rows}")


def unique_in_columns(matrix):
    # Транспонируем матрицу и применяем тот же метод, что и для строк
    return [list(set(col)) for col in matrix.T]

result_columns = unique_in_columns(matrix)
print(f"Уникальные элементы в столбцах: {result_columns}")

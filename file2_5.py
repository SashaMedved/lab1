import numpy as np

def chessboard_matrix(m, n, a, b):
    matrix = np.zeros((m, n))
    
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i, j] = a  # Если сумма индексов четная, ставим a
            else:
                matrix[i, j] = b  # Если сумма индексов нечетная, ставим b
    
    return matrix

m = 4
n = 5
a = 1
b = 0

result = chessboard_matrix(m, n, a, b)
print(f"Шахматная матрица размером {m}x{n} с числами {a} и {b}:\n{result}")

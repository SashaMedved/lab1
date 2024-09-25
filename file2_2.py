import numpy as np

def binarize_matrix(M, threshold):
    binary_matrix = np.where(M >= threshold, 1, 0)
    return binary_matrix

M = np.array([[1, 5, 7],
              [2, 8, 3],
              [6, 9, 4]])

threshold = 5
result = binarize_matrix(M, threshold)
print(f"Бинаризованная матрица при threshold {threshold}:\n{result}")

import numpy as np

def matrix_vector_sum(matrices, vectors):
    n = len(vectors[0])
    total_sum = np.zeros((n, 1))
    
    # Перебираем каждую матрицу и соответствующий вектор
    for matrix, vector in zip(matrices, vectors):
        total_sum += np.dot(matrix, vector)
    
    return total_sum

matrices = [
    np.array([[1, 2], [3, 4]]),
    np.array([[5, 6], [7, 8]])
]

vectors = [
    np.array([[1], [2]]),
    np.array([[3], [4]])
]

result = matrix_vector_sum(matrices, vectors)
print(f"Сумма произведений матриц на векторы: \n{result}")
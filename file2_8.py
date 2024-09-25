import numpy as np

def one_hot_encoding(labels):
    # Определяем количество уникальных классов
    num_classes = np.max(labels) + 1
    
    # Создаем матрицу для one-hot encoding
    one_hot_matrix = np.zeros((len(labels), num_classes))
    
    # Заполняем 1 в нужных позициях
    for i, label in enumerate(labels):
        one_hot_matrix[i, label] = 1
    
    return one_hot_matrix

labels = [0, 2, 3, 0]
one_hot_encoded = one_hot_encoding(labels)
print(one_hot_encoded)

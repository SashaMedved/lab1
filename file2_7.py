import numpy as np
from scipy.signal import find_peaks

def time_series_analysis(series, p):
    mean_value = np.mean(series)
    variance = np.var(series)
    std_dev = np.std(series)
    
    # 4. Нахождение локальных максимумов и минимумов
    local_maxima = find_peaks(series)[0]  # Индексы локальных максимумов
    local_minima = find_peaks(-series)[0]  # Индексы локальных минимумов (инвертируем ряд)

    # 5. Метод скользящего среднего
    def moving_average(arr, window_size):
        return np.convolve(arr, np.ones(window_size)/window_size, mode='valid')

    smoothed_series = moving_average(series, p)

    print(f"Математическое ожидание: {mean_value}")
    print(f"Дисперсия: {variance}")
    print(f"Стандартное отклонение: {std_dev}")
    print(f"Локальные максимумы (индексы): {local_maxima}")
    print(f"Локальные минимумы (индексы): {local_minima}")
    print(f"Ряд после скользящего среднего (окно {p}): {smoothed_series}")
    
    return mean_value, variance, std_dev, local_maxima, local_minima, smoothed_series

time_series = [1, 3, 7, 1, 2, 6, 0, 1, 4, 5, 3, 2, 6, 8, 7, 9, 3]
p = 3
time_series_analysis(time_series, p)
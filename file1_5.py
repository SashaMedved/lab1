import math

def dispersion_vector(v1, v2):
	sum = 0
	lenght = len(v1)
	for i in range(lenght):
		sum += (v1[i] - v2[i])**2
	return math.sqrt(sum/lenght)

v1 = [1, 2, 3]
v2 = [1, 4, 9]
result = dispersion_vector(v1, v2)
print(f"Среднеквадратическое отклонение: {result}")



def test_dispersion_vector():
    # Тест 1: Векторы одинаковы, отклонение 0
    assert dispersion_vector([1, 2, 3], [1, 2, 3]) == 0, "Тест 1 не прошел"
    
    # Тест 2: Векторы с разным набором значений
    assert round(dispersion_vector([1, 2, 3], [4, 5, 6]), 6) == round(math.sqrt(9), 6), "Тест 2 не прошел"
    
    # Тест 3: Одноразличные векторы
    assert round(dispersion_vector([10, 20, 30], [10, 25, 30]), 6) == round(math.sqrt(25 / 3), 6), "Тест 3 не прошел"
    
    # Тест 4: Один вектор содержит нули
    assert dispersion_vector([0, 0, 0], [1, 1, 1]) == 1, "Тест 4 не прошел"
    
    # Тест 5: Длинные векторы с одинаковыми элементами
    assert dispersion_vector([100]*1000, [100]*1000) == 0, "Тест 5 не прошел"

    print("Все тесты прошли успешно!")

test_dispersion_vector()
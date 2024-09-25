def pyramid(n):
	result = 0
	count = 1
	index = 0
	while result < n:
		result += count**2
		count += 1
		index = count - 1
	if result == n:
		return index
	else:
		return "It is impossible"

n = 14
result = pyramid(n)
print(f"Результат для {n}: {result}")



def test_pyramid():
    # Тест 1: n = 14 (1^2 + 2^2 + 3^2 = 14, ответ должен быть 3)
    assert pyramid(14) == 3, "Тест 1 не прошел"
    
    # Тест 2: n = 5 (не существует пирамиды для 5, должно быть 'It is impossible')
    assert pyramid(5) == "It is impossible", "Тест 2 не прошел"
    
    # Тест 3: n = 30 (1^2 + 2^2 + 3^2 + 4^2 = 30, ответ должен быть 4)
    assert pyramid(30) == 4, "Тест 3 не прошел"
    
    # Тест 4: n = 1 (1^2 = 1, ответ должен быть 1)
    assert pyramid(1) == 1, "Тест 4 не прошел"

    print("Все тесты прошли успешно!")


test_pyramid()
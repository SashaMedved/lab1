def is_unique(str):
	words = set()
	for char in str:
		if char n words:
			return False
		words.add(char)
	return True

input_string = "abcdef"
result = is_unique(input_string)
print(f"Все символы уникальны: {result}")



def test_is_unique():
    # Тест 1: Строка с уникальными символами
    assert is_unique("abcdef") == True, "Тест 1 не прошел"
    
    # Тест 2: Строка с повторяющимися символами
    assert is_unique("aabbcc") == False, "Тест 2 не прошел"
    
    # Тест 3: Пустая строка
    assert is_unique("") == True, "Тест 3 не прошел"
    
    # Тест 4: Строка с одним символом
    assert is_unique("a") == True, "Тест 4 не прошел"
    
    # Тест 5: Строка с уникальными символами в верхнем и нижнем регистре
    assert is_unique("AaBbCc") == True, "Тест 5 не прошел"
    
    # Тест 6: Строка с повторяющимся символом в разных регистрах
    assert is_unique("abcABC") == True, "Тест 6 не прошел"
    
    # Тест 7: Строка с пробелами
    assert is_unique("a b c") == True, "Тест 7 не прошел"
    
    print("Все тесты прошли успешно!")

test_is_unique()
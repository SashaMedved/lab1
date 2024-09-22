def count_vowels(str):
	vowels = "aeiouAeiou"
	count = 0
    
        for char in string:
                if char in vowels:          
                	count += 1
    
    return count

input_string = "Hello World"
result = count_vowels(input_string)

print(f"Количество гласных в строке '{input_string}': {result}")


def test_count_vowels():
    # Тест 1: Строка с гласными и согласными
    assert count_vowels("Hello World") == 3, "Тест 1 не прошел"
    
    # Тест 2: Строка без гласных
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0, "Тест 2 не прошел"
    
    # Тест 3: Строка только с гласными
    assert count_vowels("aeiou") == 5, "Тест 3 не прошел"
    
    # Тест 4: Пустая строка
    assert count_vowels("") == 0, "Тест 4 не прошел"
    
    # Тест 5: Строка с гласными в верхнем регистре
    assert count_vowels("AEIOU") == 5, "Тест 5 не прошел"
    
    # Тест 6: Строка с повторяющимися гласными
    assert count_vowels("aaaeeeiii") == 9, "Тест 6 не прошел"
    
    print("Все тесты прошли успешно!")

test_count_vowels()
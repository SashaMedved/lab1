def multiplication(n):
    count = 0
    while n >= 10:
        result = 1
        while n > 0:
            result *= n % 10
            n //= 10
        n = result
        count += 1
    return count

number = int(input("Введите число: "))
result = multiplication(number)
print(f"Количество шагов для числа {number}: {result}")


def test_multiplication():
    # Тест 1: Число 39 (результат 3)
    assert multiplication(39) == 3, "Тест 1 не прошел"
    
    # Тест 2: Число 4 (результат 0)
    assert multiplication(4) == 0, "Тест 2 не прошел"
    
    # Тест 3: Число 999 (результат 4)
    assert multiplication(999) == 4, "Тест 3 не прошел"
    
    # Тест 4: Число 25 (результат 2: 25=10 => 10=0)
    assert multiplication(25) == 2, "Тест 4 не прошел"
    
    # Тест 5: Число 10 (результат 1: 10=0)
    assert multiplication(10) == 1, "Тест 5 не прошел"
    
    # Тест 6: Число 1 (результат 0, так как это уже одна цифра)
    assert multiplication(1) == 0, "Тест 6 не прошел"
    
    print("Все тесты прошли успешно!")

test_multiplication()

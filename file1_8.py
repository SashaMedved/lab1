def is_balanced(n):
    digits = str(n)
    length = len(digits)
    
    # Если длина четная, исключаем две средние цифры
    if length % 2 == 0:
        left = digits[:length // 2 - 1]
        right = digits[length // 2 + 1:]
    # Если длина нечетная, исключаем одну среднюю цифру
    else:
        left = digits[:length // 2]
        right = digits[length // 2 + 1:]
    
    left_sum = sum(int(x) for x in left)
    right_sum = sum(int(x) for x in right)
    
    return left_sum == right_sum

n = 123321
result = is_balanced(n)
print(f"Число {n} сбалансировано: {result}")



def test_is_balanced():
    # Тест 1: Четное число длиной 6, сумма до и после средних равна
    assert is_balanced(123321) == True, "Тест 1 не прошел"
    
    # Тест 2: Нечетное число длиной 5, сумма до и после средней не равна
    assert is_balanced(12345) == False, "Тест 2 не прошел"
    
    # Тест 6: Одноразрядное число (считается сбалансированным)
    assert is_balanced(5) == True, "Тест 6 не прошел"
    
    print("Все тесты прошли успешно!")

test_is_balanced()

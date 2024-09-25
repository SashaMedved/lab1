def prime_factorization(n):
    factors = {}
    # Проверяем деление на 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    
    # Проверяем деление на нечетные числа начиная с 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors[factor] = factors.get(factor, 0) + 1
            n //= factor
        factor += 2
    
    # Если после цикла n больше 2, то это простое число
    if n > 2:
        factors[n] = 1
    
    # Формируем строку результата
    result = ""
    for prime, power in sorted(factors.items()):
        if power == 1:
            result += f"({prime})"
        else:
            result += f"({prime}**{power})"
    
    return result

n = 86240
result = prime_factorization(n)
print(f"Разложение числа {n} на простые множители: {result}")



def test_prime_factorization():
    # Тест 1: Число 86240
    assert prime_factorization(86240) == "(2**5)(5)(7**2)(11)", "Тест 1 не прошел"
    
    # Тест 2: Простое число 13 (разложение должно быть просто (13))
    assert prime_factorization(13) == "(13)", "Тест 2 не прошел"
    
    # Тест 3: Число 100 (два простых множителя 2 и 5)
    assert prime_factorization(100) == "(2**2)(5**2)", "Тест 3 не прошел"
    
    # Тест 4: Число 1 (для 1 разложение отсутствует, функция может возвращать пустую строку)
    assert prime_factorization(1) == "", "Тест 4 не прошел"
    
    # Тест 5: Число 360 (разложение 2**3 * 3**2 * 5)
    assert prime_factorization(360) == "(2**3)(3**2)(5)", "Тест 5 не прошел"  
    
    print("Все тесты прошли успешно!")

test_prime_factorization()


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
import random


# без рекурсии
def prime(number: int) -> bool:
    if number in [1, 2]:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, number ** 0.5 + 1, 2):
# диапазон от 3, так как 1,2 проверили,
# убираем половину делителей(так как число не делится нацело если делитель больше половины числа, с шагом 2 (пропускаем чётные делители)
            if number % i == 0:
                return False
    return True


# с рекурсией

def prime_recursion(number, div):
    if div == number // 2 + 1:
        return True
    elif number % div == 0:
        return False
    else:
        return prime_recursion(number, div + 1)


number = int(input('Введите число: '))
print(f'Число {number} - ' + ('простое' if prime(number) else 'составное'))
print(f'Число {number} - ' + ('простое' if prime_recursion(number, 2) else 'составное'))

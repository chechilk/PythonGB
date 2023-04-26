def search_summ(first_number: int, second_number: int) -> int:
    while second_number > 0:
        return search_summ(first_number + 1, second_number - 1)
    return first_number


first_number, second_number = map(int, input('Введите 2 числа через пробел: ').split())
print(f'Сумма чисел {first_number} + {second_number} = {search_summ(first_number, second_number)}')

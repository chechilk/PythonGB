def result_func(number: int, degree_for_number: int, result=1) -> int:
    if degree_for_number != 0:
        result *= number
        return result_func(number, degree_for_number - 1, result)
    else:
        return result


numbers, degree_for_number = map(int, input('Введите числа через пробел в одну строчку (число/степень): ').split())
print(f'{numbers} в {degree_for_number} степени = {result_func(numbers, degree_for_number)}')

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def func(number: int, str_number=' ') -> str:
    if number != 0:
        str_number += str(number) + ' '
        return func(number - 1, str_number)
    else:
        return str_number

number = int(input("Введите число: "))
print(func(number))

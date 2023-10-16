'''Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.'''

number = int(input('Введите число: '))
first_number_fub = 0
second_number_fib = 1
number_fib = 0
count_number = 1

while number_fib <= number:
    number_fib = first_number_fub + second_number_fib
    first_number_fub = second_number_fib
    second_number_fib = number_fib
    count_number += 1
    if (number == number_fib):
        print(count_number + 1)
        exit()

print(-1)

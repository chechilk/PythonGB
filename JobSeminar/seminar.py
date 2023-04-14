'''По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1

number = int(input('Введите число: '))

fact = 1
i = 1
while i <= number:
    fact *= i
    i += 1

# for i in range(1,  number + 1):
#     fact *= 1

print(fact)


Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.


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

Сколько дней длилась самая длинная оттепель. Оттепель, где градусы > 0.
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50


import random
all_days = int(input('Введите количество дней в месяце: '))
today = 0
i = 1
count = 0
max = 0
while i <= all_days:
    today += random.randint(-3, 3)
    print(today, end=' ')
    if today > 0:
        count += 1
    if count > max:
        max = count
    else:
        count = 0
    i += 1
print(f'\n{max}')

Задача: Среди всех арбузов, надо выбрать самый маленький и самый большой
'''
import random

count_waterlemon = int(input('Введите количество арбузов: '))
minimum_weigh = 30
maximum_weight = 0

for i in range(count_waterlemon):
    weigh_waterlemon = random.randint(1, 30)
    print(f'{i+1} вес арбуза {weigh_waterlemon}')
    if weigh_waterlemon > maximum_weight:
        maximum_weight = weigh_waterlemon
    if weigh_waterlemon < minimum_weigh:
        minimum_weigh = weigh_waterlemon

print(f'\nДля себя {maximum_weight} \nДля тёщи {minimum_weigh}')








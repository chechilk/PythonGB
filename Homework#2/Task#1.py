''''## **Task#1**
**Условие:** На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

*Пример:*
* Input: 5 -> 1 0 1 1 0
* Output: 2'''
import random
count_money = int(input('Введите количество монет: '))
list_money = []
count_one = 0
count_zero = 0

for i in range(count_money):
    list_money.append(random.randint(0, 1))

for i in range(count_money):
    if list_money[i] > 0:
        count_one += 1
    else:
        count_zero += 1

print(list_money)
if count_zero > count_one:
    print(f'\nМинимум надо перевернуть {count_money - count_zero} раз')
else:
    print(f'\nМинимум надо перевернуть {count_money - count_one} раз')



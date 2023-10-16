# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

count_list = int(input('Введите количество элементов в списке: '))
numbers = []
for i in range(count_list):
    numbers.append(random.randint(1, 13))
print('Список: ', numbers)

search_number = random.randint(0, 15)

if numbers.count(search_number) > 0:
    count_search_number = numbers.count(search_number)
    print(f'Количество элемента {search_number} = {count_search_number}')
else:
    print(f'Элемент {search_number} не найден!')

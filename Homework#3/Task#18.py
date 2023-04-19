# Требуется найти в строке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
import random

numbers = []
count_number = int(input('Введите количество элементов в списке: '))

for i in range(count_number):
    numbers.append(random.randint(1, 15))
numbers.sort()
print('Список: ', numbers)

search_number = random.randint(1, 12)

found = numbers[0]
if search_number in numbers:
    print(f'Элемент в списке.\nБлижайшее число к числу {search_number} это {search_number}')
else:
    for item in numbers:
        if abs(item - search_number) < abs(found - search_number):
            found = item
    print(f'Такого элемента в списке нет.\nНо ближайшее из списка к числу {search_number} это {found}')





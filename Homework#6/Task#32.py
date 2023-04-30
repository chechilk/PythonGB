# определить индексы и значения элементов списка, которые входят в заданный диапазон
import random

max_score = int(input('Введите максимальное значение диапазона: '))
min_score = int(input('Введите минимальное значение диапазона: '))
print(list_number := [random.randint(1, 20) for _ in range(15)])

for i in list_number:
    if min_score < i < max_score:
        print(f'Индекс/Значение {i} {list_number[i]}')

# Дан список, состоящий из целых чисел. Напишите
# программу, которая в данном списке определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в списке
# Далее записаны N чисел — элементы списка. Список
# состоит из целых чисел.
from random import randint

# number = [randint(1, 10) for _ in range(10)]
# моржовый оператор
# print(number := [randint(1, 10) for _ in range(11)])
# count = 0
# for i in range(1, len(number) - 1):
#     if number[i - 1] < number[i] > number[i + 1]:
#         count += 1
# print(count)

print(number := [randint(1, 10) for _ in range(11)])
print(len([i for i in range(1, len(number) - 1) if number[i - 1] < number[i] > number[i + 1]]))

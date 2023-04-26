# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа:
# n — кол-во элементов первого множества;
# m — кол-во элементов второго множества;
# Затем пользователь вводит сами элементы множеств.
import random

len_first = int(input('Enter first length set: '))
len_second = int(input('Enter second length set: '))
list_first = list()
list_second = list()

for i in range(len_first):
    list_first.append(random.randint(0, len_first))
for i in range(len_second):
    list_second.append(random.randint(0, len_second))

set_first = set(list_first)
set_second = set(list_second)
set_intersection = set_first.intersection(set_second)
list_intersection = list(set_intersection)
list_intersection.sort()

print("First set: ", set_first)
print("Second set: ", set_second)
print("Intersection first set and second set: ", list_intersection)

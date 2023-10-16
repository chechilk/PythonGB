# 23. Дан список, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random

my_list = []
for i in range(7):
    my_list.append(random.randint(-5, 5))

print(my_list)
count = 0

for j in range(1, len(my_list)):
    if my_list[j] < my_list[j - 1]:
        count += 1
print(count)

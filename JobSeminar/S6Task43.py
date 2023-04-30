from random import randint

print(number := [randint(1, 15) for _ in range(13)])
# Считает, но ошибка в том, что считает 3 повторяющихся числа как 2 пары, а их 1
# count = 0
# for i in range(len(number)):
#     if number[i] in number[i + 1:len(number)]:
#         count += 1
# print(count)
#
# print(len([i for i in range(len(number)) if number[i] in number[i + 1:len(number)]]))

print(sum((number.count(i)//2) for i in set(number)))

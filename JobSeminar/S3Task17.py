'''Задача: Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6'''


my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
my_list_2 = set(my_list)
print(type(my_list_2), my_list_2, len(my_list_2), sep=';')
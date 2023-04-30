from random import randint

print(first_list := [randint(1, 25) for _ in range(randint(5, 15))])
print(second_list := [randint(1, 25) for _ in range(randint(5, 20))])

result_list = [i for i in first_list if i not in second_list]  # перебор элементов первого листа,
# и если нет этих элементов во втором списке - добавляем
print(f'Результат вычитания из \n{first_list} - {second_list} = {result_list}')

# с помощью множества, но без сохранения порядка элементов
'''
first_count, second_count = map(int, input('Введите кол-во элементов 1 и 2 списка: ').split())
print(first_list := [randint(1, 25) for _ in range(first_count)])
print(second_list := [randint(1, 25) for _ in range(second_count)])
print('Изначальные списки', first_list, second_list, sep='\n')

first_set = set(first_list)
second_set = set(second_list)
print('Множество', first_list, second_list, sep='\n')

result_set = first_set.difference(second_set)
result_list = list(result_set)
print('Результат', result_list, sep='\n')
'''

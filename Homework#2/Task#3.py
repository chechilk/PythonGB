''''## **Task#3**
**Условие:** Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.

*Пример:*
* 10 -> 1 2 4 8'''

list_number = [1]
count_number = int(input('Введите количество чисел: '))
numbers = 0
for i in range(1, count_number):
    numbers = list_number[i - 1] + list_number[i - 1]
    if numbers <= count_number:
        list_number.insert(i, numbers)
    else:
        print(list_number)
        exit()
print(list_number)







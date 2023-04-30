# Задача ввести 3 числа (начало, шаг, и сколько цифр)
def fill_list(start, step, count):
    if count == 0:
        return list_number
    else:
        list_number.append(start)
        return fill_list(start + step, step, count - 1)


start = int(input('Введите начало: '))
step = int(input('Введите шаг: '))
count = int(input('Введите кол - во цифр: '))
list_number = []
print(fill_list(start, step, count))

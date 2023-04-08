# Найдите сумму цифр трехзначного числа
number = int(input('Введите трёхзначное число: '))

def checkSize(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count
def checkSumm(number):
    summ = 0
    if checkSize(number) == 3:
        while number > 0:
            summ = summ + (number % 10)
            number //= 10
    else:
        print('Введите верное число')
        exit()
    return summ


print(f'Сумма элементов в числе {number} = {checkSumm(number)}')



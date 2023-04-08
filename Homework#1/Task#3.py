'''Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.'''

number = int(input('Введите номер билета: '))
firstPair = number // 1000
secondPair = number % 1000
firstSumm = 0
secondSumm = 0
def checkSize(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


if checkSize(number) == 6:
    while firstPair > 0 and secondPair > 0:
        firstSumm += firstPair % 10
        firstPair //= 10
        secondSumm += secondPair % 10
        secondPair //= 10
else:
    print('Введите верное кол-во цифр!')
    exit()


if firstSumm == secondSumm:
    print(f'{firstSumm} = {secondSumm} Yes')
else:
    print(f'{firstSumm} != {secondSumm} No')



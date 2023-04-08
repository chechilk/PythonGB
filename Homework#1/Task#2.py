'''Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?

Серёжа = х
Петя = х
Катя = (х+х)2 = 4х
4х + х + х = summ
x = summ/6 - это Петя и Серёжа
4х => x = 4 * (summ/6)
'''
summ = int(input('Введите общее кол-во журавликов: '))
print(f'Катя сделала {4*(summ//6)}, Петя и Серёжа {summ // 6}')

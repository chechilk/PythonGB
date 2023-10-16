'''Среди всех арбузов найти самый меленький и самый большой'''
import random

count_waterlemon = int(input('Введите количество арбузов: '))
minimum_weigh = 30
maximum_weight = 0

for i in range(count_waterlemon):
    weigh_waterlemon = random.randint(1, 30)
    print(f'{i+1} вес арбуза {weigh_waterlemon}')
    if weigh_waterlemon > maximum_weight:
        maximum_weight = weigh_waterlemon
    if weigh_waterlemon < minimum_weigh:
        minimum_weigh = weigh_waterlemon

print(f'\nДля себя {maximum_weight} \nДля тёщи {minimum_weigh}')
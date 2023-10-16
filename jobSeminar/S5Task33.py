# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
from random import randint


#   С помощью листов и рекурсии
def func(score, max_number, min_score):
    if max_number in score:
        index_max_score = score.index(max_number)   # Находим индекс максимального элемента
        score.remove(max_number)    # удаляем максимальный элемент по индексу
        score.insert(index_max_score, min_score)    # на место удалённого ставим минимальную оценку
        return (func(score, max_number, min_score))
    return score


score = [randint(1, 5) for _ in range(1, 10)]
score_for = score.copy()
print('Оценки до исправления: ', score)
max_number = max(score)
min_score = min(score)
print('Оценки после исправления (list + рекурсия): ', func(score, max_number, min_score))

#   С помощью for
for i in range(len(score_for)):
    if score_for[i] == max_number:
        score_for[i] = min_score
print('Оценки после исправления (for): ', score_for)

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только  английские, либо только русские буквы.


point_in_Scrabble = {
    1: 'AEIOULNSTRАВЕИНОРСТ',
    2: 'DGДКЛМПУ',
    3: 'BCMPБГЁЬЯ',
    4: 'FHVWYЙЫ',
    5: 'KЖЗХЦЧ',
    8: 'JXШЭЮ',
    10: 'QZФЩЪ'
}

summ = 0
search_letter = input('Введите слово: ')

for letter in search_letter.upper():
    for key, value in point_in_Scrabble.items():
        if letter in value:
            summ += key

print(f'Сумма слова {search_letter} = {summ}')

# english_dict = {
#     1: 'AEIOULNSTR',
#     2: 'DG',
#     3: 'BCMP',
#     4: 'FHVWY',
#     5: 'K',
#     8: 'JX',
#     10: 'QZ'
# }
# russian_dict = {
#     1: 'АВЕИНОРСТ',
#     2: 'ДКЛМПУ',
#     3: 'БГЁЬЯ',
#     4: 'ЙЫ',
#     5: 'ЖЗХЦЧ',
#     8: 'ШЭЮ',
#     10: 'ФЩЪ'
# }
# from langdetect import detect
# с помощью detect() возвращает язык (не всегда правильно)
# import re
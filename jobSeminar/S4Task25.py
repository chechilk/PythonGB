# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

text_list = list(input('Введите строку: '))  # ввод строки
# text_list = list(text)  # конвертация строки в список
count_text = dict()  # создание пустого словаря

# запись элементов списка
# for letters in text_list:  # берём элементы из списка
#     if letters in count_text:  # есть ли элемент списка в словаре?
#         count_text[letters] += 1  # если есть, то +1
#         print(f'{letters}_{count_text[letters]}', end=' ')
#     else:
#         count_text[letters] = 0  # если нет, то создаём и добавляем ему значение 0
#         print(letters, end=' ')
# print(f'{letters}_{count_text[letters]}'if count_text[letters] > 0 else letters, end=' ')

for letters in text_list:
        count_text[letters] = count_text.get(letters, 0) + 1
        print(letters if count_text.get(letters) == 1 else
              f'{letters}_{count_text.get(letters) - 1}', end=' ')
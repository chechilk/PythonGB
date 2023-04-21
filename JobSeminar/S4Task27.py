# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells " \
#        "that she sells are sea shells Im sure. So if she sells sea" \
#        "shells on the sea shore Im sure that the shells are sea" \
#        "shore shells"

text = input('Enter some text: ')
text_list = text.lower().split()
count_dict = dict()

for letter in text_list:
    count_dict[letter] = count_dict.get(letter, 0) + 1
print('Различных слов:', len(count_dict))

# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure . So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

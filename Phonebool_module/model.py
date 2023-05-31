phone_book = []
path = 'phone_book.txt'


def open_book():
    global phone_book  # указываем с чем конкретно будем работать
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()  # считываем все строки с переносом строки
    for contact in data:
        contact = contact.strip().split(':')  # разделяем строки по символу ":" и убираем служебные символы
        new = {'last_name': contact[0],
               'first_name': contact[1],
               'phone': contact[2],
               'comm': contact[3]}
        phone_book.append(new)  # считываем файл -> создаём копию и добавляем список словарей в phone_book


def get_pb():
    global phone_book
    return phone_book

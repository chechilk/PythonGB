from typing import List

phone_book: list[dict[str:str]] = []
path = 'phone_book.txt'


def open_book():
    global phone_book  # указываем с чем конкретно будем работать
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()  # считываем все строки с переносом строки
    for contact in data:
        contact = contact.strip().split(':')  # разделяем строки по символу ":" и убираем служебные символы
        new = {'id': contact[0],
               'last_name': contact[1],
               'first_name': contact[2],
               'phone': contact[3],
               'comm': contact[4]}
        phone_book.append(new)  # считываем файл -> создаём копию и добавляем список словарей в phone_book


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))  # объединяем в список каждое значение словаря по :
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> list[str | None]:  # добавляем новый контакт
    global phone_book
    new_id = int(phone_book[-1].get('id')) + 1
    new['id'] = str(new_id)
    phone_book.append(new)
    return [new.get('last_name'), new.get('first_name')]


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    for contact in phone_book:  # берём первый контакт
        for field in contact.values():  # берём каждые ЗНАЧЕНИЯ 1го контакта
            if word.lower() in field.lower():  # если значение совпало
                result.append(contact)  # добавляем весь контакт
                break
    return result


def search_max_len_pb(book: list[dict[str, str]]) -> int:
    len_dict = []
    # добавление элементов словарей в лист
    for contacts in book:
        for key, value in contacts.items():
            len_dict.append([key, value])
    list_summ = []
    # поиск максимальной длины
    for contact in len_dict:
        summ = 0
        for i in contact:
            summ = summ + len(i)
        list_summ.append(summ)
    return max(list_summ)


def change_contact(new: dict, index: int) -> list:
    global phone_book
    for contact in phone_book:
        if index == contact.get('id'):
            contact['first_name'] = new.get('first_name', contact.get('first_name')) # если ничего не ввели, добавляем тоже самое
            contact['last_name'] = new.get('last_name', contact.get('last_name'))
            contact['phone'] = new.get('phone', contact.get('phone'))
            contact['comm'] = new.get('comm', contact.get('comm'))
            return [new.get('last_name'), new.get('first_name')]
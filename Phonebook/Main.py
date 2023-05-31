draft_book = []
book = []
path = 'book.txt'


def open_file_read():  # Открыть файл для чтения case 1
    global book
    with open(path, 'r', encoding='UTF-8') as file:
        main_list = file.readlines()  # чтение всех строк
    for word in main_list:
        word = word.strip().split(':')  # Отделяем значения по :, отбрасывая служебные символы
        # Список словарей. Добавляем ключи
        draft_book.append({'last_name': word[0],
                           'first_name': word[1],
                           'phone': word[2],
                           'comm': word[3]})
    book = draft_book.copy()
    return 'Файл открыт'


def save_file():
    global book
    list_for_save_data = []  # создаём список для новой инфы
    for word in draft_book:
        list_for_save_data.append(':'.join(word.values()))  # добавляем значения из черновика
    data = '\n'.join(list_for_save_data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    book = draft_book.copy()
    return 'Файл сохранён'


def add_new_contact(new_human: dict[str, str]) -> None:
    draft_book.append(new_human)  # Сохраняем нового человека в черновой вариант справочника,
    # а после уже он сохраняется в основной справочник

def show_full_contact(phone_book: list[dict]) -> None:
    print('puk')
    for i, words in enumerate(phone_book, 1):
        print(f'{i}.{words.get("last_name")}'
              f'{words.get("first_name")}'
              f'{words.get("phone")}'
              f'{words.get("comm")}')
def input_human_info():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    number_phone = input('Введите номер телефона: ')
    comm = input('Введите комментарий: ')
    return {'last_name': last_name, 'first_name': first_name, 'phone': number_phone, 'comm': comm}

def get_phone_book() -> list[dict]:
    return book

print(
    f'1. Открыть файл\n2. Сохарнить файл\n3. Показать все контакты\n4. Добавить контакт\n5. Найти контакт\n6. Изменить контакт\n7. Удалить контакт\n8. Выход')

while True:
    while True:
        number = int(input('Введите цифру для выбора действия: '))
        if 0 < number < 9:
            match number:
                case 1:
                    print(open_file_read())  # Открыть файл для чтения
                case 2:
                    print(save_file())
                    print(book)
                case 3:
                    pb = get_phone_book()
                    show_full_contact(pb)  # Показать все контакты
                case 4:
                    print(add_new_contact(input_human_info()))  # Запись в файл
                case 8:
                    exit()
                case _:
                    print('Выберите числа от 1 - 8!')

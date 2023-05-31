import text  # Импорт модуля text


def main_menu() -> int:  # Выбор пункта меню, возвращает выбранный пункт(int)
    print(text.menu)  # text - модуль, menu - объект. считывает сколько строк в menu
    while True:
        option = input(text.input_option)
        if option.isdigit() and 0 < int(option) < 9:  # Проверка на правильность выбора цифры
            return int(option)


def print_message(message: str):  # печать сообщений
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    if book:  # если данные заполнены
        print('\n' + '=' * 71)
        for i, contact in enumerate(book, 1):
            print(f'{i:>3}.{contact.get("last_name"):<20} | ' # по середине :^
                  f'{contact.get("first_name"):<20} | '
                  f'{contact.get("phone"):<20} | '
                  f'{contact.get("comm"):<20}| ')
        print('=' * 71 + '\n')
    else:
        print_message(error)

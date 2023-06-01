import text  # Импорт модуля text
import model


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
        print('\n' + '=' * ((model.search_max_len_pb(model.get_pb())) + 20 * 4))
        for contact in book:
            print(f'{contact.get("id")}.{contact.get("last_name"):<20} | '  # по середине :^
                  f'{contact.get("first_name"):<20} | '
                  f'{contact.get("phone"):<20} | '
                  f'{contact.get("comm"):<20}| ')
        print('=' * ((model.search_max_len_pb(model.get_pb())) + 20 * 4) + '\n')
    else:
        print_message(error)


def input_contact(message) -> [dict[str, str]]:
    new = {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key] = value  # Вводим данные с клавиатуры в каждый key
    return new

def input_index(book: list, message: str) -> int:
    while True:
        option = input(message)
        if option.isdigit() and


def input_search(message) -> str:
    return input(message)

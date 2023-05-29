def open_file_read(path):  # Открыть файл для чтения
    with open(path, 'r') as file:
        main_list = file.readlines()  # чтение всех строк
        # запись строк в лист
    return [x.rstrip().split(':') for x in main_list]


def open_full_file(path):
    with open(path, 'r') as file:
        main_list = file.readlines()
        for line in main_list:
            print(line.rstrip().split(':'))
        # return [line.rstrip().split(':') for line in main_list]


def open_file_write(path, list_file):  # Открыть файл для записи
    with open(path, 'w') as file:
        file.writelines([':'.join(x) + '\n' for x in list_file])


print(
    f'1. Открыть файл\n2. Сохарнить файл\n3. Показать все контакты\n4. Добавить контакт\n5. Найти контакт\n6. Изменить контакт\n7. Удалить контакт\n8. Выход')
number = int(input('Введите цифру для выбора действия: '))

match number:
    case 1:
        print(open_file_read('book.txt'))  # Открыть файл для чтения
    case 3:
        open_full_file('book.txt')  # Показать все контакты
    case 4:
        list_file = [['Vova', 'Puk', '82374', 'comm'], ['Polina', 'Puk', '28472', 'kek']]
        print(open_file_write('book_1.txt', list_file))  # Запись в файл
    case _:
        print('Выберите числа от 1 - 8!')

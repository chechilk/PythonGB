# запуск основных команд

import view
import model
import text


def start():
    while True:  # для того, что бы выбор был цикличен, до момента выбора case 8
        option = view.main_menu()
        match option:
            case 1:
                model.open_book()
                view.print_message(text.open_successful)
                pass
            case 2:
                pass
            case 3:
                pb = model.get_pb() # взяли из model и отправляем на view
                view.print_contacts(pb, text.pb_empty)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break

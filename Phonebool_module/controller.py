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
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_pb()  # возвращает phone_book
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = model.search_contact(key_word)
                view.print_contacts(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:  # если несколько человек
                        view.print_contacts(result, ' ')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = int(result[0].get('id'))
                    # условия для всех
                    new_contact = view.input_contact(text.change_contact)
                    name = model.change_contact(new_contact, current_id)
                    view.print_message(text.change_successful(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 7:
                pb = model.get_pb()
                view.print_contacts(pb, text.error_open_file)
                if pb:
                    index = view.input_index(pb, text.input_index_delete)  # выбор индекса на удаление
                    if view.confirm(text.confirm_delete(pb[index - 1].get('first_name'))):  # если y, то удаляем
                        view.print_message(text.delete_contact_successful(model.remove_contact(index)))
                    else:
                        view.print_message(text.error_delete_contact)
            case 8:
                if view.confirm(text.confirm_exit()):
                    break

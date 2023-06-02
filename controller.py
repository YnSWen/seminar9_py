import view
import model
import text_for_user

my_phonebook = model.PhoneBook()


def start():

    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                # Открыть файл
                my_phonebook.open()
                view.print_message(text_for_user.load_successful)
            case 2:
                # Сохранить файл
                my_phonebook.save()
                view.print_message(text_for_user.save_successful)
            case 3:
                # Показать все контакты
                _phonebook = my_phonebook.show_contacts()
                view.print_contacts(_phonebook, text_for_user.pb_empty)
            case 4:
                # Добавить контакт
                contact = view.input_contact(text_for_user.input_new_contact)
                name = my_phonebook.add_contact(contact)
                view.print_message(text_for_user.new_contact_successful(name))
            case 5:
                # Найти контакт
                key_word = view.input_search(text_for_user.input_search)
                result = my_phonebook.search(key_word)
                view.print_contacts(result, text_for_user.empty_search)
            case 6:
                # Изменить контакт
                key_word = view.input_search(text_for_user.input_change)
                result = my_phonebook.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        found_id = view.input_search(text_for_user.input_index_for_change)
                    else:
                        found_id = result[0].get('id')
                    new_contact = view.input_contact(text_for_user.change_contact)
                    name = my_phonebook.change_contact(new_contact, found_id)
                    view.print_message(text_for_user.change_successful(name))
                else:
                    view.print_message(text_for_user.empty_search(key_word))

            case 7:
                # Удалить контакт
                key_word = view.input_search(text_for_user.input_delete)
                result = my_phonebook.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        found_id = view.input_search(text_for_user.input_index_for_delete)
                    else:
                        found_id = result[0].get('id')
                    name = my_phonebook.delete_contact(found_id)
                    view.print_message(text_for_user.delete_successful(name))
                else:
                    view.print_message(text_for_user.empty_search)
            case 8:
                # Выход
                break

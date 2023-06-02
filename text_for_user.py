main_menu = '''\nКоманды для работы с телефонной книгой:
    1 - Открыть файл
    2 - Сохранить файл
    3 - Показать все контакты
    4 - Добавить контакт
    5 - Найти контакт
    6 - Изменить контакт
    7 - Удалить контакт
    8 - Выход\n'''

input_choice = 'Введите команду: '

load_successful = 'Телефонная книга успешно открыта.'

save_successful = 'Телефонная книга успешно сохранена.'

pb_empty = 'Телефонная книга пуста или не загружена.'

input_new_contact = 'Введите данные нового контакта: '
new_contact = {'name': 'Введите имя: ',
                'phone_number': 'Введите номер телефона: ',
                'city': 'Введите город: '}


def new_contact_successful(name:str):
    return f'Контакт {name} успешно добавлен'


input_search = 'Поиск: '


def empty_search(word) -> str:
    return f'Контакты, содержащие {word} не найдены'


input_change = 'Введите контакт, который надо изменить: '
input_index_for_change = 'Введите индекс контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, если не надо менять данные: '


def change_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен.'


input_delete = 'Введите контакт, который нужно удалить: '

input_index_for_delete = 'Введите индекс контакта: '


def delete_successful(name: str) -> str:
    return f'Контакт {name} успешно удален!'

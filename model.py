
class PhoneBook:

    def __init__(self, path: str = 'phonebook.txt'):
        self.phone_book: list[dict[str, str]] = []
        self.path = path
        self.last_id = 0

    def open(self):
        with open(self.path, 'r', encoding= 'UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(';')
            new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'city': contact[3]}
            self.phone_book.append(new)

    def save(self):
        data = []
        for contact in self.phone_book:
            data.append(';'.join([value for value in contact.values()]))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def show_contacts(self):
        return self.phone_book

    def add_contact(self, new: dict[str, str]) -> str:
        self.last_id += 1
        new['id'] = str(self.last_id)
        self.phone_book.append(new)
        return new.get('name')

    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self.phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result

    def change_contact(self, new: dict, index: int | str) -> str:
        for contact in self.phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone_number'] = new.get('phone_number', contact.get('phone_number'))
                contact['city'] = new.get('city', contact.get('city'))
                return contact.get('name')

    def delete_contact(self, index: int) -> str:
        deleted_contact = self.phone_book.pop(index - 1)
        return deleted_contact.get('name')


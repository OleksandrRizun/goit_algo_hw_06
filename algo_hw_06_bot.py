#------------------------------------------------------------------------------
# Розробити книгу контактів. Можна додавати/видаляти/редагувати/шукати записи.
# Поля (критерии) можуть бути обов'язковими і необов'язковими.
# Записи можуть містити декілька полів одного типу (наприклад, телефонів).
# Реалізована валідація номера телефону (10 цифр).
#------------------------------------------------------------------------------
from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('The number format is incorrect')
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def __str__(self):
        return f"Contact name: {self.name.value}, "\
                f"phones: {'; '.join(str(p) for p in self.phones)}"
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    def edit_phone(self, old_phone, new_phone):
        line = [str(p) for p in self.phones]
        index = line.index(old_phone)
        self.phones[index] = Phone(new_phone)
    def find_phone(self, phone):
        line = [str(p) for p in self.phones]
        return Phone(phone) if phone in line else None
    def remove_phone(self, phone):
        line = [str(p) for p in self.phones]
        if phone in line:
            index = line.index(phone)
            self.phones.pop(index)

class AddressBook(UserDict):
    def __str__(self):
        strg = '\n--------------- Address Book -------------------\n'
        for key, value in self.items():
            line = ', '.join(str(phone) for phone in value.phones)
            strg += f'{key}: {line} \n'
        return strg
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def find(self, name):
        if not name in self.keys():
            return None
        return self.data[name]
    def delete(self, name):
        if not name in self.keys():
            return
        del self[name]

book = AddressBook()
john_record = Record('John')
john_record.add_phone('1234567890')
john_record.add_phone('5555555555')
book.add_record(john_record)
jane_record = Record('Jane')
jane_record.add_phone('9876543210')
book.add_record(jane_record)
print(book)
john = book.find('John')
john.edit_phone('1234567890', '1112223333')
print(john)
found_phone = john.find_phone('5555555555')
print(f'{john.name}: {found_phone}')
book.delete('Jane')

john.remove_phone('5555555555')
john.add_phone('8888888888')
print(book)
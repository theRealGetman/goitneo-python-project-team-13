from collections import UserDict, defaultdict
from datetime import datetime
from src.utils import *


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise BirthdayValidationError()

        super().__init__(date)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise PhoneValidationError()

        super().__init__(value)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Phone):
            return self.value == other.value
        return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        phone = Phone(phone)

        if phone in self.phones:
            raise PhoneExistsError()

        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        phone = Phone(phone)

        if phone not in self.phones:
            raise PhoneNotExistError()

        self.phones.remove(phone)

    def edit_phone(self, old: str, new: str):
        old = Phone(old)
        new = Phone(new)

        if old not in self.phones:
            raise PhoneNotExistError()

        index = self.phones.index(old)
        self.phones[index] = new

    def find_phone(self, phone: str) -> Phone:
        phone = Phone(phone)

        if phone not in self.phones:
            raise PhoneNotExistError()

        index = self.phones.index(phone)

        return self.phones[index]

    def add_birthday(self, birthday: str):
        if self.birthday:
            raise BirthdayExistsError()

        birthday = Birthday(birthday)

        self.birthday = birthday

    def show_birthday(self) -> str:
        if not self.birthday:
            raise BirthdayNotExistError()

        return datetime.strftime(self.birthday.value, "%d.%m.%Y")


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value

        if name in self.data:
            raise ContactExistsError()

        self.data[name] = record

    def edit_record(self, record: Record):
        name = record.name.value

        if name not in self.data:
            raise ContactNotExistError()

        self.data[name] = record

    def find(self, name: str) -> Record:
        try:
            return self.data[name]
        except KeyError:
            raise ContactNotExistError()

    def delete(self, name: str):
        try:
            self.data.pop(name)
        except KeyError:
            raise ContactNotExistError()

    def all_records(self):
        return self.data.values()

    def get_birthdays_per_week(self) -> str:
        birthdays_by_weekday = defaultdict(list)
        today = datetime.now().date()
        for contact in self.data.values():
            name = contact.name.value

            if not contact.birthday:
                continue
            birthday = contact.birthday.value

            birthday_this_year = birthday.replace(year=today.year)
            if today > birthday_this_year:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1)

            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                weekday = weekdays[birthday_this_year.weekday()]
                if weekday == 'Saturday' or weekday == 'Sunday':
                    if delta_days > 5:
                        birthdays_by_weekday['Next Monday'].append(
                            {'name': name, 'days_delta': delta_days})
                    else:
                        birthdays_by_weekday['Monday'].append(
                            {'name': name, 'days_delta': delta_days})
                else:
                    birthdays_by_weekday[weekday].append(
                        {'name': name, 'days_delta': delta_days})

        sorted_items = {k: v for k, v in sorted(
            birthdays_by_weekday.items(), key=lambda item: item[1][0]['days_delta'])}

        result = []
        for weekday, contacts in sorted_items.items():
            result.append('{}: {}'.format(weekday, ', '.join(
                [contact['name'] for contact in contacts])))

        return result

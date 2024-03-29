from src.local_storage import address_book, notes
from src.utils import ContactExistsError, handle_error, commands, NoteExistsError
from src.models import Record
from src.notes import Note
from termcolor import colored

_separator = '\n' + ('-' * 80) + '\n'

# AddressBook


@handle_error(
    args_error_label='You need to provide name and phone',
    key_error_label='Contact already exists.',
)
def add_contact(name, phone, email='', birthday='') -> str:
    if not name or not phone:
        raise ValueError()

    try:
        record = Record(name)
        record.add_phone(phone)
        if email:
            record.add_email(email)
        if birthday:
            record.add_birthday(birthday)

        address_book.add_record(record)
        return f'Contact {name} added.'
    except ContactExistsError:
        record = address_book.find(name)
        record.add_phone(phone)
        address_book.edit_record(record)
        return f'Added phone to contact {name}.'


def is_contact_already_exist(name: str) -> bool:
    return address_book.is_record_already_exist(name)


@handle_error(
    args_error_label='You need to provide name, old phone and new phone',
    key_error_label='Contact doesn`t exist.',
)
def change_contact(name, old_phone, new_phone) -> str:
    if not name or not old_phone or not new_phone:
        raise ValueError()

    record = address_book.find_by_name(name)
    record.edit_phone(old_phone, new_phone)

    return f'For {name} changed phone from {old_phone} to {new_phone}'


@handle_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn`t exist.',
)
def remove_contact(args) -> str:
    name = args[0]

    address_book.remove_contact(name)
    return f'Contact {name} removed'


@handle_error(
    args_error_label='You need to provide name or phone',
    key_error_label='Contact doesn\'t exist.',
)
def find_contact(args) -> str:
    keyword = args[0]
    records = address_book.find(keyword)
    if records:
        return '\n' + _separator.join(str(record) for record in records) + '\n'
    else:
        return f'No contacts find for search query: {keyword}'


@handle_error(
    args_error_label='You need to provide name and birthday',
    key_error_label='Contact doesn\'t exists.',
)
def add_birthday(args) -> str:
    name, birthday = args

    record = address_book.find_by_name(name)
    record.add_birthday(birthday)

    return f'For {name} added birthday {birthday}'


@handle_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn\'t exists.',
)
def show_birthday(args) -> str:
    name = args[0]

    record = address_book.find_by_name(name)
    return record.show_birthday()


@handle_error(
    args_error_label='You need to specify the amount of days in numbers',
)
def get_birthdays_per_day(args) -> str:
    if not args:
        return '\n'.join(address_book.get_birthdays_per_week())
    else:
        days = int(args[0])
        return '\n'.join(address_book.get_birthdays_per_week(days))


@handle_error(
    args_error_label='You need to provide name and email',
    key_error_label='Contact doesn\'t exists.',
)
def add_email(args) -> str:
    name, email = args

    record = address_book.find_by_name(name)
    record.add_email(email)

    return f'For {name} added email {email}'


@handle_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn\'t exists.',
)
def show_email(args) -> str:
    name = args[0]

    record = address_book.find_by_name(name)
    return record.show_email()


@handle_error(
    args_error_label='You need to provide name and email',
    key_error_label='Contact doesn\'t exists.',
)
def change_email(args) -> str:
    name, email = args

    record = address_book.find_by_name(name)
    record.change_email(email)

    return f'For {name} changed email {email}'


@handle_error()
def show_all() -> str:
    return '\n' + _separator.join([str(record) for record in address_book.all_records()]) + '\n'


# Notes
@handle_error(
    args_error_label='You need to provide title, description, and optionally tags',
)
def add_note(args) -> str:
    title, desc, tags = args
    note = Note(title, desc, tags.split(' '))
    notes.add_note(note)
    return f'Note "{title}" added.'


@handle_error(
    args_error_label='You need to provide title',
    key_error_label='Note doesn\'t exist.',
)
def show_notes(search: list = None) -> str:
    def show(notes):
        return ''.join(_separator + str(notes[note]) for note in notes) + _separator

    if not search:
        return show(notes)

    found_notes = notes.find_notes(search)

    if found_notes:
        return show(found_notes)

    return 'No notes found.'


@handle_error(
    args_error_label='You need to provide title and optionally new title, new description, and new tags',
    key_error_label='Note doesn\'t exist.',
)
def edit_note(title, new_title, new_desc, tags) -> str:
    new_tags = tags.split()
    notes.edit_note(title, new_title=new_title,
                    new_desc=new_desc, new_tags=new_tags)
    return f'Note "{title}" has been updated.'


@handle_error(
    args_error_label='You need to provide title',
    key_error_label='Note doesn\'t exist.',
)
def remove_note(title) -> str:
    if not title:
        raise ValueError()

    notes.remove_note(title)
    return f'Note "{title}" removed.'


# Common
def hello() -> str:
    return 'Greetings, fellow traveler of the sands. May the wisdom of the desert bless your journey.'


def close() -> str:
    return 'May the sands of time guide your path, until we meet again beneath the stars of Arrakis. Farewell, noble traveler.'


def note_already_exist(title: str) -> str:
    return f'Note with title: "{title}" already exist.'


def is_note_already_exist(title: str) -> bool:
    return notes.is_note_already_exist(title)


def note_doesnt_exist(title: str) -> str:
    return f'Note with title: "{title}" doesn\'t exist.'


def invalid_command() -> str:
    return 'Invalid command.'


def print_help() -> None:
    print(colored("Available commands:", 'light_yellow', attrs=['bold']))
    for name, description in commands.items():
        formatted_name = f"{colored(name, 'green', attrs=['bold']):40}"
        print(f"{formatted_name} {description}")

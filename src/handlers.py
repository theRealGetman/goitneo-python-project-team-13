
from src.local_storage import address_book, notes
from src.utils import ContactExistsError, handle_error, commands, NoteExistsError
from src.models import Record
from src.notes import Note
from termcolor import colored


# AddressBook
@handle_error(
    args_error_label='You need to provide name and phone',
    key_error_label='Contact already exists.',
)
def add_contact(args) -> str:
    name, phone = args

    try:
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        return f'Contact {name} added.'
    except ContactExistsError:
        record = address_book.find(name)
        record.add_phone(phone)
        address_book.edit_record(record)
        return f'Added phone to contact {name}.'


@handle_error(
    args_error_label='You need to provide name, old phone and new phone',
    key_error_label='Contact doesn`t exist.',
)
def change_contact(args) -> str:
    name, old_phone, new_phone = args

    record = address_book.find_by_name(name)
    record.edit_phone(old_phone, new_phone)

    return f'For {name} changed phone from {old_phone} to {new_phone}'


@handle_error(
    args_error_label='You need to provide name or phone',
    key_error_label='Contact doesn\'t exist.',
)
def find_contact(args) -> str:
    keyword = args[0]
    separator = '\n' + ('-' * 40) + '\n'
    records = address_book.find(keyword)
    if records:
        return '\n' + separator.join(str(record) for record in records) + '\n'
    else:
        return f'No contacts find for search query: {keyword}'


@handle_error(
    args_error_label='You need to provide name and birthday',
    key_error_label='Contact doesn\'t exists.',
)
def add_birthday(args) -> str:
    name, birthday = args

    record = address_book.find(name)
    record.add_birthday(birthday)

    return f'For {name} added birthday {birthday}'


@handle_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn\'t exists.',
)
def show_birthday(args) -> str:
    name = args[0]

    record = address_book.find(name)
    return record.show_birthday()


@handle_error()
def birthdays() -> str:
    return '\n'.join(address_book.get_birthdays_per_week())


@handle_error()
def show_all() -> str:
    return '\n'.join([str(record) for record in address_book.all_records()])


# Notes
@handle_error(
    args_error_label='You need to provide title, description, and optionally tags',
)
def add_note(args) -> str:
    title, desc, *tags = args
    note = Note(title, desc, tags)
    notes.add_note(note)
    return f'Note "{title}" added.'


@handle_error(
    args_error_label='You need to provide title',
    key_error_label='Note doesn\'t exist.',
)
def show_notes(search: list = None) -> str:
    separator = '\n' + ('-' * 40) + '\n\n'

    def show(notes):
        return ''.join(separator + str(notes[note]) for note in notes) + separator

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
    notes.edit_note(title, new_title=new_title, new_desc=new_desc, new_tags=new_tags)
    return f'Note "{title}" has been updated.'


@handle_error(
    args_error_label='You need to provide title',
    key_error_label='Note doesn\'t exist.',
)
def remove_note(args) -> str:
    title = args[0]
    notes.remove_note(title)
    return f'Note "{title}" removed.'


# Common
def hello() -> str:
    return 'How can I help you?'


def close() -> str:
    return 'Good bye!'


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

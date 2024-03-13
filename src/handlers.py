from src.local_storage import address_book, notes
from src.utils import ContactExistsError, handle_error, NoteNotExistError
from src.models import Record
from src.notes import Note


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

    record = address_book.find(name)
    record.edit_phone(old_phone, new_phone)

    return f'For {name} changed phone from {old_phone} to {new_phone}'


@handle_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn\'t exist.',
)
def show_phone(args) -> str:
    name = args[0]
    return ', '.join(str(phone) for phone in address_book.find(name).phones)


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
    print('args', args)
    title, desc, *tags = args
    note = Note(title, desc, tags)
    print('Note', note)

    notes.add_note(note)
    return f'Note "{title}" added.'


@handle_error(
    args_error_label='You need to provide title',
    key_error_label='Note doesn\'t exist.',
)
def show_notes(args) -> str:
    if not args:
        return '\n'.join(str(note) for note in notes.data)
    key_word = args[0]
    found_notes = notes.find_notes(key_word)
    if found_notes:
        return '\n'.join(str(note) for note in found_notes) + '\n'
    return 'No notes found.'


@handle_error(
    args_error_label='You need to provide title and optionally new title, new description, and new tags',
    key_error_label='Note doesn\'t exist.',
)
def edit_note(args) -> str:
    if len(args) < 1:
        raise ValueError("You need to provide at least the title of the note to edit.")

    title = args[0]
    new_title = args[1] if len(args) > 1 else ''
    new_desc = args[2] if len(args) > 2 else ''
    new_tags = args[3].split(',') if len(args) > 3 else []

    try:
        notes.edit_note(title, new_title=new_title, new_desc=new_desc, new_tags=new_tags)
        return f'Note "{title}" has been updated.'
    except NoteNotExistError as e:
        return str(e)


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


def invalid_command() -> str:
    return 'Invalid command.'

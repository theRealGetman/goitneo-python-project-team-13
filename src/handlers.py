from src.local_storage import address_book
from src.utils import ContactExistsError, handle_error, commands
from src.models import Record
from termcolor import colored


def hello() -> str:
    return 'How can I help you?'


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
    record[0].add_birthday(birthday)

    return f'For {name} added birthday {birthday}'


@handle_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn\'t exists.',
)
def show_birthday(args) -> str:
    name = args[0]

    record = address_book.find(name)
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


@handle_error()
def show_all() -> str:
    return '\n'.join([str(record) for record in address_book.all_records()])


def close() -> str:
    return 'Good bye!'


def invalid_command() -> str:
    return 'Invalid command.'


def print_help() -> None:
    print(colored("Available commands:", 'light_yellow', attrs=['bold']))
    for name, description in commands.items():
        formatted_name = f"{colored(name, 'green', attrs=['bold']):40}"
        print(f"{formatted_name} {description}")

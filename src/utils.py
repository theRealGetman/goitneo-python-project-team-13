from prompt_toolkit.completion import NestedCompleter


class PhoneValidationError(Exception):
    pass


class PhoneExistsError(Exception):
    pass


class PhoneNotExistError(Exception):
    pass


class BirthdayValidationError(Exception):
    pass


class BirthdayExistsError(Exception):
    pass


class BirthdayNotExistError(Exception):
    pass


class ContactExistsError(Exception):
    pass


class ContactNotExistError(Exception):
    pass


class EmailValidationError(Exception):
    pass


class EmailExistsError(Exception):
    pass


class EmailNotExistError(Exception):
    pass


def handle_error(args_error_label='', key_error_label=''):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                return args_error_label
            except KeyError:
                return key_error_label
            except PhoneValidationError:
                return 'Phone must be 10 digits'
            except PhoneExistsError:
                return 'Phone already exists'
            except PhoneNotExistError:
                return 'Phone doesn\'t exists'
            except BirthdayValidationError:
                return 'Birthday does not match format \'DD.MM.YYYY\''
            except BirthdayExistsError:
                return 'Birthday already exists'
            except BirthdayNotExistError:
                return 'Birthday doesn\'t exist'
            except ContactExistsError:
                return 'Contact already exists'
            except ContactNotExistError:
                return 'Contact doesn\'t exist'
            except EmailValidationError:
                return 'You should provide real email address'
            except EmailNotExistError:
                return 'Email doesn\'t exist'
            except EmailExistsError:
                return 'Email already exist'
            except Exception as e:
                return f'Exception during {func.__name__} >>> {e}'
        return inner
    return decorator


weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


# TODO: add notes related commands
commands = {
    'help': "Shows all available commands",
    'hello': "Greeting command",
    'add': "Adds new contact. Required arguments: name, phone (10 digits)",
    'change': "Changes existing contact. Required arguments: name, old phone, new phone",
    'phone': "Shows contact phones. Required arguments: name",
    'all': "Shows all contacts",
    'add-birthday': "Adds birthday to contact. Date format: dd-mm-yyyy",
    'show-birthday': "Shows contact birthday. Required arguments: name",
    'birthdays': "Shows upcoming birthdays",
    'exit': "Exits assistant",
    'close': "Alias for Exit command"
}


commands_completer = NestedCompleter.from_nested_dict(
    dict.fromkeys(commands.keys()))

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

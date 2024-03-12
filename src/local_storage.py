from src.models import AddressBook
import pickle
import os

_filename = "assets/address_book.bin"
address_book: AddressBook = None


def initialize_book():
    global address_book

    try:
        with open(_filename, 'rb') as file:
            address_book = pickle.load(file)
    except:
        address_book = AddressBook()


initialize_book()


def save_book():
    os.makedirs(os.path.dirname(_filename), exist_ok=True)
    with open(_filename, 'wb') as file:
        pickle.dump(address_book, file)

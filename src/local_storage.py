from src.models import AddressBook
from src.notes import Notes

import pickle
import os

_address_book_filename = "assets/address_book.bin"
_notes_filename = "assets/notes.bin"

address_book: AddressBook = None
notes: Notes = None


def initialize_book():
    global address_book

    try:
        with open(_address_book_filename, 'rb') as file:
            address_book = pickle.load(file)
    except:
        address_book = AddressBook()


def initialize_notes():
    global notes

    try:
        with open(_notes_filename, 'rb') as file:
            notes = pickle.load(file)
    except:
        notes = Notes()


initialize_book()
initialize_notes()


def save_book():
    os.makedirs(os.path.dirname(_address_book_filename), exist_ok=True)
    with open(_address_book_filename, 'wb') as file:
        pickle.dump(address_book, file)


def save_notes():
    os.makedirs(os.path.dirname(_notes_filename), exist_ok=True)
    with open(_notes_filename, 'wb') as file:
        pickle.dump(notes, file)

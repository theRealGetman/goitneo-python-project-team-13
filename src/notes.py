from collections import UserList
from datetime import datetime
from src.utils import *


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Title(Field):
    pass


class Desc(Field):
    pass


class Tag(Field):
    pass


class CreateAt(Field):
    def __init__(self):
        data = datetime.now().date()
        self.value = data
        super().__init__(data)


class Note:
    def __init__(self, title: str, desc: str, tags: list):
        self.title = Title(title)
        self.desc = Desc(desc)
        self.tags = [Tag(tag) for tag in tags]
        self.createAt = CreateAt()

    def __str__(self):
        tags_str = ', '.join(tag.value for tag in self.tags)
        return (f"Title: {self.title.value}\n"
                f"Description: {self.desc.value}\n"
                f"Tags: {tags_str}\n"
                f"Created At: {self.createAt.value.strftime('%Y-%m-%d')}")


class Notes(UserList):
    def add_note(self, note: Note):
        self.data.append(note)

    def edit_note(self, title, new_title: str = '', new_desc: str = '', new_tags: list = []):
        for note in self.data:
            if note.title.value == title:
                if new_title:
                    note.title = Title(new_title)
                if new_desc:
                    note.desc = Desc(new_desc)
                if new_tags:
                    note.tags = [Tag(tag) for tag in new_tags]
                return
        raise NoteNotExistError(f"Note with title '{title}' not found.")

    def find_notes(self, key_word) -> list:
        found_notes = []
        _key_word = key_word.lower()

        for note in self.data:
            matched_title = _key_word in note.title.value.lower()
            matched_desc = _key_word in note.desc.value.lower()
            matched_tags = list(filter(lambda tag: tag.value.lower() == _key_word, note.tags))

            if matched_title or matched_desc or len(matched_tags) > 0:
                found_notes.append(note)
        return found_notes

    def remove_note(self, title):
        for i, note in enumerate(self.data):
            if note.title.value == title:
                del self.data[i]
                return
        raise NoteNotExistError(f"Note with title '{title}' not found.")


def test_notes():
    notes = Notes()

    # Helper
    def show(title: str):
        print('-' * 10, title, '-' * 10)
        for note in notes.data:
            print(note.title.value, note.desc.value, [tag.value for tag in note.tags])

    # Додавання заміток
    notes.add_note("Shopping list", "Buy milk, bread, eggs", ["shopping", "urgent"])
    notes.add_note("To-Do", "Call John", ["work"])
    show('add_note')

    # Редагування замітки
    notes.edit_note("Shopping list", new_desc="Buy milk, bread, eggs, and cheese")
    notes.edit_note("To-Do", new_tags=["work", "test"])
    show('edit_note')

    # Пошук заміток
    found_notes = notes.find_notes("shopping")
    print('-' * 10, 'find_notes', '-' * 10)
    for note in found_notes:
        print(note.title.value, note.desc.value, [tag.value for tag in note.tags])

    # Видалення всіх замітки
    notes.remove_note("To-Do")
    show('remove_note')


if __name__ == "__main__":
    test_notes()

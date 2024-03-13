from collections import UserDict, UserList
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


class CreatedAt(Field):
    def __init__(self):
        data = datetime.now().date()
        self.value = data
        super().__init__(data)


class Note:
    def __init__(self, title: str, desc: str, tags: list):
        self.title = Title(title)
        self.desc = Desc(desc)
        self.tags = [Tag(tag) for tag in tags]
        self.createdAt = CreatedAt()

    def __str__(self):
        tags_str = ', '.join(tag.value for tag in self.tags)
        return ('{:20}{}\n'.format('Title:', self.title.value) +
                '{:20}{}\n'.format('Description:', self.desc.value) +
                '{:20}{}\n'.format('Tags:', tags_str) +
                '{:20}{}\n'.format('Created At:', self.createdAt.value.strftime('%Y-%m-%d'))
                )


class Notes(UserDict):
    def add_note(self, note: Note):
        title = note.title.value
        if title in self.data:
            raise NoteExistsError()
        self.data[title] = note

    def edit_note(self, title, new_title: str = '', new_desc: str = '', new_tags: list = []):
        current_note = self.data[title]

        if not current_note:
            raise NoteNotExistError()

        if new_title:
            current_note.title = Title(new_title)
        if new_desc:
            current_note.desc = Desc(new_desc)
        if new_tags:
            current_note.tags = [Tag(tag) for tag in new_tags]
        return

    def find_notes(self, key_word) -> list:
        _key_word = key_word.lower()

        def match_notes(title):
            note = self.data[title]
            matched_title = _key_word in note.title.value.lower()
            matched_desc = _key_word in note.desc.value.lower()
            matched_tags = list(filter(lambda tag: tag.value.lower() == _key_word, note.tags))

            if matched_title or matched_desc or matched_tags:
                return note

        return list(filter(lambda title: match_notes(title), self.data))

    def remove_note(self, title):
        del self.data[title]


def test_notes():
    notes = Notes()

    # Helper
    def show(title: str):
        print('-' * 10, title, '-' * 10)
        for title in notes.data:
            note = notes.data[title]
            print(note.title.value, note.desc.value, [tag.value for tag in note.tags])

    # Додавання заміток
    notes.add_note(Note("Shopping list", "Buy milk, bread, eggs", ["shopping", "urgent"]))
    notes.add_note(Note("To-Do", "Call John", ["work"]))
    show('add_note')

    # Редагування замітки
    notes.edit_note("Shopping list", new_desc="Buy milk, bread, eggs, and cheese")
    notes.edit_note("To-Do", new_tags=["work", "test"])
    show('edit_note')

    # Пошук заміток
    found_notes = notes.find_notes("shopping")
    print('-' * 10, 'find_notes', '-' * 10)

    for title in found_notes:
        note = notes[title]
        print(note.title.value, note.desc.value, [tag.value for tag in note.tags])

    # Видалення всіх замітки
    notes.remove_note("To-Do")
    show('remove_note')


if __name__ == "__main__":
    test_notes()

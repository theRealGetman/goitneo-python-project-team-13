from src.fake_utils import create_fake_contacts, create_fake_notes
import src.handlers as handlers
from src.local_storage import save_book, save_notes
from src.utils import commands_completer, welcome
from prompt_toolkit import prompt


def parse_input(user_input: str):
    if user_input.strip() == '':
        return '', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print(welcome)
    handlers.print_help()
    while True:
        user_input = prompt("Enter a command: ", completer=commands_completer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(handlers.close())
            break
        elif command == "hello":
            print(handlers.hello())
        elif command == "add-contact":
            name = input("Enter name: ")
            if handlers.is_contact_already_exist(name):
                print(f'Contact {name} already exists')
                continue
            phone = input("Enter phone: ")
            email = input("Enter email (empty to skip): ")
            birthday = input("Enter birthday (empty to skip): ")
            print(handlers.add_contact(name, phone, email, birthday))
        elif command == "change-contact":
            name = input("Enter name: ")
            if not handlers.is_contact_already_exist(name):
                print(f'Contact {name} not exists')
                continue
            old_phone = input("Enter old phone: ")
            new_phone = input("Enter new phone: ")
            print(handlers.change_contact(name, old_phone, new_phone))
        elif command == "remove-contact":
            print(handlers.remove_contact(args))
        elif command == "find-contact":
            print(handlers.find_contact(args))
        elif command == "all-contacts":
            print(handlers.show_all())
        elif command == "add-birthday":
            print(handlers.add_birthday(args))
        elif command == "show-birthday":
            print(handlers.show_birthday(args))
        elif command == "birthdays":
            print(handlers.get_birthdays_per_day(args))
        elif command == "add-email":
            print(handlers.add_email(args))
        elif command == "show-email":
            print(handlers.show_email(args))
        elif command == "change-email":
            print(handlers.change_email(args))
        elif command == "add-note":
            title = input("Enter note title: ")
            if handlers.is_note_already_exist(title):
                print(handlers.note_already_exist(title))
                continue
            desc = input("Enter note content: ")
            tags = input("Enter note tags (leave emplty if none): ")

            print(handlers.add_note([title, desc, tags]))
        elif command == "edit-note":
            old_title = input("Enter note title: ")
            if not handlers.is_note_already_exist(old_title):
                print(handlers.note_doesnt_exist(old_title))
                continue

            new_title = input("Enter note new title: ")
            if handlers.is_note_already_exist(new_title):
                print(handlers.note_already_exist(new_title))
                continue

            desc = input("Enter note new content: ")
            tags = input("Enter note new tags (leave emplty if none): ")

            print(handlers.edit_note(old_title, new_title, desc, tags))
        elif command == "show-notes":
            print(handlers.show_notes(args))
        elif command == "remove-note":
            title = input("Enter note title: ")
            if not handlers.is_note_already_exist(title):
                print(handlers.note_doesnt_exist(title))
                continue
            print(handlers.remove_note(title))
        elif command == "help":
            handlers.print_help()
        elif command == "generate-fakes":
            create_fake_contacts()
            save_book()
            create_fake_notes()
            save_notes()
        else:
            print(handlers.invalid_command())
        save_book()
        save_notes()


if __name__ == "__main__":
    main()

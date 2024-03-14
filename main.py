import src.handlers as handlers
from src.local_storage import save_book, save_notes
from src.utils import commands_completer
from prompt_toolkit import prompt


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    handlers.print_help()
    while True:
        user_input = prompt("Enter a command: ", completer=commands_completer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(handlers.close())
            break
        elif command == "hello":
            print(handlers.hello())
        elif command == "add":
            print(handlers.add_contact(args))
        elif command == "change":
            print(handlers.change_contact(args))
        elif command == "phone":
            print(handlers.show_phone(args))
        elif command == "all":
            print(handlers.show_all())
        elif command == "add-birthday":
            print(handlers.add_birthday(args))
        elif command == "show-birthday":
            print(handlers.show_birthday(args))
        elif command == "birthdays":
            print(handlers.birthdays())
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
                print(handlers.note_doesnt_exist(new_title))
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
            print(handlers.remove_note(args))
        elif command == "help":
            handlers.print_help()
        else:
            print(handlers.invalid_command())
        save_book()
        save_notes()


if __name__ == "__main__":
    main()

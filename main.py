import src.handlers as handlers
from src.local_storage import save_book
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
        elif command == "add-contact":
            print(handlers.add_contact(args))
        elif command == "change-contact":
            print(handlers.change_contact(args))
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
        elif command == "help":
            handlers.print_help()
        else:
            print(handlers.invalid_command())
        save_book()


if __name__ == "__main__":
    main()

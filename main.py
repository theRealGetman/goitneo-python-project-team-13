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
        elif command == "add":
            print(handlers.add_contact(args))
        elif command == "change":
            print(handlers.change_contact(args))
        elif command == "remove-contact":
            print(handlers.remove_contact(args))
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
        elif command == "add-email":
            print(handlers.add_email(args))
        elif command == "show-email":
            print(handlers.show_email(args))
        elif command == "change-email":
            print(handlers.change_email(args))
        elif command == "help":
            handlers.print_help()        
        else:
            print(handlers.invalid_command())
        save_book()


if __name__ == "__main__":
    main()

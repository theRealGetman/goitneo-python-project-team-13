import src.handlers as handlers
from src.local_storage import save_book


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
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
        else:
            print(handlers.invalid_command())
        save_book()


if __name__ == "__main__":
    main()

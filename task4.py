def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].casefold()
    args = parts[1:]
    return command, args


def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid input. Please provide both name and phone number."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid input. Please provide both name and new phone number."
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    if len(args) < 1:
        return "Invalid input. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    output = ''
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output


def main():
    contacts = {}
    print("Welcome to the bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good-bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

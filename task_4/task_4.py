from pathlib import Path

# Функція для розбору введених користувачем команд
def parse_input(user_input):
    parts = user_input.split()
    if not parts:  # Якщо parts пустий список, повертаємо команду "" і пустий список аргументів
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, *args

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments provided."
    return inner

# Додавання контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

# Отримання контакту
@input_error
def get_contact(name, contacts):
    return contacts.get(name)

# Редагування контакту
@input_error
def edit_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    raise KeyError

# Видалення контакту
@input_error
def delete_contact(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"Contact {name} deleted."
    raise KeyError

# Перегляд контакту
@input_error
def view_contact(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    contact = get_contact(name, contacts)
    return f"{name}: {contact}" if contact else f"Contact {name} not found."

# Пошук контактів
@input_error
def search_contacts(args, contacts):
    if len(args) != 1:
        raise ValueError
    term = args[0]
    results = {name: phone for name, phone in contacts.items() if term in name or term in phone}
    
    if results:
        return "\n".join(f"{name}: {phone}" for name, phone in results.items())
    return "No matching contacts found."

# Виведення всіх контактів
@input_error
def list_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Допомога
@input_error
def show_help():
    commands = {
        "hello": "Say hi",
        "all": "View all contacts",
        "add": "Add a contact (add <name> <phone>)",
        "view": "View a contact (view <name>)",
        "search": "Search for a contact (search <term>)",
        "edit": "Edit a contact (edit <name> <new_phone>)",
        "delete": "Delete a contact (delete <name>)",
        "exit/close": "Exit the program",
        "help": "Show this help"
    }
    return "\nAvailable commands:\n" + "\n".join(f"  {cmd} - {desc}" for cmd, desc in commands.items())

# Головна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print(show_help())

    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "add":
                print(add_contact(args, contacts))
            case "view":
                print(view_contact(args, contacts))
            case "search":
                print(search_contacts(args, contacts))
            case "edit":
                print(edit_contact(args, contacts))
            case "delete":
                print(delete_contact(args, contacts))
            case "all":
                print(list_contacts(contacts))
            case "help":
                print(show_help())
            case "exit" | "close":
                print("Goodbye!")
                break
            case "hello":
                print("How can I help you?")
            case _:
                print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

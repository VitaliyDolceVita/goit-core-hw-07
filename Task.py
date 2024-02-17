
from datetime import datetime

class Birthday:
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_birthday(self, value):
        self.birthday = Birthday(value)


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            # реалізація

        elif command == "show-birthday":
            # реалізація

        elif command == "birthdays":
            # реалізація

        else:
            print("Invalid command.")


# Декоратор для обробки помилок введення користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def parse_input(command):
    # Перетворюємо введену команду у нижній регістр для зручності порівняння.
    parts = command.split()
    # Перевіряємо, яка команда була введена та викликаємо відповідну функцію.
    if parts[0] == "hello":
        return "How can I help you?"
    elif parts[0] == "add" and len(parts) == 3:
        if parts[2].isdigit(): 
            return add_contact(parts[1], parts[2])
        else:   # Якщо телефон не є цифрами
            return "Phone number is not digit."  # Повідомляємо користувача 
    elif parts[0] == "change" and len(parts) == 3:
        return change_contact(parts[1], parts[2])
    elif parts[0] == "phone" and len(parts) == 2:
        return show_phone(parts[1])
    elif parts[0] == "all":
        return show_all()
    elif parts[0] == "exit" or parts[0] == "close":
        return "Good bye!"
    else:
        return "Enter the argument for the command"

# Функція для додавання нового контакту до словника.
@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номера телефону існуючого контакту.
@input_error
def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

# Функція для відображення номера телефону за ім'ям контакту.
@input_error
def show_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Функція для відображення всіх контактів.
@input_error
def show_all():
    if contacts:
        # Формуємо рядок з усіма контактами для виводу.
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


# Основна функція для управління основним циклом обробки команд.
def main():
    contacts = {}  #  створюємо порожній словник для зберігання контактів
    while True:
        # Зчитуємо введену користувачем команду.
        command = input("Enter command: ")
        # Розбираємо введену команду та отримуємо відповідь.
        response = parse_input(command)
        # Виводимо відповідь користувачеві.
        print(response)
        # Якщо користувач ввів "exit" або "close", завершуємо виконання програми.
        if response == "Good bye!":
            break


# Перевіряємо, чи цей скрипт є основним і викликаємо функцію main.
if __name__ == "__main__":
    main()

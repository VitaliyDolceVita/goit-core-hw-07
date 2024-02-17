from collections import UserDict   # Імпортуєм необхідну функцію модуля


class Field:   # Створюємо клас Field
    def __init__(self, value):  # Ініціація класу
        self.value = value  # Присвоєння значення атрибуту value

    def __str__(self):  # Оголошення методу для конвертації об'єкта в рядок 
        return str(self.value)  


class Name(Field):  # Створюєм клас Name який наслідує клас  Field
    def __init__(self, name):
        self.name = name


class Phone(Field):   # Створюєм клас Name який наслідує клас  Field
    def __init__(self, value):  # Оголошення конструктора класу з аргументом value
        super().__init__(value)  # Виклик конструктора батьківського класу Field з передачею значення value
        if not self.is_valid():
            raise ValueError("Invalid phone number format. Please provide a 10-digit phone number.")  # виклик винятку, якщо номер телефону некоректний


    def is_valid(self):  # Оголошення методу для перевірки валідності номера телефону
    return len(self.value) == 10 and self.value.isdigit()  # Повертає True, якщо довжина номера телефону дорівнює 10 і всі символи є цифрами, інакше повертає False


class Record:  # Оголошення класу Record
    def __init__(self, name):  # Оголошення конструктора класу з аргументом name
        self.name = Name(name)  # Створення об'єкту класу Name з переданим ім'ям
        self.phones = []  # Ініціалізація порожнього списку для зберігання телефонів

    def add_phone(self, phone):  # Оголошення методу для додавання телефону до запису
        self.phones.append(Phone(phone))  # Додавання нового телефону до списку телефонів запису

    def remove_phone(self, phone):  # Оголошення методу для видалення телефону з запису
        self.phones = [p for p in self.phones if p.value != phone]  # Видалення телефону зі списку телефонів запису, якщо він співпадає з переданим

    def edit_phone(self, old_phone, new_phone):  # Оголошення методу для редагування телефону
        for p in self.phones:  # Ітерація по всіх телефонах запису
            if p.value == old_phone:  # Якщо знайдено телефон, який потрібно змінити
                p.value = new_phone  # Заміна старого значення телефону на нове
                break  # Виходимо з циклу після зміни

    def find_phone(self, phone):  # Оголошення методу для пошуку телефону в записі
        for p in self.phones:  # Ітерація по всіх телефонах запису
            if p.value == phone:  # Якщо знайдено шуканий телефон
                return p  # Повертаємо його
        return None  # Повертаємо None, якщо телефон не знайдено

    def __str__(self):  # Оголошення методу для конвертації об'єкту в рядок
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"  # Повертає рядок з ім'ям та списком телефонів запису



class AddressBook(UserDict):  # Оголошення класу AddressBook, що успадковує клас UserDict
    def add_record(self, record):  # Оголошення методу для додавання запису до адресної книги
        self.data[record.name.value] = record  # Додавання запису до словника адресної книги, використовуючи ім'я як ключ

    def find(self, name):  # Оголошення методу для пошуку запису за ім'ям у адресній книзі
        return self.data.get(name)  # Повернення запису за вказаним ім'ям, якщо він існує у книзі

    def delete(self, name):  # Оголошення методу для видалення запису за ім'ям з адресної книги
        if name in self.data:  # Перевірка, чи ім'я присутнє у книзі
            del self.data[name]  # Видалення запису з книги, якщо воно присутнє

    def __str__(self):  # Оголошення методу для конвертації об'єкту в рядок
        return "\n".join(str(record) for record in self.data.values())  # Повертає рядок, складений з рядків, які представляють кожен запис у словнику адресної книги
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
    parts = command.split()
    return parts[0] 

        
@input_error
def parse_input1(command):
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

        elif command == "add" and len(parts) == 3:
            if parts[2].isdigit(): 
                return add_contact(parts[1], parts[2])
            else:   # Якщо телефон не є цифрами
                return "Phone number is not digit."  # Повідомляємо користувача 

        elif command == "change" and len(parts) == 3:
        return change_contact(parts[1], parts[2])

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

# Основна функція для управління основним циклом обробки команд.
def main():
    # contacts = {}  #  створюємо порожній словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        # Зчитуємо введену користувачем команду.
        command = input("Enter command: ")
        # Розбираємо введену команду та отримуємо відповідь.
        response = parse_input1(command)
        # Виводимо відповідь користувачеві.
        print(response)
        # Якщо користувач ввів "exit" або "close", завершуємо виконання програми.
        if response == "Good bye!":
            break


# Перевіряємо, чи цей скрипт є основним і викликаємо функцію main.
if __name__ == "__main__":
    main()

import json
from users import Admin, Employee, User
from orders import OrderSystem
from finances import Finance
from reports import ReportGenerator
from product_manager import ProductManager  # Importuj klasę ProductManager

# Funkcja logowania
def login(users):
    username = input("Podaj nazwę użytkownika: ")
    password = input("Podaj hasło: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            if user['role'] == 'admin':
                return Admin(user['username'], user['password'])
            elif user['role'] == 'employee':
                return Employee(user['username'], user['password'])
            else:
                return User(user['username'], user['password'])
    print("Niepoprawne dane logowania.")
    return None

# Ładowanie użytkowników z pliku JSON
def load_users():
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Brak pliku z danymi użytkowników.")
        return []

# Funkcje dla administratora
def admin_functions(report_gen):
    print("Funkcje Administratora:")
    print("1. Wyświetl raport")
    print("2. Zarządzaj użytkownikami")
    print("3. Zarządzaj finansami")
    print("4. Zarządzaj produktami")  # Nowa opcja dla zarządzania produktami
    
    choice = input("Wybierz opcję: ")

    if choice == '1':
        report_gen.save_report_to_file()
    elif choice == '2':
        manage_users()
    elif choice == '3':
        manage_finances()
    elif choice == '4':
        manage_products()  # Wywołanie funkcji zarządzania produktami
    else:
        print("Niepoprawny wybór.")

# Funkcje dla pracowników
def employee_functions():
    print("Funkcje Pracownika:")
    print("1. Składaj zamówienia")
    print("2. Wyświetl raport finansowy")
    
    choice = input("Wybierz opcję: ")

    if choice == '1':
        place_order()
    elif choice == '2':
        finance = Finance()
        finance.view_balance()
    else:
        print("Niepoprawny wybór.")

# Funkcja do zarządzania użytkownikami
def manage_users():
    users = load_users()  # Ładuj użytkowników
    while True:
        print("\nZarządzanie Użytkownikami:")
        print("1. Dodaj użytkownika")
        print("2. Edytuj użytkownika")
        print("3. Usuń użytkownika")
        print("4. Wyświetl wszystkich użytkowników")
        print("5. Powrót do menu administratora")
        
        choice = input("Wybierz opcję: ")

        if choice == '1':
            add_user(users)
        elif choice == '2':
            edit_user(users)
        elif choice == '3':
            delete_user(users)
        elif choice == '4':
            display_users(users)
        elif choice == '5':
            break
        else:
            print("Niepoprawny wybór.")

    save_users(users)  # Zapisz zmiany

def add_user(users):
    username = input("Podaj nazwę użytkownika: ")
    password = input("Podaj hasło: ")
    role = input("Podaj rolę (admin, employee, user): ")

    new_user = {
        'username': username,
        'password': password,
        'role': role
    }
    users.append(new_user)
    print(f"Użytkownik {username} dodany.")

def edit_user(users):
    username = input("Podaj nazwę użytkownika do edycji: ")
    for user in users:
        if user['username'] == username:
            password = input("Podaj nowe hasło (lub naciśnij Enter, aby pominąć): ")
            role = input("Podaj nową rolę (lub naciśnij Enter, aby pominąć): ")

            if password:
                user['password'] = password
            if role:
                user['role'] = role
            
            print(f"Użytkownik {username} zaktualizowany.")
            return

    print(f"Użytkownik {username} nie znaleziony.")

def delete_user(users):
    username = input("Podaj nazwę użytkownika do usunięcia: ")
    for user in users:
        if user['username'] == username:
            users.remove(user)
            print(f"Użytkownik {username} usunięty.")
            return

    print(f"Użytkownik {username} nie znaleziony.")

def display_users(users):
    print("Lista Użytkowników:")
    for user in users:
        print(f"Nazwa: {user['username']}, Rola: {user['role']}")

def save_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)
    print("Dane użytkowników zapisane.")

# Funkcja do zarządzania finansami
def manage_finances():
    finance = Finance()
    while True:
        print("\nZarządzanie Finansami:")
        print("1. Wyświetl saldo")
        print("2. Dodaj do salda")
        print("3. Usuń z salda")
        print("4. Powrót do menu administratora")
        
        choice = input("Wybierz opcję: ")

        if choice == '1':
            finance.view_balance()
        elif choice == '2':
            amount = float(input("Podaj kwotę do dodania: "))
            finance.add_balance(amount)
        elif choice == '3':
            amount = float(input("Podaj kwotę do usunięcia: "))
            finance.remove_balance(amount)
        elif choice == '4':
            break
        else:
            print("Niepoprawny wybór.")

# Funkcja do zarządzania produktami
def manage_products():
    product_manager = ProductManager()  # Utworzenie instancji ProductManager
    
    while True:
        print("\nZarządzanie Produktami:")
        print("1. Dodaj produkt")
        print("2. Edytuj produkt")
        print("3. Usuń produkt")
        print("4. Wyświetl produkty")
        print("5. Powrót do menu administratora")
        
        choice = input("Wybierz opcję: ")

        if choice == '1':
            name = input("Podaj nazwę produktu: ")
            price = float(input("Podaj cenę produktu: "))
            available = int(input("Podaj dostępność produktu: "))
            product_id = len(product_manager.products) + 1  # Przydziel ID na podstawie liczby produktów
            new_product = {'id': product_id, 'name': name, 'price': price, 'available': available}
            product_manager.add_product(new_product)

        elif choice == '2':
            product_id = int(input("Podaj ID produktu do edytowania: "))
            name = input("Podaj nową nazwę produktu: ")
            price = float(input("Podaj nową cenę produktu: "))
            available = int(input("Podaj nową dostępność produktu: "))
            updated_product = {'id': product_id, 'name': name, 'price': price, 'available': available}
            product_manager.edit_product(product_id, updated_product)

        elif choice == '3':
            product_id = int(input("Podaj ID produktu do usunięcia: "))
            product_manager.remove_product(product_id)

        elif choice == '4':
            product_manager.view_products()

        elif choice == '5':
            break

        else:
            print("Niepoprawny wybór.")

def load_products():
    try:
        with open('data/products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Brak pliku z produktami.")
        return []

# Funkcja do składania zamówień
def place_order():
    print("Składanie zamówienia:")
    products = load_products()  # Ładowanie produktów
    for product in products:
        print(f"{product['id']}: {product['name']} - {product['price']} PLN (Dostępne: {product['available']})")
    
    product_id = int(input("Podaj ID produktu: "))
    quantity = int(input("Podaj ilość: "))

    # Ładowanie stanu finansów
    finance = Finance()
    
    # Sprawdzenie, czy produkt istnieje
    selected_product = next((product for product in products if product['id'] == product_id), None)

    if not selected_product:
        print("Produkt o podanym ID nie istnieje.")
        return

    # Obliczanie łącznej ceny
    total_price = selected_product['price'] * quantity

    # Sprawdzenie dostępności produktu
    if quantity > selected_product['available']:
        print("Niewystarczająca ilość produktu w magazynie.")
        return

    # Sprawdzenie, czy mamy wystarczające środki
    if total_price > finance.view_balance():
        print("Brak wystarczających środków na koncie.")
        return

    # Dodawanie zamówienia
    order_system = OrderSystem()  # Utworzenie instancji OrderSystem
    order_system.add_order(product_id, quantity)

    # Aktualizacja salda
    finance.remove_balance(total_price)  # Odejmowanie od salda
    selected_product['available'] -= quantity  # Zmniejszanie stanu produktu
    print(f"Zamówienie dodane: Produkt ID {product_id}, Ilość: {quantity}, Łączny koszt: {total_price:.2f} PLN")

def main():
    users = load_users()
    
    print("Witamy w systemie zarządzania firmą!")
    
    user = None
    while user is None:
        user = login(users)

    report_gen = ReportGenerator(users)  # Tworzenie instancji ReportGenerator

    if isinstance(user, Admin):
        print("Zalogowano jako Admin.")
        admin_functions(report_gen)  # Przekazanie obiektu report_gen do funkcji
    elif isinstance(user, Employee):
        print("Zalogowano jako Pracownik.")
        employee_functions()
    else:
        print("Zalogowano jako Użytkownik.")
        # Dla zwykłych użytkowników mogą być ograniczone funkcje

if __name__ == "__main__":
    main()

import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def view_profile(self):
        print(f"Profil użytkownika: {self.username}")
    
    def change_password(self, new_password):
        self.password = new_password
        print("Hasło zostało zmienione.")
        self._save_users()

    def _save_users(self):
        with open('data/users.json', 'r') as file:
            users = json.load(file)
        
        for user in users:
            if user['username'] == self.username:
                user['password'] = self.password
        
        with open('data/users.json', 'w') as file:
            json.dump(users, file, indent=4)

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def view_all_users(self):
        with open('data/users.json', 'r') as file:
            users = json.load(file)
        print("Lista użytkowników:")
        for user in users:
            print(f"Użytkownik: {user['username']}, Rola: {user['role']}")

    def change_user_role(self, username, new_role):
        with open('data/users.json', 'r') as file:
            users = json.load(file)
        
        for user in users:
            if user['username'] == username:
                user['role'] = new_role
        
        with open('data/users.json', 'w') as file:
            json.dump(users, file, indent=4)
        
        print(f"Zmieniono rolę użytkownika {username} na {new_role}.")

class Employee(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def place_order(self, product_name, quantity):
        # Funkcja do składania zamówień (do zaimplementowania w orders.py)
        pass

    def view_products(self):
        # Funkcja do przeglądania produktów (do zaimplementowania w products.py)
        pass

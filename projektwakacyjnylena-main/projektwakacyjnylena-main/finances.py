import json

class Finance:
    def __init__(self):
        self.balance = self.load_balance()

    def load_balance(self):
        try:
            with open('data/finances.json', 'r') as file:
                data = json.load(file)
                return data.get('balance', 0)
        except FileNotFoundError:
            return 0  # Domyślna wartość salda, jeśli plik nie istnieje

    def view_balance(self):
        print(f"Aktualne saldo: {self.balance} PLN")
        return self.balance  # Zwracanie aktualnego salda

    def add_balance(self, amount):
        if amount < 0:
            print("Kwota do dodania musi być większa od 0.")
            return
        self.balance += amount
        self.save_balance()
        print(f"Do salda dodano: {amount} PLN. Nowe saldo: {self.balance} PLN")

    def remove_balance(self, amount):
        if amount < 0:
            print("Kwota do usunięcia musi być większa od 0.")
            return
        if amount > self.balance:
            print("Nie można usunąć więcej niż aktualne saldo.")
        else:
            self.balance -= amount
            self.save_balance()
            print(f"Z salda usunięto: {amount} PLN. Nowe saldo: {self.balance} PLN")

    def save_balance(self):
        with open('data/finances.json', 'w') as file:
            json.dump({'balance': self.balance}, file, indent=4)
        print("Saldo zapisane.")

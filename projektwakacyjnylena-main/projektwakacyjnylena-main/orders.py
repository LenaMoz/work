import json
from products import Product

class OrderSystem:
    def __init__(self):
        self.orders = self.load_orders()

    def load_orders(self):
        try:
            with open('data/orders.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Domyślna wartość zamówień, jeśli plik nie istnieje

    def add_order(self, product_id, quantity):
        products = self.load_products()  # Załaduj dostępne produkty
        product = self.find_product(products, product_id)
        
        if product:
            if product['available'] >= quantity:
                total_price = product['price'] * quantity
                product['available'] -= quantity
                
                self.save_orders(product, quantity, total_price)
                self.save_products(products)  # Zapisz zmiany w pliku produktów
                print(f"Zamówienie złożone: {quantity} x {product['name']} za {total_price:.2f} PLN")
            else:
                print("Niedostateczna ilość produktu.")
        else:
            print("Produkt nie znaleziony.")

    def find_product(self, products, product_id):
        for product in products:
            if product['id'] == product_id:
                return product
        return None

    def load_products(self):
        try:
            with open('data/products.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Brak pliku z produktami.")
            return []

    def save_orders(self, product, quantity, total_price):
        order = {
            'product_name': product['name'],
            'quantity': quantity,
            'total_price': total_price
        }
        self.orders.append(order)
        with open('data/orders.json', 'w') as file:
            json.dump(self.orders, file, indent=4)

    def save_products(self, products):
        with open('data/products.json', 'w') as file:
            json.dump(products, file, indent=4)  # Zapisz zmiany w pliku produktów

    def view_orders(self):
        print("Złożone zamówienia:")
        for order in self.orders:
            print(f"Produkt: {order['product_name']}, Ilość: {order['quantity']}, Cena całkowita: {order['total_price']:.2f} PLN")

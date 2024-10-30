import json

class ProductManager:
    def __init__(self, filepath='data/products.json'):
        self.filepath = filepath
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Domyślna wartość, jeśli plik nie istnieje

    def save_products(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.products, file, indent=4)
        print("Produkty zapisane.")

    def add_product(self, product):
        self.products.append(product)
        self.save_products()
        print(f"Produkt dodany: {product['name']}")

    def edit_product(self, product_id, updated_product):
        for index, product in enumerate(self.products):
            if product['id'] == product_id:
                self.products[index] = updated_product
                self.save_products()
                print(f"Produkt zaktualizowany: {updated_product['name']}")
                return
        print("Produkt nie znaleziony.")

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product['id'] != product_id]
        self.save_products()
        print(f"Produkt o ID {product_id} usunięty.")

    def view_products(self):
        print("Lista produktów:")
        for product in self.products:
            print(f"ID: {product['id']}, Nazwa: {product['name']}, Cena: {product['price']} PLN, Dostępne: {product['available']}")

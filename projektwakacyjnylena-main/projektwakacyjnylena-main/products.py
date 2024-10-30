import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        self.stock = new_stock
        print(f"Zaktualizowano stan magazynowy dla {self.name} na {self.stock} szt.")
        self._save_products()

    def update_price(self, new_price):
        self.price = new_price
        print(f"Zaktualizowano cenę dla {self.name} na {self.price} PLN.")
        self._save_products()

    def _save_products(self):
        with open('data/products.json', 'r') as file:
            products = json.load(file)
        
        for product in products:
            if product['product_id'] == self.product_id:
                product['stock'] = self.stock
                product['price'] = self.price

        with open('data/products.json', 'w') as file:
            json.dump(products, file, indent=4)

# Funkcja do ładowania produktów z pliku JSON
def load_products():
    try:
        with open('data/products.json', 'r') as file:
            products_data = json.load(file)
            return [Product(**prod) for prod in products_data]
    except FileNotFoundError:
        print("Brak pliku z produktami.")
        return []

# Funkcja do wyświetlania listy produktów
def display_products():
    products = load_products()
    print("Dostępne produkty:")
    for product in products:
        print(f"{product.product_id}. {product.name} - {product.price} PLN, Magazyn: {product.stock} szt.")

# Funkcja do dodawania nowego produktu
def add_product(product_id, name, price, stock):
    new_product = Product(product_id, name, price, stock)
    
    products = load_products()
    products.append(new_product)

    with open('data/products.json', 'w') as file:
        json.dump([prod.__dict__ for prod in products], file, indent=4)

    print(f"Dodano produkt: {name}, Cena: {price} PLN, Stan magazynowy: {stock} szt.")

# Assumptions for Inventory Class:
# - Product has: product_id, name, price, quantity, expiry_date.
# - Sale will call Inventory to reduce stock using product_id and quantity_sold.
# - Inventory will store products in a dictionary keyed by product_id.
# - Low stock threshold = 10 units.
# - No negative quantities allowed.
# - Expired products are flagged when checked.

from datetime import date
class Product:
    def __init__(self, product_id, batch_number, name, price, quantity, expiry_date):
        self.product_id = product_id           # Unique identifier for the product
        self.batch_number = batch_number       # Identifies the batch of the product
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date

class Inventory:
    def __init__(self, low_stock_threshold):
        self.products = {}                                 # A dictionary for the products keys and values.
        self.low_stock_threshold = 10                      # When the quantity is 10 units and above, it is normal stock and less than 10 units is low stock.

    def add_product(self, product):
        product_key = (product.product_id, product.batch_number)      # product_key is the unique identifier for a product batch so the inventory can track multiple batches of the same product.

        if product_key in self.products:       # If Product exists already
            print("Product already added.")
            return False
        if product.quantity < 0:               # Makes sure the quantity is not negative
            print("Quantity must be positive")
            return False
        if product.price <= 0:                 # Ensures the price of the product is zero and above and not negative.
            print("Price must be positive")
            return False
        # If Product is not in the inventory
        self.products[product_key] = product   # self.products[product.product_id, product.batch_number] = Product(product_id, batch_number, name, price, quantity, expiry_date)
        print(f"Product with ID {product.product_id} and {product.batch_number} added successfully.")
        return True

    def find_product(self, product_id, batch_number):    # Way of filtering the products using product key.
        product_key = (product_id, batch_number)
        return self.products.get(product_key, None)      # .get returns the value if the key exists and return None if no key exist so the system does not crash.

    def remove_product(self, product_id, batch_number):
        product_key = (product_id, batch_number)
        if product_key in self.products:
            del self.products[product_key]
            print("Product removed successfully")
            return True
        else:
            print("Product not found")
            return False

    def update_stock(self, product_id, batch_number, choice, quantity):
        product_key = (product_id, batch_number)

        # Check if the product exists in the inventory.
        # If not, print an error message and return False to indicate the update failed.

        if product_key not in self.products:
            print(f"Stock not updated. This product with ID {product_id} not found")
            return False

        product = self.products[product_key]

        # Blocking entry of any expired product.
        if product.expiry_date < date.today():
            print(f"Stock update declined. The product with ID {product_id} is expired.")
            return False

        choice = choice.lower()
        # I used if-elif-else because it allows multiple conditional checks
        if choice == "set new quantity":
            if quantity >= 0:
                product.quantity = quantity # e.g. the product quantity = 50
                print(f"Stock updated. {product.name} now has {product.quantity} units in stock")
                return True
            else:
                print("Quantity must be zero or greater than zero")
                return False

        elif choice == "increase":
            if quantity > 0:
                product.quantity += quantity
                print(f"Increased {product.name} stock by {quantity}")
                return True
            else:
                print("Increase must be a positive integer")
                return False

        elif choice == "decrease":
            if quantity <= 0:
                print("Decrease must be positive")
                return False
            else:
                if quantity > product.quantity:
                    print("Quantity can not be decreased than stock available")
                    return False
                else:
                    product.quantity -= quantity
                    print(f"Decreased {product.name} stock by {quantity}")
                    return True
        else:
            print("Invalid choice. Must be either 'Set new quantity' or 'Increase' or 'Decrease'")
            return False

    def get_low_stock_products(self):
        low_stock_products = {}
        for product_key, product in self.products.items():
            if product.quantity <= self.low_stock_threshold:
                low_stock_products[product_key] = product
        return low_stock_products

    def get_expired_products(self):
        expired_products = {}
        today = date.today()
        for product_key, product in self.products.items():
            if product.expiry_date < today:
                expired_products[product_key] = product
        return expired_products

    def get_all_products(self):
        if not self.products:  # Checks if the list is empty
            print("\nNo product in inventory yet.")
            return
        # Print table header
        print(f"{'No.':<5}|{'Product ID':<10}|{'Batch':<8}|{'Name':<15}|{'Price(Mur)':<12}|{'Quantity':<10}|{'Expiry':<12}")
        print("-" * 70)
        for index, (product_key, product) in enumerate(self.products.items(), start=1):
        # Loop through all products in the inventory, giving each one a numbered index starting from 1.
            print(f"{index:<5}|{product.product_id:<10}|{product.batch_number:<8}|{product.name:<15}|"
                  f"{product.price:<12}|{product.quantity:<10}|{product.expiry_date:<12}")
    def all_products_summary(self):
        print("\nYour products inventory summary")
        unique_count = len(self.products) # How many different batches do we have?
        total_quantity = sum(product.quantity for product in self.products.values()) # How much stock do we have in total?
        low_stock_count = len(self.get_low_stock_products()) # What needs restocking soon?
        expired_count = len(self.get_expired_products()) # What products needs to be flagged or removed?
        # ALL PRODUCTS SUMMARY TABLE
        print(f"{'Unique Products':<16}|{'Total Quantity':<15}|{'Low Stocks':<11}|{'Expired Products ':<12}")
        print("-" * 60)
        print(f"{unique_count:<16}|{total_quantity:<15}|{low_stock_count:<11}|{expired_count:<12}")

    def product_sale(self, product_id, batch_number, quantity):
        product_key = (product_id, batch_number)
        if product_key not in self.products:         # Checks if the product exists. If it doesn’t exist, prints a clear error message and stops the sale.
            print("Product not found in inventory.")
            return False
        product = self.products[product_key]
        if product.expiry_date < date.today():   # Checks the product’s expiry date. If the product is expired, the sale is blocked and a message is shown.
            print(f"Sale failed: The product with ID {product_id} is expired.")
            return False
        if quantity <= 0:
            print(f"Sale failed: The quantity must be positive")
            return False
        if product.quantity < quantity:
            print(f"Sale failed: Only {product.quantity} units available for {product.name}.")
            return False
        product.quantity -= quantity
        print(f"Sale successful: Sold {quantity} units of {product.name}."
              f"Stock left {product.quantity} units available for {product.name}.")
        return True

if __name__ == "__main__":
    inventory = Inventory(low_stock_threshold=10)

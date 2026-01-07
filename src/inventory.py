from product import Product
# Assumptions for Inventory Class:
# - Product has: product_id, name, price, quantity, expiry_date.
# - Sale will call Inventory to reduce stock using product_id and quantity_sold.
# - Inventory will store products in a dictionary keyed by product_id.
# - Low stock threshold = 10 units.
# - No negative quantities allowed.
# - Expired products are flagged when checked.

class Inventory:
    def __init__(self, low_stock_threshold):
        self.products = {}
        self.low_stock_threshold = 10

    def add_product(self, product):
        product_key = (product.product_id, product.batch_number)
        self.products[product_key] = product
        return True

    def find_product(self, product_id, batch_number):
        product_key = (product_id, batch_number)
        return self.products.get(product_key, None)

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

        if product_key not in self.products:
            print(f"Stock not updated. This product with ID {product_id} is not found")
            return False
        product = self.products[product_key]
        choice = choice.lower()

        if choice == "set new quantity":
            if quantity >= 0:
                product.quantity = quantity
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
        from datetime import date
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
        print(f"{'No.':<5}{'PRODUCT ID':<10}{'Batch':<8}{'Name':<15}{'Price (Rupees)':<10}{'Quantity':<10}{'Expiry':<12}")
        print("-" * 70)
        for index, (product_key, product) in enumerate(self.products.items(), start=1):
            print(f"{index:<5}|{product.product_id:<5}|{product.batch_number:<8}|{product.name:<15}|"
                  f"{product.price:<10}|{product.quantity:<10}|{product.expiry_date:<12}")

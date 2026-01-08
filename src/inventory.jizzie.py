from product import Product


class Inventory:
    def __init__(self):
        self.products = []  # list of Product objects

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_id, batch_number):
        for product in self.products:
            if product.product_id == product_id and product.batch_number == batch_number:
                return product
        return None

    def get_low_stock_products(self, threshold):
        low_stock = []
        for product in self.products:
            if product.quantity < threshold:
                low_stock.append(product)
        return low_stock

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            print(
                product.product_id,
                product.batch_number,
                product.name,
                product.price,
                product.quantity,
                product.expiry_date
            )

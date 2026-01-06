from datetime import date

class Product:
    def __init__(self, product_id, batch_number, name, price, quantity, expiry_date):
        self.product_id = product_id
        self.batch_number = batch_number
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date  # expected as date object

    def update_quantity(self, amount):
        self.quantity += amount

    def update_price(self, new_price):
        self.price = new_price

    def is_expired(self):
        return date.today() > self.expiry_date

    def is_expiring_soon(self, days):
        remaining_days = (self.expiry_date - date.today()).days
        return 0 <= remaining_days <= days

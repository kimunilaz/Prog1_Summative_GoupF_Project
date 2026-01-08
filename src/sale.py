
from datetime import date
class Sale:
    def _init_(self, product_id, batch_number, quantity_sold, price_per_unit):
        self.product_id = product_id
        self.batch_number = batch_number
        self.quantity_sold = quantity_sold
        self.price_per_unit = price_per_unit
        self.total_price = self.calculate_total()
        self.sale_date = date.today()

    def calculate_total(self):
        return self.quantity_sold * self.price_per_unit

    def to_record(self):
        return {
            "product_id": self.product_id,
            "batch_number": self.batch_number,
            "quantity_sold": self.quantity_sold,
            "total_price": self.total_price,
            "sale_date": self.sale_date
        }

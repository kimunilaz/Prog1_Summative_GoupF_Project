
from datetime import datetime, date

class Sale:
    """
    Represents a sale transaction.

    """
    def __init__(self, sale_id, product_id, batch_number, quantity_sold, price_per_unit, sale_date=None):
        self.sale_id = sale_id                    # Unique sale ID
        self.product_id = product_id              # Product ID sold
        self.batch_number = batch_number          # Batch number of the product
        self.quantity_sold = int(quantity_sold)   # Number of units sold
        self.price_per_unit = float(price_per_unit)  # Price per unit at time of sale
        self.total_price = self.calculate_total()    # Total price of this sale
        # Sale date: today by default, or use provided date
        if sale_date is None:
            self.sale_date = date.today()
        elif isinstance(sale_date, str):
            self.sale_date = datetime.strptime(sale_date, "%Y-%m-%d").date()
        elif isinstance(sale_date, date):
            self.sale_date = sale_date
        else:
            raise ValueError("sale_date must be None, 'YYYY-MM-DD' string, or datetime.date object")

    def calculate_total(self):
        return self.quantity_sold * self.price_per_unit

    def to_record(self):
        """
        Returns a dictionary suitable for writing to CSV.
        """
        return {
            "sale_id": self.sale_id,
            "product_id": self.product_id,
            "batch_number": self.batch_number,
            "quantity_sold": self.quantity_sold,
            "price_per_unit": self.price_per_unit,
            "total_price": self.total_price,
            "sale_date": self.sale_date
        }

    def __str__(self):
        return f"Sale({self.sale_id}, Product: {self.product_id}, Batch: {self.batch_number}, Qty: {self.quantity_sold}, Total: {self.total_price}, Date: {self.sale_date})"

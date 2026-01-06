# shopsystem.py

import csv
from datetime import datetime
from product import Product   # your existing Product class
from sale import Sale         # your existing Sale class

class ShopSystem:
    def __init__(self):
        self.products = []  # list of Product objects
        self.sales = []     # list of Sale objects

    # ----------------- PRODUCTS -----------------
    def load_products(self, filename="products.csv"):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                self.products = []
                for row in reader:
                    try:
                        product = Product(
                            row['product_code'],
                            row['name'],
                            float(row['price']),
                            int(row['quantity']),
                            datetime.strptime(row['expiry_date'], "%Y-%m-%d").date()
                        )
                        self.products.append(product)
                    except (ValueError, KeyError) as e:
                        print(f"Bad data in row {row}: {e}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty product list.")

    def save_products(self, filename="products.csv"):
        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['product_code', 'name', 'price', 'quantity', 'expiry_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for p in self.products:
                    writer.writerow({
                        'product_code': p.product_code,
                        'name': p.name,
                        'price': p.price,
                        'quantity': p.quantity,
                        'expiry_date': p.expiry_date
                    })
        except Exception as e:
            print(f"Error saving products: {e}")

    # ----------------- SALES -----------------
    def load_sales(self, filename="sales.csv"):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                self.sales = []
                for row in reader:
                    try:
                        sale = Sale(
                            row['sale_id'],
                            row['product_code'],
                            int(row['quantity_sold']),
                            datetime.strptime(row['date_of_sale'], "%Y-%m-%d").date()
                        )
                        self.sales.append(sale)
                    except (ValueError, KeyError) as e:
                        print(f"Bad data in row {row}: {e}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty sales list.")

    def save_sales(self, filename="sales.csv"):
        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['sale_id', 'product_code', 'quantity_sold', 'date_of_sale']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for s in self.sales:
                    writer.writerow({
                        'sale_id': s.sale_id,
                        'product_code': s.product_code,
                        'quantity_sold': s.quantity_sold,
                        'date_of_sale': s.date_of_sale
                    })
        except Exception as e:
            print(f"Error saving sales: {e}")


# ----------------- DEMO -----------------
if __name__ == "__main__":
    shop = ShopSystem()

    # Load existing data (or start empty if missing)
    shop.load_products()
    shop.load_sales()

    print("Products Loaded:")
    for p in shop.products:
        print(vars(p))

    print("\nSales Loaded:")
    for s in shop.sales:
        print(vars(s))

    # Example: Add a new product and sale
    from datetime import date
    new_product = Product("P003", "Bread", 1200, 15, date(2026, 1, 10))
    shop.products.append(new_product)

    new_sale = Sale("S003", "P003", 2, date.today())
    shop.sales.append(new_sale)

    # Save changes back to CSV
    shop.save_products()
    shop.save_sales()

    print("\nProducts and Sales saved successfully!")

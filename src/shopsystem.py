# shopsystem.py

import csv
from datetime import datetime, date
from inventory2 import Inventory, Product
from sale import Sale


class ShopSystem:
    def __init__(self):
        # Inventory manages products & stock
        self.inventory = Inventory(low_stock_threshold=10)

        # List of Sale objects
        self.sales = []

    # ----------------- PRODUCTS -----------------
    def load_products(self, filename="products.csv"):
        try:
            with open(filename, newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        product = Product(
                            row["product_id"],
                            row["batch_number"],
                            row["name"],
                            float(row["price"]),
                            int(row["quantity"]),
                            datetime.strptime(row["expiry_date"], "%Y-%m-%d").date()
                        )
                        self.inventory.add_product(product)

                    except (ValueError, KeyError) as e:
                        print(f"Bad product data skipped: {row} → {e}")

        except FileNotFoundError:
            print("products.csv not found. Inventory starts empty.")

    def save_products(self, filename="products.csv"):
        try:
            with open(filename, "w", newline="") as file:
                fieldnames = [
                    "product_id",
                    "batch_number",
                    "name",
                    "price",
                    "quantity",
                    "expiry_date"
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for (product_id, batch_number), product in self.inventory.products.items():
                    writer.writerow({
                        "product_id": product.product_id,
                        "batch_number": product.batch_number,
                        "name": product.name,
                        "price": product.price,
                        "quantity": product.quantity,
                        "expiry_date": product.expiry_date
                    })

        except Exception as e:
            print(f"Error saving products: {e}")

    # ----------------- SALES -----------------
    def load_sales(self, filename="sales.csv"):
        try:
            with open(filename, newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        sale = Sale(
                            row["sale_id"],
                            row["product_id"],
                            row["batch_number"],
                            int(row["quantity_sold"]),
                            datetime.strptime(row["date_of_sale"], "%Y-%m-%d").date()
                        )
                        self.sales.append(sale)

                    except (ValueError, KeyError) as e:
                        print(f"Bad sale data skipped: {row} → {e}")

        except FileNotFoundError:
            print("sales.csv not found. Sales start empty.")

    def save_sales(self, filename="sales.csv"):
        try:
            with open(filename, "w", newline="") as file:
                fieldnames = [
                    "sale_id",
                    "product_id",
                    "batch_number",
                    "quantity_sold",
                    "date_of_sale"
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for sale in self.sales:
                    writer.writerow({
                        "sale_id": sale.sale_id,
                        "product_id": sale.product_id,
                        "batch_number": sale.batch_number,
                        "quantity_sold": sale.quantity_sold,
                        "date_of_sale": sale.date_of_sale
                    })

        except Exception as e:
            print(f"Error saving sales: {e}")


# ----------------- DEMO -----------------
if __name__ == "__main__":
    shop = ShopSystem()

    shop.load_products()
    shop.load_sales()

    print("\nInventory Loaded:")
    shop.inventory.get_all_products()

    # Example sale
    print("\nMaking a sale...")
    if shop.inventory.product_sale("P001", "B001", 2):
        new_sale = Sale("S003", "P001", "B001", 2, date.today())
        shop.sales.append(new_sale)

    shop.save_products()
    shop.save_sales()

    print("\nData saved successfully.")

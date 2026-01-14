import csv
from datetime import datetime, date, timedelta

# ===================== Product =====================
class Product:
    def __init__(self, product_id, batch_number, name, price, quantity, expiry_date):
        self.product_id = product_id
        self.batch_number = batch_number
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.expiry_date = (
            datetime.strptime(expiry_date, "%Y-%m-%d").date()
            if isinstance(expiry_date, str)
            else expiry_date
        )

# ===================== Sale =====================
class Sale:
    def __init__(self, sale_id, product_id, batch_number, quantity_sold, price, date_of_sale):
        self.sale_id = sale_id
        self.product_id = product_id
        self.batch_number = batch_number
        self.quantity_sold = int(quantity_sold)
        self.price = float(price)
        self.total = self.quantity_sold * self.price
        self.date_of_sale = (
            datetime.strptime(date_of_sale, "%Y-%m-%d").date()
            if isinstance(date_of_sale, str)
            else date_of_sale
        )

# ===================== ShopSystem =====================
class ShopSystem:
    def __init__(self):
        self.products = []
        self.sales = []

    # ---------- Load & Save ----------
    def load_products(self, filename="products.csv"):
        try:
            with open(filename, newline="") as file:
                reader = csv.DictReader(file)
                self.products = []
                for row in reader:
                    try:
                        if not row["price"] or not row["quantity"]:
                                 continue
                        self.products.append(Product(
                            row["product_id"],
                            row["batch_number"],
                            row["name"],
                            row["price"],
                            row["quantity"],
                            row["expiry_date"],
                        ))
                    except Exception:
                        print(f"Skipping bad product row: {row}")
        except FileNotFoundError:
            print("products.csv not found. Starting empty.")

    def save_products(self, filename="products.csv"):
        with open(filename, "w", newline="") as file:
            fieldnames = ["product_id", "batch_number", "name", "price", "quantity", "expiry_date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for p in self.products:
                writer.writerow({
                    "product_id": p.product_id,
                    "batch_number": p.batch_number,
                    "name": p.name,
                    "price": p.price,
                    "quantity": p.quantity,
                    "expiry_date": p.expiry_date,
                })

    def load_sales(self, filename="sales.csv"):
        try:
            with open(filename, newline="") as file:
                reader = csv.DictReader(file)
                self.sales = [
                    Sale(
                        row["sale_id"],
                        row["product_id"],
                        row["batch_number"],
                        row["quantity_sold"],
                        row["price"],
                        row["date_of_sale"],
                    )
                    for row in reader
                ]
        except FileNotFoundError:
            print("sales.csv not found. Starting empty.")

    def save_sales(self, filename="sales.csv"):
        with open(filename, "w", newline="") as file:
            fieldnames = [
                "sale_id", "product_id", "batch_number",
                "quantity_sold", "price", "total", "date_of_sale"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in self.sales:
                writer.writerow(vars(s))

    # ---------- Core Features ----------
    def view_products(self):
        print("\nID | Batch | Name | Price | Qty | Expiry | Status")
        print("-" * 70)
        for p in self.products:
            status = "EXPIRED" if p.expiry_date < date.today() else (
                "EXPIRING SOON" if p.expiry_date <= date.today() + timedelta(days=7) else "OK"
            )
            print(f"{p.product_id} | {p.batch_number} | {p.name} | {p.price} | {p.quantity} | {p.expiry_date} | {status}")

    def add_product(self):
        # --- Product ID ---
        while True:
            pid = input("Product ID: ").strip()
            if pid:
                break
            print("Product ID cannot be empty.")

        # --- Batch Number ---
        while True:
            batch = input("Batch number: ").strip()
            if batch:
                break
            print("Batch number cannot be empty.")

        # --- Name ---
        while True:
            name = input("Name: ").strip()
            if name:
                break
            print("Product name cannot be empty.")

        # --- Price ---
        while True:
            try:
                price = float(input("Price: "))
                if price > 0:
                    break
                print("Price must be a positive number.")
            except ValueError:
                print("Invalid price. Enter a number.")

        # --- Quantity ---
        while True:
            try:
                qty = int(input("Quantity: "))
                if qty > 0:
                    break
                print("Quantity must be a positive integer.")
            except ValueError:
                print("Invalid quantity. Enter a whole number.")

        # --- Expiry Date ---
        while True:
            expiry = input("Expiry (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(expiry, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        # --- Merge if product & batch exist ---
        for p in self.products:
            if p.product_id == pid and p.batch_number == batch:
                p.quantity += qty
                self.save_products()
                print("Existing product batch updated (quantity merged).")
                return

        # --- Otherwise add new product ---
        self.products.append(Product(pid, batch, name, price, qty, expiry))
        self.save_products()
        print("New product added successfully.")

    def update_price(self):
        pid = input("Product ID: ")
        batch = input("Batch number: ")
        new_price = float(input("New price: "))

        if new_price <= 0:
            print("Price must be positive.")
            return

        for p in self.products:
            if p.product_id == pid and p.batch_number == batch:
                p.price = new_price
                self.save_products()
                print("Price updated.")
                return

        print("Product batch not found.")

    def make_sale(self):
        sale_id = input("Sale ID: ")
        pid = input("Product ID: ")
        batch = input("Batch number: ")
        qty = int(input("Quantity sold: "))

        if qty <= 0:
            print("Quantity must be positive.")
            return

        for p in self.products:
            if p.product_id == pid and p.batch_number == batch:
                if p.expiry_date < date.today():
                    print("Cannot sell expired product.")
                    return
                if p.quantity < qty:
                    print("Insufficient stock.")
                    return

                p.quantity -= qty
                sale = Sale(sale_id, pid, batch, qty, p.price, date.today())
                self.sales.append(sale)
                self.save_products()
                self.save_sales()
                print(f"Sale completed. Revenue: {sale.total}")
                return

        print("Product batch not found.")

    def view_sales(self):
        print("\nSaleID | Product | Batch | Qty | Price | Total | Date")
        print("-" * 70)
        total_revenue = 0
        for s in self.sales:
            total_revenue += s.total
            print(f"{s.sale_id} | {s.product_id} | {s.batch_number} | {s.quantity_sold} | {s.price} | {s.total} | {s.date_of_sale}")
        print(f"\nTOTAL REVENUE: {total_revenue}")

    def remove_expired_products(self):
        self.products = [p for p in self.products if p.expiry_date >= date.today()]
        self.save_products()
        print("Expired products removed.")

    # ---------- Menu ----------
    def run(self):
        self.load_products()
        self.load_sales()

        while True:
            print("\n--- ShopSystem Menu ---")
            print("1. View Products")
            print("2. Add Product")
            print("3. Update Product Price")
            print("4. Make Sale")
            print("5. View Sales")
            print("6. Remove Expired Products")
            print("7. Save & Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.view_products()
            elif choice == "2":
                self.add_product()
            elif choice == "3":
                self.update_price()
            elif choice == "4":
                self.make_sale()
            elif choice == "5":
                self.view_sales()
            elif choice == "6":
                self.remove_expired_products()
            elif choice == "7":
                self.save_products()
                self.save_sales()
                print("Data saved. Goodbye!")
                break
            else:
                print("Invalid choice.")

# ===================== Run =====================
if __name__ == "__main__":
    ShopSystem().run()

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
    def __init__(self, sale_id, product_code, quantity_sold, date_of_sale):
        self.sale_id = sale_id
        self.product_code = product_code
        self.quantity_sold = int(quantity_sold)
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
                self.products = [
                    Product(
                        row["product_id"],
                        row["batch_number"],
                        row["name"],
                        row["price"],
                        row["quantity"],
                        row["expiry_date"],
                    )
                    for row in reader
                ]
        except FileNotFoundError:
            print("products.csv not found. Starting empty.")

    def save_products(self, filename="products.csv"):
        with open(filename, "w", newline="") as file:
            fieldnames = [
                "product_id",
                "batch_number",
                "name",
                "price",
                "quantity",
                "expiry_date",
            ]
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
                        row["product_code"],
                        row["quantity_sold"],
                        row["date_of_sale"],
                    )
                    for row in reader
                ]
        except FileNotFoundError:
            print("sales.csv not found. Starting empty.")

    def save_sales(self, filename="sales.csv"):
        with open(filename, "w", newline="") as file:
            fieldnames = ["sale_id", "product_code", "quantity_sold", "date_of_sale"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in self.sales:
                writer.writerow({
                    "sale_id": s.sale_id,
                    "product_code": s.product_code,
                    "quantity_sold": s.quantity_sold,
                    "date_of_sale": s.date_of_sale,
                })

    # ---------- Core Features ----------
    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nID | Batch | Name | Price | Qty | Expiry | Status")
        print("-" * 60)

        for p in self.products:
            if p.expiry_date < date.today():
                status = "EXPIRED"
            elif p.expiry_date <= date.today() + timedelta(days=7):
                status = "EXPIRING SOON"
            else:
                status = "OK"

            print(
                f"{p.product_id} | {p.batch_number} | {p.name} | "
                f"{p.price} | {p.quantity} | {p.expiry_date} | {status}"
            )

    def add_product(self):
        pid = input("Product ID: ")
        batch = input("Batch number: ")
        name = input("Name: ")
        while True:
            try:
                price = float(input("Enter Price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 10.50).")

        while True:
            try:
                qty = int(input("Quantity: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 10).")

        expiry = input("Expiry (YYYY-MM-DD): ")

        try:
            self.products.append(Product(pid, batch, name, price, qty, expiry))
            self.save_products()
            print("Product added and saved successfully.")
        except Exception as e:
            print("Error adding product:", e)

    def update_price(self):
        pid = input("Enter product ID: ")
        batch = input("Enter batch number: ")

        for p in self.products:
            if p.product_id == pid and p.batch_number == batch:
                new_price = float(input("Enter new price: "))
                if new_price <= 0:
                    print("Price must be positive.")
                    return
                p.price = new_price
                self.save_products()
                print("Price updated and saved.")
                return

        print("Product not found for that batch.")

    def make_sale(self):
        sale_id = input("Sale ID: ")
        pid = input("Product ID: ")
        batch = input("Batch number: ")
        qty = int(input("Quantity sold: "))

        for p in self.products:
            if p.product_id == pid and p.batch_number == batch:
                if p.expiry_date < date.today():
                    print("Cannot sell expired product.")
                    return
                if p.quantity < qty:
                    print("Insufficient stock.")
                    return

                p.quantity -= qty
                self.sales.append(Sale(sale_id, f"{pid}-{batch}", qty, date.today()))
                self.save_products()
                self.save_sales()
                print("Sale completed and saved.")
                return

        print("Product not found for that batch.")

    def view_sales(self):
        if not self.sales:
            print("No sales recorded.")
            return
        print("\nSaleID | Product | Qty | Date")
        print("-" * 40)
        for s in self.sales:
            print(f"{s.sale_id} | {s.product_code} | {s.quantity_sold} | {s.date_of_sale}")

    def remove_expired_product(self):
        pid = input("Product ID: ")
        batch = input("Batch number: ")

        for p in self.products:
            if p.product_id == pid and p.batch_number == batch:
                if p.expiry_date >= date.today():
                    print("Cannot remove product: not expired.")
                    return
                self.products.remove(p)
                self.save_products()
                print("Expired product removed and saved.")
                return

        print("Product not found.")

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
            print("6. Remove Expired Product")
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
                self.remove_expired_product()
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

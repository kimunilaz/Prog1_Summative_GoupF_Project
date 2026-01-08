import csv
from datetime import datetime, date

# ----------------- Product & Sale Classes -----------------
class Product:
    def __init__(self, product_id, name, price, quantity, expiry_date):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date() if isinstance(expiry_date, str) else expiry_date

class Sale:
    def __init__(self, sale_id, product_code, quantity_sold, date_of_sale):
        self.sale_id = sale_id
        self.product_code = product_code
        self.quantity_sold = int(quantity_sold)
        self.date_of_sale = datetime.strptime(date_of_sale, "%Y-%m-%d").date() if isinstance(date_of_sale, str) else date_of_sale

# ----------------- ShopSystem -----------------
class ShopSystem:
    def __init__(self):
        self.products = []
        self.sales = []

    # ----------------- Products -----------------
    def load_products(self, filename="products.csv"):
        try:
            with open(filename, newline="") as file:
                reader = csv.DictReader(file)
                self.products = []
                for row in reader:
                    try:
                        p = Product(
                            row["product_id"],
                            row["name"],
                            row["price"],
                            row["quantity"],
                            row["expiry_date"]
                        )
                        self.products.append(p)
                    except (ValueError, KeyError) as e:
                        print(f"Bad product data skipped: {row} → {e}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty product list.")

    def save_products(self, filename="products.csv"):
        try:
            with open(filename, "w", newline="") as file:
                fieldnames = ["product_id", "name", "price", "quantity", "expiry_date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for p in self.products:
                    writer.writerow({
                        "product_id": p.product_id,
                        "name": p.name,
                        "price": p.price,
                        "quantity": p.quantity,
                        "expiry_date": p.expiry_date
                    })
        except Exception as e:
            print(f"Error saving products: {e}")

    # ----------------- Sales -----------------
    def load_sales(self, filename="sales.csv"):
        try:
            with open(filename, newline="") as file:
                reader = csv.DictReader(file)
                self.sales = []
                for row in reader:
                    try:
                        s = Sale(
                            row["sale_id"],
                            row["product_code"],
                            row["quantity_sold"],
                            row["date_of_sale"]
                        )
                        self.sales.append(s)
                    except (ValueError, KeyError) as e:
                        print(f"Bad sale data skipped: {row} → {e}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty sales list.")

    def save_sales(self, filename="sales.csv"):
        try:
            with open(filename, "w", newline="") as file:
                fieldnames = ["sale_id", "product_code", "quantity_sold", "date_of_sale"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for s in self.sales:
                    writer.writerow({
                        "sale_id": s.sale_id,
                        "product_code": s.product_code,
                        "quantity_sold": s.quantity_sold,
                        "date_of_sale": s.date_of_sale
                    })
        except Exception as e:
            print(f"Error saving sales: {e}")

    # ----------------- Utility Methods -----------------
    def view_products(self):
        if not self.products:
            print("\nNo products in inventory yet.")
            return
        print("\nProducts in Inventory:")
        print(f"{'ID':<6}|{'Name':<15}|{'Price':<8}|{'Qty':<5}|{'Expiry':<12}")
        print("-"*50)
        for p in self.products:
            print(f"{p.product_id:<6}|{p.name:<15}|{p.price:<8}|{p.quantity:<5}|{p.expiry_date}")

    def add_product(self):
        pid = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = input("Enter price: ")
        quantity = input("Enter quantity: ")
        expiry = input("Enter expiry date (YYYY-MM-DD): ")
        try:
            new_p = Product(pid, name, price, quantity, expiry)
            self.products.append(new_p)
            print(f"Product {name} added successfully!")
        except Exception as e:
            print(f"Failed to add product: {e}")

    def make_sale(self):
        if not self.products:
            print("No products to sell. Inventory empty.")
            return
        sale_id = input("Enter sale ID: ")
        product_code = input("Enter product ID to sell: ")
        qty = int(input("Enter quantity: "))

        product = next((p for p in self.products if p.product_id == product_code), None)
        if not product:
            print("Product not found in inventory.")
            return
        if product.expiry_date < date.today():
            print("Cannot sell expired product!")
            return
        if product.quantity < qty:
            print(f"Not enough stock! Available: {product.quantity}")
            return

        product.quantity -= qty
        new_sale = Sale(sale_id, product_code, qty, date.today())
        self.sales.append(new_sale)
        print(f"Sale successful: {qty} units of {product.name} sold!")

    def view_sales(self):
        if not self.sales:
            print("No sales yet.")
            return
        print("\nSales History:")
        print(f"{'Sale ID':<8}|{'Product':<8}|{'Qty':<5}|{'Date':<12}")
        print("-"*40)
        for s in self.sales:
            print(f"{s.sale_id:<8}|{s.product_code:<8}|{s.quantity_sold:<5}|{s.date_of_sale}")

# ----------------- Main Menu -----------------
def main():
    shop = ShopSystem()
    shop.load_products()
    shop.load_sales()

    while True:
        print("\n--- ShopSystem Menu ---")
        print("1. View Products")
        print("2. Add Product")
        print("3. Make Sale")
        print("4. View Sales History")
        print("5. Save & Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            shop.view_products()
        elif choice == "2":
            shop.add_product()
        elif choice == "3":
            shop.make_sale()
        elif choice == "4":
            shop.view_sales()
        elif choice == "5":
            shop.save_products()
            shop.save_sales()
            print("Data saved. Exiting ShopSystem.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

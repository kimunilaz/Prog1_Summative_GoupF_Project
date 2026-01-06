# populate_products_extended.py
import csv

products = [
    {"product_code": "P001", "name": "Sugar", "price": 2500, "quantity": 10, "expiry_date": "2026-12-31"},
    {"product_code": "P002", "name": "Milk", "price": 1500, "quantity": 20, "expiry_date": "2026-01-15"},
    {"product_code": "P003", "name": "Bread", "price": 1200, "quantity": 15, "expiry_date": "2026-01-10"},
    {"product_code": "P004", "name": "Butter", "price": 3500, "quantity": 5, "expiry_date": "2026-03-05"},
    {"product_code": "P005", "name": "Eggs", "price": 800, "quantity": 30, "expiry_date": "2026-01-12"}
]

filename = "products.csv"

with open(filename, "w", newline="") as file:
    fieldnames = ["product_code", "name", "price", "quantity", "expiry_date"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for p in products:
        writer.writerow(p)

print(f"{filename} has been populated with products data!")

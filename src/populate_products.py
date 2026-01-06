# populate_products.py
import csv

# Sample products data
products = [
    {"product_code": "P001", "name": "Sugar", "price": 2500, "quantity": 10, "expiry_date": "2026-12-31"},
    {"product_code": "P002", "name": "Milk", "price": 1500, "quantity": 20, "expiry_date": "2026-01-15"}
]

# Path to your existing products.csv
filename = "products.csv"

# Write sample data to products.csv
with open(filename, "w", newline="") as file:
    fieldnames = ["product_code", "name", "price", "quantity", "expiry_date"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for p in products:
        writer.writerow(p)

print(f"{filename} has been populated with sample products!")

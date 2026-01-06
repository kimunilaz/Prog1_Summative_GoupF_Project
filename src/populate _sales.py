# populate_sales.py
import csv
from datetime import date

# Sample sales data
sales = [
    {"sale_id": "S001", "product_code": "P001", "quantity_sold": 2, "date_of_sale": "2026-01-05"},
    {"sale_id": "S002", "product_code": "P002", "quantity_sold": 1, "date_of_sale": "2026-01-06"}
]

# Path to your existing sales.csv
filename = "sales.csv"

# Write sample data to sales.csv
with open(filename, "w", newline="") as file:
    fieldnames = ["sale_id", "product_code", "quantity_sold", "date_of_sale"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for s in sales:
        writer.writerow(s)

print(f"{filename} has been populated with sample sales!")

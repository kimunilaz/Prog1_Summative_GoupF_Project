# populate_sales_extended.py
import csv

sales = [
    {"sale_id": "S001", "product_code": "P001", "quantity_sold": 2, "date_of_sale": "2026-01-05"},
    {"sale_id": "S002", "product_code": "P002", "quantity_sold": 1, "date_of_sale": "2026-01-06"},
    {"sale_id": "S003", "product_code": "P003", "quantity_sold": 5, "date_of_sale": "2026-01-07"},
    {"sale_id": "S004", "product_code": "P001", "quantity_sold": 1, "date_of_sale": "2026-01-08"},
    {"sale_id": "S005", "product_code": "P004", "quantity_sold": 2, "date_of_sale": "2026-01-09"},
    {"sale_id": "S006", "product_code": "P005", "quantity_sold": 12, "date_of_sale": "2026-01-10"},
    {"sale_id": "S007", "product_code": "P002", "quantity_sold": 3, "date_of_sale": "2026-01-11"},
    {"sale_id": "S008", "product_code": "P003", "quantity_sold": 2, "date_of_sale": "2026-01-12"}
]

filename = "sales.csv"

with open(filename, "w", newline="") as file:
    fieldnames = ["sale_id", "product_code", "quantity_sold", "date_of_sale"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for s in sales:
        writer.writerow(s)

print(f"{filename} has been populated with sales data!")

import csv

sales = [
    {"sale_id": "S001", "product_id": "P001", "batch_number": "B001", "quantity_sold": 2, "price": 2500, "date_of_sale": "2026-01-05"},
    {"sale_id": "S002", "product_id": "P002", "batch_number": "B001", "quantity_sold": 1, "price": 1500, "date_of_sale": "2026-01-06"},
    {"sale_id": "S003", "product_id": "P003", "batch_number": "B001", "quantity_sold": 5, "price": 1200, "date_of_sale": "2026-01-07"},
]

with open("sales.csv", "w", newline="") as file:
    fieldnames = ["sale_id", "product_id", "batch_number", "quantity_sold", "price", "date_of_sale"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sales)

print("sales.csv populated correctly!")

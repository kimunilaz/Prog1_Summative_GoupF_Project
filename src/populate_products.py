
import csv
from datetime import date

products = [
    {
        "product_id": "P001",
        "batch_number": "B001",
        "name": "Sugar",
        "price": 2500,
        "quantity": 10,
        "expiry_date": date(2026, 12, 31)
    },
    {
        "product_id": "P002",
        "batch_number": "B001",
        "name": "Milk",
        "price": 1500,
        "quantity": 20,
        "expiry_date": date(2026, 1, 15)
    },
    {
        "product_id": "P003",
        "batch_number": "B001",
        "name": "Bread",
        "price": 1200,
        "quantity": 15,
        "expiry_date": date(2026, 1, 10)
    },
    {
        "product_id": "P004",
        "batch_number": "B001",
        "name": "Butter",
        "price": 3500,
        "quantity": 5,
        "expiry_date": date(2026, 3, 5)
    },
    {
        "product_id": "P005",
        "batch_number": "B001",
        "name": "Eggs",
        "price": 800,
        "quantity": 30,
        "expiry_date": date(2026, 1, 12)
    }
]

with open("products.csv", "w", newline="") as file:
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

    for product in products:
        writer.writerow(product)

print("products.csv populated successfully!")

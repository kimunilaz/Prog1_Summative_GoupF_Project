# Unit tests for Sale class in sale.py
# These tests check that Sale objects correctly calculate totals,
# handle invalid inputs, and produce proper records.

import unittest
from datetime import date
from sale import Sale

class TestSale(unittest.TestCase):

    # 1. Record a normal sale
    def test_normal_sale(self):
        """
        Test that a normal sale with valid product ID, batch, quantity, and price
        calculates the correct total and sets today's date.
        """
        sale = Sale("J001", "B001", 5, 70.0)  # 5 units at ₹70 each
        self.assertEqual(sale.product_id, "J001")
        self.assertEqual(sale.batch_number, "B001")
        self.assertEqual(sale.quantity_sold, 5)
        self.assertEqual(sale.price_per_unit, 70.0)
        self.assertEqual(sale.total_price, 350.0)  # 5 * 70
        self.assertEqual(sale.sale_date, date.today())

    # 2. Calculate total for quantity
    def test_calculate_total(self):
        """
        Test that calculate_total() correctly multiplies quantity by price per unit.
        """
        sale = Sale("J002", "B002", 3, 40.0)  # 3 units at ₹40 each
        self.assertEqual(sale.calculate_total(), 120.0)

    # 3. Sale with 0 quantity
    def test_zero_quantity_sale(self):
        """
        Test that a sale with zero quantity results in a total price of 0.
        """
        sale = Sale("J003", "B003", 0, 25.0)
        self.assertEqual(sale.total_price, 0.0)

    # 4. Sale exceeding available stock (simulation only)
    def test_exceeding_stock_sale(self):
        """
        Test that a very large sale still calculates mathematically,
        though in a real system this should be blocked by Inventory/ShopSystem.
        """
        sale = Sale("J004", "B004", 1000, 5.0)  # unrealistic quantity
        self.assertEqual(sale.total_price, 5000.0)

    # 5. Invalid product ID (simulate rejection)
    def test_invalid_product_id(self):
        """
        Test that a sale with an empty product ID still stores the value,
        though in a real system this should be rejected.
        """
        sale = Sale("", "B005", 2, 30.0)
        self.assertEqual(sale.product_id, "")

    # 6. to_record method returns dictionary
    def test_to_record(self):
        """
        Test that to_record() returns a dictionary with correct sale details.
        """
        sale = Sale("J006", "B006", 4, 140.0)  # 4 units at ₹140 each
        record = sale.to_record()
        self.assertEqual(record["product_id"], "J006")
        self.assertEqual(record["batch_number"], "B006")
        self.assertEqual(record["quantity_sold"], 4)
        self.assertEqual(record["total_price"], 560.0)  # 4 * 140
        self.assertEqual(record["sale_date"], date.today())

if __name__ == "__main__":
    unittest.main()

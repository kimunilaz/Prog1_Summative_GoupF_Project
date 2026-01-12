# Unit tests for Sale class in sale.py
import unittest
from datetime import date
from sale import Sale

class TestSale(unittest.TestCase):
# 1. Record a normal sale
  def test_normal_sale(self):
      sale = Sale("P001", "B001", 5, 10.0)
      self.assertEqual(sale.product_id, "P001")
      self.assertEqual(sale.batch_number, "B001")
      self.assertEqual(sale.quantity_sold, 5)
      self.assertEqual(sale.price_per_unit, 10.0)
      self.assertEqual(sale.total_price, 50.0)  # 5 * 10
      self.assertEqual(sale.sale_date, date.today())

# 2. Calculate total for quantity
  def test_calculate_total(self):
    sale = Sale("P002", "B002", 3, 20.0)
    self.assertEqual(sale.calculate_total(), 60.0)

# 3. Sale with 0 quantity
  def test_zero_quantity_sale(self):
    sale = Sale("P003", "B003", 0, 15.0)
    self.assertEqual(sale.total_price, 0.0)

# 4. Sale exceeding available stock (simulate error handling)
  def test_exceeding_stock_sale(self):
   # In real system, you'd check against inventory. Here we just simulate.
    sale = Sale("P004", "B004", 1000, 2.0)
    self.assertEqual(sale.total_price, 2000.0)  # still calculates, but logic should prevent in ShopSystem

# 5. Invalid product ID (simulate rejection)
  def test_invalid_product_id(self):
    sale = Sale("", "B005", 2, 10.0)  # empty product_id
    self.assertEqual(sale.product_id, "")  # still stores, but ShopSystem should reject

# 6. to_record method returns dictionary
  def test_to_record(self):
    sale = Sale("P006", "B006", 4, 12.5)
    record = sale.to_record()
    self.assertEqual(record["product_id"], "P006")
    self.assertEqual(record["batch_number"], "B006")
    self.assertEqual(record["quantity_sold"], 4)
    self.assertEqual(record["total_price"], 50.0)
    self.assertEqual(record["sale_date"], date.today())

if __name__ == "__main__":
    unittest.main()

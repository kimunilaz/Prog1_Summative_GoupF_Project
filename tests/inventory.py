# Unit tests for Inventory class in inventory.py
import unittest
from datetime import date, timedelta
from inventory import Inventory, Product

class TestInventory(unittest.TestCase):
    def setUp(self):
        # Create a fresh inventory before each test
        self.inventory = Inventory(low_stock_threshold=10)
        self.product = Product("P001", "B001", "Milk", 20.0, 10, date.today() + timedelta(days=5))
        self.inventory.add_product(self.product)

    # 1. Add a new product
    def test_add_product(self):
        new_product = Product("P002", "B002", "Sugar", 15.0, 5, date.today() + timedelta(days=10))
        result = self.inventory.add_product(new_product)
        self.assertTrue(result)
        self.assertIn(("P002", "B002"), self.inventory.products)

    # 2. Find existing product
    def test_find_product(self):
        found = self.inventory.find_product("P001", "B001")
        self.assertEqual(found, self.product)

    # 3. Remove product
    def test_remove_product(self):
        result = self.inventory.remove_product("P001", "B001")
        self.assertTrue(result)
        self.assertIsNone(self.inventory.find_product("P001", "B001"))

    # 4.1. Update stock - Increase
    def test_update_stock_increase(self):
        result = self.inventory.update_stock("P001", "B001", "increase", 5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 15)

    # 4.2. Update stock - Decrease
    def test_update_stock_decrease(self):
        result = self.inventory.update_stock("P001", "B001", "decrease", 5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 5)

    # 4.3. Update stock - Set new quantity
    def test_update_stock_set_new_quantity(self):
        result = self.inventory.update_stock("P001", "B001", "set new quantity", 20)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 20)

    # 7. Get low-stock products
    def test_get_low_stock_products(self):
        self.product.quantity = 2
        low_stock = self.inventory.get_low_stock_products()
        self.assertIn(("P001", "B001"), low_stock)

    # 8. Get expired products
    def test_get_expired_products(self):
        expired_product = Product("P003", "B003", "Bread", 10.0, 5, date.today() - timedelta(days=1))
        self.inventory.add_product(expired_product)
        expired_list = self.inventory.get_expired_products()
        self.assertIn(("P003", "B003"), expired_list)

    # 9. Find non-existent product
    def test_find_nonexistent_product(self):
        result = self.inventory.find_product("X999", "B999")
        self.assertIsNone(result)

    # 10. Update stock with invalid quantity
    def test_invalid_stock_update(self):
        result = self.inventory.update_stock("P001", "B001", "decrease", 100)  # too much
        self.assertFalse(result)
        self.assertGreaterEqual(self.product.quantity, 0)

    # 11.1. Product sale - normal
    def test_product_sale_normal(self):
        result = self.inventory.product_sale("P001", "B001", 5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 5)

    # 11.2. Product sale - expired product
    def test_product_sale_expired(self):
        expired_product = Product("P004", "B004", "Juice", 10.0, 5, date.today() - timedelta(days=1))
        self.inventory.add_product(expired_product)
        result = self.inventory.product_sale("P004", "B004", 1)
        self.assertFalse(result)

    # 11.3. Product sale - invalid quantity
    def test_product_sale_invalid_quantity(self):
        result = self.inventory.product_sale("P001", "B001", -5)
        self.assertFalse(result)

    # 11.4. Product sale - more than available stock
    def test_product_sale_exceeding_stock(self):
        result = self.inventory.product_sale("P001", "B001", 50)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

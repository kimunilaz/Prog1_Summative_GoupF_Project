# Unit tests for Inventory class in inventory.py
# These tests check that Inventory methods (add, find, remove, update stock, sales, etc.)
# behave correctly under normal, edge, and invalid conditions.

import unittest
from datetime import date, timedelta
from src.inventory import Inventory, Product

class TestInventory(unittest.TestCase):
    def setUp(self):
        """
        Runs before each test.
        Creates a fresh Inventory object and adds one sample product (Milk).
        This ensures every test starts with a clean, predictable state.
        """
        self.inventory = Inventory(low_stock_threshold=10)
        self.product = Product("J001", "B001", "Milk", 70.0, 10, date.today() + timedelta(days=5))
        self.inventory.add_product(self.product)

    # 1. Add a new product
    def test_add_product(self):
        """
        Test that a new product can be added successfully.
        """
        new_product = Product("J002", "B002", "Sugar", 40.0, 5, date.today() + timedelta(days=10))
        result = self.inventory.add_product(new_product)
        self.assertTrue(result)  # Should return True
        self.assertIn(("J002", "B002"), self.inventory.products)  # Product should be stored

    # 2. Find existing product
    def test_find_product(self):
        """
        Test that an existing product can be found using product_id and batch_number.
        """
        found = self.inventory.find_product("J001", "B001")
        self.assertEqual(found, self.product)

    # 3. Remove product
    def test_remove_product(self):
        """
        Test that a product can be removed successfully.
        """
        result = self.inventory.remove_product("J001", "B001")
        self.assertTrue(result)
        self.assertIsNone(self.inventory.find_product("J001", "B001"))  # Should no longer exist

    # 4. Update stock - Increase
    def test_update_stock_increase(self):
        """
        Test increasing stock quantity by 5 units.
        """
        result = self.inventory.update_stock("J001", "B001", "increase", 5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 15)

    # 5. Update stock - Decrease
    def test_update_stock_decrease(self):
        """
        Test decreasing stock quantity by 5 units.
        """
        result = self.inventory.update_stock("J001", "B001", "decrease", 5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 5)

    # 6. Update stock - Set new quantity
    def test_update_stock_set_new_quantity(self):
        """
        Test setting stock quantity directly to 20 units.
        """
        result = self.inventory.update_stock("J001", "B001", "set new quantity", 20)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 20)

    # 7. Get low-stock products
    def test_get_low_stock_products(self):
        """
        Test that products with quantity <= threshold are flagged as low stock.
        """
        self.product.quantity = 2
        low_stock = self.inventory.get_low_stock_products()
        self.assertIn(("J001", "B001"), low_stock)

    # 8. Get expired products
    def test_get_expired_products(self):
        """
        Test that expired products are flagged correctly.
        """
        expired_product = Product("J003", "B003", "Bread", 25.0, 5, date.today() - timedelta(days=1))
        self.inventory.add_product(expired_product)
        expired_list = self.inventory.get_expired_products()
        self.assertIn(("J003", "B003"), expired_list)

    # 9. Find non-existent product
    def test_find_nonexistent_product(self):
        """
        Test that searching for a product that does not exist returns None.
        """
        result = self.inventory.find_product("X999", "B999")
        self.assertIsNone(result)

    # 10. Update stock with invalid quantity
    def test_invalid_stock_update(self):
        """
        Test that decreasing stock by more than available fails.
        """
        result = self.inventory.update_stock("J001", "B001", "decrease", 100)
        self.assertFalse(result)
        self.assertGreaterEqual(self.product.quantity, 0)

    # 11. Product sale - normal
    def test_product_sale_normal(self):
        """
        Test that a valid sale reduces stock correctly.
        """
        result = self.inventory.product_sale("J001", "B001", 5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 5)

    # 12. Product sale - expired product
    def test_product_sale_expired(self):
        """
        Test that selling an expired product is blocked.
        """
        expired_product = Product("J004", "B004", "Juice", 30.0, 5, date.today() - timedelta(days=1))
        self.inventory.add_product(expired_product)
        result = self.inventory.product_sale("J004", "B004", 1)
        self.assertFalse(result)

    # 13. Product sale - invalid quantity
    def test_product_sale_invalid_quantity(self):
        """
        Test that selling with a negative quantity is blocked.
        """
        result = self.inventory.product_sale("J001", "B001", -5)
        self.assertFalse(result)

    # 14. Product sale - more than available stock
    def test_product_sale_exceeding_stock(self):
        """
        Test that selling more than available stock is blocked.
        """
        result = self.inventory.product_sale("J001", "B001", 50)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

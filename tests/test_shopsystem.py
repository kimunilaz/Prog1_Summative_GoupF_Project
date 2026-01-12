# Unit tests for ShopSystem class in shopsystem.py
# These tests check that the ShopSystem integrates Product, Inventory, and Sale correctly.
# It ensures data loading/saving, sales processing, and menu handling work as expected.

import unittest
from datetime import date, timedelta
from product import Product
from inventory import Inventory
from sale import Sale
from shopsystem import ShopSystem

class TestShopSystem(unittest.TestCase):

    def setUp(self):
        """
        Runs before each test.
        Creates a fresh ShopSystem with one product (Milk).
        """
        self.system = ShopSystem()
        self.product = Product("J001", "B001", "Milk", 70.0, 10, date.today() + timedelta(days=5))
        self.system.inventory.add_product(self.product)

    # 1. Load data from files (simulation)
    def test_load_data(self):
        """
        Test that load_data() runs and populates inventory.
        """
        self.system.load_data()  # assumes method exists
        self.assertIsInstance(self.system.inventory.products, dict)

    # 2. Save data to files (simulation)
    def test_save_data(self):
        """
        Test that save_data() runs without errors.
        """
        self.system.save_data()  # assumes method exists
        # Could check file existence or mock file writing in a real test

    # 3. Process a normal sale
    def test_process_sale(self):
        """
        Test that processing a valid sale reduces stock correctly.
        """
        result = self.system.process_sale("J001", "B001", 2)  # sell 2 units
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 8)

    # 4. Process sale for low-stock product
    def test_low_stock_alert(self):
        """
        Test that selling the last unit reduces stock to zero.
        """
        self.product.quantity = 1
        result = self.system.process_sale("J001", "B001", 1)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity, 0)

    # 5. Process sale for expired product
    def test_expired_product_sale(self):
        """
        Test that sales of expired products are blocked.
        """
        expired_product = Product("J002", "B002", "Bread", 25.0, 5, date.today() - timedelta(days=1))
        self.system.inventory.add_product(expired_product)
        result = self.system.process_sale("J002", "B002", 1)
        self.assertFalse(result)

    # 6. Invalid menu selection
    def test_invalid_menu_selection(self):
        """
        Test that invalid menu options are handled gracefully.
        """
        result = self.system.handle_menu("invalid_option")  # assumes method exists
        self.assertEqual(result, "Invalid selection")

    # 7. Add new product with missing fields
    def test_add_product_missing_fields(self):
        """
        Test that adding a product with missing details fails.
        """
        result = self.system.add_product("", "B003", "", 0, 0, None)  # invalid product
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

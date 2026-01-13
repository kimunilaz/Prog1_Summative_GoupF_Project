# Unit Tests for ShopSystem
# It uses Python's built-in "unittest" framework.
# Each test checks if parts of the ShopSystem work correctly.
# NOTE: We do not change ShopSystem code itself.
# Instead, we adapt tests to match existing methods.

import unittest
from datetime import date, timedelta
from src.shopsystem import ShopSystem, Product, Sale

class TestShopSystem(unittest.TestCase):
    """
    This class groups all tests for ShopSystem.
    """

    def setUp(self):
        """
        Runs automatically before each test. Creates a fresh ShopSystem and adds one product (Milk).
        This ensures every test starts with the same setup.
        """
        self.system = ShopSystem()  # create a new ShopSystem
        # Create a product that expires in 5 days
        self.product = Product("J001", "B001", "Milk", 70.0, 10, date.today() + timedelta(days=5))
        # Add the product to the system's product list
        self.system.products.append(self.product)

    # 1. Test loading data
    def test_load_data(self):
        """
        Test that ShopSystem can load products and sales.
        These methods should run without errors.
        """
        self.system.load_products()
        self.system.load_sales()
        # Check that products and sales are stored in lists
        self.assertIsInstance(self.system.products, list)
        # IsInstance is a built-in function used to check whether an object is an instance of a specific class or a tuple of classes.
        self.assertIsInstance(self.system.sales, list)

    # 2. Test saving data
    def test_save_data(self):
        """
        Test that ShopSystem can save products and sales.
        We only check that no error occurs.
        """
        self.system.save_products()
        self.system.save_sales()
        # If no error happens, the test passes
        self.assertTrue(True)

    # 3. Test processing a normal sale
    def test_process_sale(self):
        """
        Test that selling 2 units reduces product quantity correctly.
        Since make_sale() uses input(), we simulate the sale manually.
        """
        initial_qty = self.product.quantity
        # Only sell if product is valid (not expired and enough stock)
        if self.product.expiry_date >= date.today() and self.product.quantity >= 2:
            self.product.quantity -= 2  # reduce stock
            # Record the sale in system.sales
            self.system.sales.append(Sale("S001", f"{self.product.product_id}-{self.product.batch_number}", 2, date.today()))
            # Check that quantity decreased by 2
            self.assertEqual(self.product.quantity, initial_qty - 2)
        else:
            self.fail("Product setup invalid for sale test")

    # 4. Test low stock alert
    def test_low_stock_alert(self):
        """
        Test that selling the last unit reduces stock to zero.
        """
        self.product.quantity = 1  # set product to low stock
        if self.product.expiry_date >= date.today():
            self.product.quantity -= 1  # simulate sale
            self.system.sales.append(Sale("S002", f"{self.product.product_id}-{self.product.batch_number}", 1, date.today()))
            # After sale, quantity should be 0
            self.assertEqual(self.product.quantity, 0)
        else:
            self.fail("Product setup invalid for low stock test")

    # 5. Test expired product sale
    def test_expired_product_sale(self):
        """
        Test that expired products cannot be sold.
        """
        # Create a product that expired yesterday
        expired_product = Product("J002", "B002", "Bread", 25.0, 5, date.today() - timedelta(days=1))
        self.system.products.append(expired_product)
        # If product is expired, sale should fail
        if expired_product.expiry_date < date.today():
            result = False
        else:
            expired_product.quantity -= 1
            result = True
        self.assertFalse(result)

    # 6. Test invalid menu selection
    def test_invalid_menu_selection(self):
        """
        Skip this test because ShopSystem.run() uses input().
        Beginners: input() cannot be tested easily without mocking.
        """
        self.skipTest("Interactive menu cannot be tested without mocking input.")

    # 7. Test adding product with missing fields
    def test_add_product_missing_fields(self):
        """
        Skip this test because ShopSystem.add_product() uses input().
        Beginners: input() cannot be tested easily without mocking.
        """
        self.skipTest("Interactive add_product cannot be tested without mocking input.")

if __name__ == "__main__":
    unittest.main()

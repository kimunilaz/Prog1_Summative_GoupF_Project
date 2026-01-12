# Implementation of Product Test cases of the ShopSystsem
import unittest # Python's built-in testing framework
from datetime import date, timedelta # timedelta is used for time difference days=2 mean a time difference of 2 days
from product import Product
class Test_Product(unittest.TestCase): # Created a test suite (a collection of test cases, test suites, or both) that groups all the product-related tests.
 # 1. Check normal product creation
    def test_product_creation(self):
        product = Product("J0014", "Milk", 10, 70.0, date.today() + timedelta(days=5))
        self.assertEqual(product.name, "Milk")
        self.assertEqual(product.quantity, 10)
        self.assertEqual(product.price, 20.0)

    # 2. Update product quantity 
    def test_update_quantity(self):
        product = Product("J0022", "Plastic Bag", 5, 4.0, date.today() + timedelta(days=10))
        product.update_quantity(10)  
        self.assertEqual(product.quantity, 15)

    # 3. Update product price
    def test_update_price(self):
        product = Product("J003", "Pomegranate", 5, 100.0, date.today() + timedelta(days=10))
        product.update_price(12.0)  
        self.assertEqual(product.price, 12.0)

    # 4. Check expired product
    def test_expired_product(self):
        expired_date = date.today() - timedelta(days=2)
        product = Product("J0048", "Bread", 10, 25.0, expired_date)
        self.assertTrue(product.is_expired())

    # 5. Check product expiring soon
    def test_expiring_soon(self):
        soon_date = date.today() + timedelta(days=3)
        product = Product("J005", "Juice", 10, 30.0, soon_date)
        self.assertTrue(product.is_expiring_soon(5))

    # 6. Update quantity with negative number exceeding stock
    def test_invalid_quantity_update(self):
        product = Product(J0016", "Eggs", 50, 5.0, date.today() + timedelta(days=10))
        product.update_quantity(-100)  #  Error handling
        self.assertGreaterEqual(product.quantity, 0)

    # 7. Update price with negative value
    def test_invalid_price_update(self):
        product = Product("J027", "Butter", 10, 140.0, date.today() + timedelta(days=10))
        product.update_price(-10)  # Error handling
        self.assertGreaterEqual(product.price, 0)

if __name__ == "__main__":
    unittest.main()


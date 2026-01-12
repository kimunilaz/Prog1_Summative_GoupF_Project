# Implementation of Product Test cases of the ShopSystsem
import unittest # Python's built-in testing framework
from datetime import date, timedelta # timedelta is used for time difference days=2 mean a time difference of 2 days
from product import Product
class Test_Product(unittest.TestCase): # Created a test suite (a collection of test cases, test suites, or both) that groups all the product-related tests.
def test_expired_product(self):
  expired_date = date.today() - timedelta(days=2)
  product = Product("JOO23", "Bread", 10, 25.0, expired_date)
  self.assertTrue(product.is_expired()) # >>>>> The actual test


if __name__ == "__main__":
  unittest.main()

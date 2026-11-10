# test_discount.py

import unittest
from discount import calculate_discount

class TestDiscount(unittest.TestCase):
    
    def test_no_discount(self):
        # discount_rate = 0 -> expect original price
        self.assertEqual(calculate_discount(100, 0), 100)
    
    def test_10_percent_discount(self):
        # 10% discount on 100 => 90
        result = calculate_discount(100, 0.1)
        self.assertEqual(result, 90.0)

    def test_50_percent_discount(self):
        # 50% discount on 80 => 40
        result = calculate_discount(80, 0.5)
        self.assertAlmostEqual(result, 40.0, places=2)

if __name__ == "__main__":
    unittest.main()

import unittest
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_cutting import *

class TestCutPattern(unittest.TestCase):

    def setUp(self):
        self.demands = [Demand(22,10), Demand(19,10), Demand(16,10)]
        self.stock = Stock(630,1)
        self.quantities = [10,10,10]
        self.pattern = CutPattern(self.stock, self.demands, self.quantities)

    def test_leftovers(self):
        self.assertEqual(self.pattern.leftover, 60)

    def test_get_demand_quantities_hash(self):
        hash = self.pattern.get_demand_quantities_hash()
        self.assertEqual(hash[self.demands[0]], 10)
        self.assertEqual(hash[self.demands[1]], 10)
        self.assertEqual(hash[self.demands[2]], 10)

if __name__ == '__main__':
    unittest.main()
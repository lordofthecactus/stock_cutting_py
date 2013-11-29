import unittest
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_cutting_problem import *


class TestInitialPatternsFactory(unittest.TestCase):

    def setUp(self):
        self.stocks = [Stock(10,2)]
        self.demands = [Demand(4,2)]

    def test_leftovers(self):
        patterns = InitialPatternsFactory.get(self.stocks, self.demands)
        for pattern in patterns:
            self.assertEqual(pattern.leftover >= 0, True, "waste seems negative: %g" % pattern.leftover)

if __name__ == '__main__':
    unittest.main()
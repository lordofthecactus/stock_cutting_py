import unittest
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_cutting import *

from pprint import pprint


class TestInitialPatternsFactory(unittest.TestCase):

    def setUp(self):
        self.stocks = [Stock(630,10)]
        self.demands = [Demand(19,10), Demand(22,10), Demand(16,10)]

    def test_leftovers(self):
        patterns = InitialPatternsFactory.get(self.stocks, self.demands)

        for pattern in patterns:
            self.assertEqual(pattern.leftover >= 0, True, "waste seems negative: %g" % pattern.leftover)

if __name__ == '__main__':
    unittest.main()
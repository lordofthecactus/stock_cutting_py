import unittest
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_cutting import *


class TestGlpkMasterSetup(unittest.TestCase):

    def setUp(self):
        self.demands = [Demand(1,10)]
        self.stock = Stock(10,2)
        self.quantities = [8]
        self.pattern = CutPattern(self.stock, self.demands, self.quantities)
        self.op_cut = GlpkMasterSetup([self.pattern], [self.stock], self.demands)

    def test_demand_contraint_number(self):
        result = self.op_cut.demand_constraint_number()
        self.assertEqual(result, 1)

    def test_stock_available_constraint_number(self):
        result = self.op_cut.stock_available_constraint_number()
        self.assertEqual(result, 1)

    def test_get_constrains_bounds(self):
        result = self.op_cut.get_constrains_bounds()
        self.assertEqual(result,[10, (0.0, 2)])

    def test_get_demand_bounds(self):
        result = self.op_cut.get_demand_bounds()
        self.assertEqual(result, [10])

    def test_get_availability_bounds(self):
        result = self.op_cut.get_availability_bounds()
        self.assertEqual(result, [(0.0, 2)])

    def test_get_column_bounds(self):
        result = self.op_cut.get_column_bounds()
        self.assertEqual(result, [(0.0, None)])

    def test_get_leftovers(self):
        result = self.op_cut.get_leftovers()
        self.assertEqual(result, [2])

    def test_get_matrix(self):
        result = self.op_cut.get_matrix()
        self.assertEqual(result, [8, 1])

    def test_get_demand_matrix(self):
        result = self.op_cut.get_demand_matrix()
        self.assertEqual(result, [8])

    def test_get_availability_matrix(self):
        result = self.op_cut.get_availability_matrix()
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()
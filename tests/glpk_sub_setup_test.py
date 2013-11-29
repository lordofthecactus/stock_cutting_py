import unittest
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_cutting_problem import *


class TestGlpkSubSetup(unittest.TestCase):

    def setUp(self):
        self.demands = [Demand(1,10)]
        self.stock = Stock(10,2)
        self.deltas = [1]
        self.lamdas = [2]
        self.op_cut = GlpkSubSetup([self.stock], self.deltas, self.demands, self.lamdas)

    def test_demand_contraint_number(self):
        result = self.op_cut.demand_constraint_number()
        self.assertEqual(result, 1)

    def test_stock_available_constraint_number(self):
        result = self.op_cut.stock_available_constraint_number()
        self.assertEqual(result, 1)

    def test_get_constrains_bounds(self):
        result = self.op_cut.get_constrains_bounds()
        self.assertEqual(result,[1, (None, 0.0)])

    def test_get_stock_number_bounds(self):
        result = self.op_cut.get_stock_number_bounds()
        self.assertEqual(result, [1])

    def test_get_stock_length_bounds(self):
        result = self.op_cut.get_stock_length_bounds()
        self.assertEqual(result, [(None, 0.0)])

    def test_get_column_bounds(self):
        result = self.op_cut.get_column_bounds()
        self.assertEqual(result, [(0.0, None),(0.0, None)])


    def test_get_objective_coefficients(self):
        result = self.op_cut.get_objective_coefficients()
        self.assertEqual(result, [-3, 9])

    def test_get_demand_adjustments(self):
        result = self.op_cut.get_demand_adjustments()
        self.assertEqual(result, [-3])

    def test_get_stock_adjustments(self):
        result = self.op_cut.get_stock_adjustments()
        self.assertEqual(result, [9])

    def test_get_matrix(self):
        result = self.op_cut.get_matrix()
        self.assertEqual(result, [0, 1, 1, -10])

    def test_get_select_stock_matrix(self):
        result = self.op_cut.get_select_stock_matrix()
        self.assertEqual(result, [0, 1])

    def test_get_stock_length_matrix(self):
        result = self.op_cut.get_stock_length_matrix()
        self.assertEqual(result, [1, -10])

if __name__ == '__main__':
    unittest.main()
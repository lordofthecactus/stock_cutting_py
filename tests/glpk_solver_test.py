import unittest
import inspect
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from stock_cutting import *


class TestGlpkSolver(unittest.TestCase):

    def setUp(self):
        self.demands = [Demand(1,12)]
        self.stock = Stock(10,2)
        self.patterns = InitialPatternsFactory.get([self.stock], self.demands)


    def test_solve_master_problem(self):
        setup = GlpkMasterSetup(self.patterns, [self.stock], self.demands)
        solver = GlpkSolver(setup)
        lp = solver.solve()
        print 'Z = %g;' % lp.obj.value
        print '; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols)
        print 'Status %s' % lp.status
        #print '; '.join('{0}'.format(c.bounds) for c in lp.rows)
        #                    # Print struct variable names and primal values
        #print '; '.join('%s = %g' % (c.name, c.dual) for c in lp.rows)
        #                # Print struct variable names and primal values
        print "%g" % len(solver.duals)
        self.assertEqual(lp.status, 'opt')

    def test_solve_sub_problem(self):
        setup = GlpkMasterSetup(self.patterns, [self.stock], self.demands)
        solver = GlpkSolver(setup)
        lp = solver.solve()
        duals = solver.duals
        self.lamdas = duals[0:len(self.demands)]
        self.deltas = duals[len(self.demands):len(duals)]
        setup = GlpkSubSetup([self.stock], self.deltas, self.demands, self.lamdas)
        solver = GlpkSolver(setup)
        lp = solver.solve()
        print 'Status %s' % lp.status
        self.assertEqual(lp.status, 'opt')

    def test_solve_sub_problem2(self):
        stocks = [Stock(91, 200)]
        deltas = [0]
        demands = [Demand(25.5, 78), Demand(22.5, 40), Demand(20, 30), Demand(15, 30)]
        patterns = InitialPatternsFactory.highest_get(stocks, demands)
        setup = GlpkMasterSetupRelaxed(patterns, stocks, demands)
        solver = GlpkSolver(setup)
        lp = solver.solve()
        print 'Status %s' % lp.status
        print '; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols)
        print '; '.join('%g' % (d) for d in solver.duals)

        self.assertEqual(lp.status, 'opt')
        lamdas = [1.0/3, 1.0/4, 1.0/4, 1.0/6]
        setup = GlpkSubSetupRelaxed(stocks, deltas, demands, lamdas)
        solver = GlpkSolver(setup)
        lp = solver.solve()
        print 'Status %s' % lp.status
        print '; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols)
        self.assertEqual(lp.status, 'opt')


if __name__ == '__main__':
    unittest.main()
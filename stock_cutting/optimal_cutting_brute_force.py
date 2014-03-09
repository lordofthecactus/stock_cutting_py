from glpk_master_setup import *
from glpk_master_setup_relaxed import *
from glpk_sub_setup import *
from glpk_solver import *
from cut_pattern import *
from initial_patterns_factory import *

class OptimalCuttingBruteForce:
  def __init__(self, stocks, demands):
    self.stocks = stocks
    self.demands = demands
    self.patterns = InitialPatternsFactory.all_patterns(self.stocks, self.demands)

  def solve(self):
    lp, relaxed_value ,deltas, lamdas = self.optimize_patterns(self.patterns, self.stocks, self.demands)
    return lp, self.patterns


  def optimize_patterns(self, patterns, stocks, demands):
    setup = GlpkMasterSetup(patterns, stocks, demands)
    solver = GlpkSolver(setup)
    lp = solver.solve()
    duals = solver.duals
    print "duals:"
    print '; '.join('%g' % (d) for d in duals)
    lamdas = duals[0:len(self.demands)]
    deltas = duals[len(self.demands):len(duals)]
    return lp, solver.relaxed_value, deltas, lamdas

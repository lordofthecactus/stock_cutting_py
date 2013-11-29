import glpk
from glpk_master_setup import *

class GlpkSolver:
  def __init__(self, setup):
    self.setup = setup

  def solve(self):
    lp = glpk.LPX()        # Create empty problem instance
    lp.name = 'problem'     # Assign symbolic name to problem
    lp.obj.maximize = False # Set this as a minimization problem
    lp.rows.add(self.setup.row_number)         # Append three rows to

    for index, bound in enumerate(self.setup.row_bounds):
      lp.rows[index].bounds = bound
    lp.cols.add(self.setup.col_number)         # Append three columns to this instance

    for c in lp.cols:      # Iterate over all columns
      c.name = 'x%d' % c.index # Name them x0, x1, and x2
      c.bounds = 0.0, None     # Set bound 0 <= xi < inf
      c.kind = int

    lp.obj[:] = self.setup.obj_function   # Set objective coefficients
    lp.matrix = self.setup.matrix
    lp.simplex()           # Solve this LP with the simplex method
    self.duals = [r.dual for r in lp.rows]
    self.relaxed_value = lp.obj.value
    lp.integer()
    return lp
    # print 'Z = %g;' % lp.obj.value,  # Retrieve and print obj func value
    # print '; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols)
    #                        # Print struct variable names and primal values
    # print '; '.join('%s = %g' % (c.name, c.dual) for c in lp.rows)
                       # Print struct variable names and primal values



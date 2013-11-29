class GlpkSubSetup:
  def __init__(self, stocks, deltas, demands, lamdas):
    self.demands = demands
    self.lamdas = lamdas
    self.stocks = stocks
    self.deltas = deltas
    self.prepare_for_glpk()

  def prepare_for_glpk(self):
    self.row_number = 2
    self.col_number = self.demand_constraint_number() + self.stock_available_constraint_number()
    self.row_bounds = self.get_constrains_bounds()
    self.col_bounds = self.get_column_bounds()
    self.obj_function = self.get_objective_coefficients()
    self.matrix = self.get_matrix()

  def demand_constraint_number(self):
    return len(self.demands)

  def stock_available_constraint_number(self):
    return len(self.stocks)

  def get_constrains_bounds(self):
    return self.get_stock_number_bounds() + self.get_stock_length_bounds()

  def get_stock_number_bounds(self):
    return [1]

  def get_stock_length_bounds(self):
    return [(None, 0.0)]

  def get_column_bounds(self):
    return [(0.0, None)]*(self.demand_constraint_number() + self.stock_available_constraint_number())

  def get_objective_coefficients(self):
    return self.get_demand_adjustments() + self.get_stock_adjustments()

  def get_demand_adjustments(self):
    return [(- demand.length - self.lamdas[index]) for index, demand in enumerate(self.demands)]

  def get_stock_adjustments(self):
    return [(stock.length - self.deltas[index]) for index, stock in enumerate(self.stocks)]

  def get_matrix(self):
    return self.get_select_stock_matrix() + self.get_stock_length_matrix()

  def get_select_stock_matrix(self):
    return [0 for demand in self.demands] + [1 for stock in self.stocks]

  def get_stock_length_matrix(self):
    return [demand.length for demand in self.demands] + [-stock.length for stock in self.stocks]
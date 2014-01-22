class GlpkMasterSetup:
  def __init__(self, cut_patterns, stocks, demands):
    self.cut_patterns = cut_patterns
    self.stocks = stocks
    self.demands = demands
    self.prepare_for_glpk()

  def prepare_for_glpk(self):
    self.row_number = self.demand_constraint_number() + self.stock_available_constraint_number()
    self.col_number = len(self.cut_patterns)
    self.row_bounds = self.get_constrains_bounds()
    self.col_bounds = self.get_column_bounds()
    self.obj_function = self.get_leftovers()
    self.matrix = self.get_matrix()

  def demand_constraint_number(self):
    return len(self.demands)

  def stock_available_constraint_number(self):
    return len(self.stocks)

  def get_constrains_bounds(self):
    return self.get_demand_bounds() + self.get_availability_bounds()

  def get_demand_bounds(self):
    return [demand.quantity for demand in self.demands]

  def get_availability_bounds(self):
    return [(0.0, stock.quantity) for stock in self.stocks]

  def get_column_bounds(self):
    return [(0.0, None)]*len(self.cut_patterns)

  def get_leftovers(self):
    return [cut_pattern.stock.length + cut_pattern.leftover for cut_pattern in self.cut_patterns]

  def get_matrix(self):
    return self.get_demand_matrix() + self.get_availability_matrix()

  def get_demand_matrix(self):
    matrix = [cut_pattern.demand_quantities_hash[demand] for demand in self.demands for cut_pattern in self.cut_patterns]
    return matrix

  def get_availability_matrix(self):
    matrix = []
    for stock in self.stocks:
      for cut_pattern in self.cut_patterns:
        if cut_pattern.stock == stock:
          matrix.append(1)
        else:
          matrix.append(0)
    return matrix




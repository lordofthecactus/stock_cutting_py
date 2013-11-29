from collections import defaultdict

class CutPattern:
  def __init__(self, stock, demands, quantities):
    self.stock = stock
    self.demands = demands
    self.quantities = quantities
    self.leftover = self.calculate_leftover()
    self.demand_quantities_hash = self.get_demand_quantities_hash()

  def calculate_leftover(self):
    sum = 0
    for index, demand in enumerate(self.demands):
      sum += self.quantities[index] * demand.length
    return self.stock.length - sum

  def get_demand_quantities_hash(self):
    hash = defaultdict(int)
    for index, demand in enumerate(self.demands):
      hash[demand] = self.quantities[index]
    return hash







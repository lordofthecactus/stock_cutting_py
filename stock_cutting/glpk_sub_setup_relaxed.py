from glpk_sub_setup import *
class GlpkSubSetupRelaxed(GlpkSubSetup):
  def get_demand_adjustments(self):
    return [(- demand.length - self.lamdas[index]) for index, demand in enumerate(self.demands)]
  def get_stock_adjustments(self):
    return [(2 * stock.length - self.deltas[index]) for index, stock in enumerate(self.stocks)]
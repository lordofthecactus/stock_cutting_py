from glpk_master_setup import *
class GlpkMasterSetupRelaxed(GlpkMasterSetup):
  def get_demand_bounds(self):
    return [(demand.quantity, None) for demand in self.demands]
  def get_leftovers(self):
      return [cut_pattern.leftover + cut_pattern.stock.length for cut_pattern in self.cut_patterns]

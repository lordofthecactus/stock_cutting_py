from glpk_master_setup import *
class GlpkMasterSetupRelaxed(GlpkMasterSetup):
  def get_demand_bounds(self):
    return [(demand.quantity, None) for demand in self.demands]
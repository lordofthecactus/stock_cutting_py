from cut_pattern import *
import math
class InitialPatternsFactory:
  @staticmethod
  def get(stocks, demands):
    patterns = []
    for stock in stocks:
      for demand in demands:
        for i in range(1, stock.length + 1):
          new_pattern = CutPattern(stock, [demand], [i])
          if new_pattern.leftover >= 0:
            patterns.append(new_pattern)
          else:
            break
    return patterns

  @staticmethod
  def highest_get(stocks, demands):
    patterns = []
    for stock in stocks:
      for demand in demands:
        for i in range(1, stock.length + 1):
          new_pattern = CutPattern(stock, [demand], [i])
          if new_pattern.leftover >= 0 and new_pattern.leftover - demand.length < 0:
            patterns.append(new_pattern)
    return patterns

  @staticmethod
  def simple_get(stocks, demands):
    patterns = []
    stock = stocks[0]
    for demand in demands:
      new_pattern = CutPattern(stock, [demand], [1])
      patterns.append(new_pattern)
    return patterns

  @staticmethod
  def fill_stocks(stocks, demands):
    patterns = []
    sorted_demands = sorted(demands, key=lambda demand: demand.length, reverse=True)
    for stock in stocks:
      for demand in sorted_demands:
        left_to_fulfill = demand.quantity
        for i in range(0,len(patterns)):
          if left_to_fulfill == 0:
            break
          pattern = patterns[i]
          length_available = pattern.leftover
          to_add = math.floor(length_available * 1.0 / demand.length)

          if to_add > left_to_fulfill:
            to_add = left_to_fulfill

          if to_add >= 1.0:
            pattern.demands.append(demand)
            pattern.quantities.append(to_add)
            patterns[i] = CutPattern(stock, pattern.demands, pattern.quantities)
            left_to_fulfill -= to_add
        while left_to_fulfill != 0:
          print left_to_fulfill
          to_add = math.floor(stock.length * 1.0 / demand.length)

          if to_add > left_to_fulfill:
            to_add = left_to_fulfill

          if to_add >= 1.0:
            new_pattern = CutPattern(stock, [demand], [to_add])
            left_to_fulfill -= to_add
            if not InitialPatternsFactory.is_duplicate(patterns, new_pattern):
              patterns.append(new_pattern)
    return patterns


  @staticmethod
  def is_duplicate(patterns, pattern):
    for p in patterns:
      if sorted(p.demands) == sorted(pattern.demands) and sorted(p.quantities) == sorted(pattern.quantities):
        return True
    return False

  @staticmethod
  def all_patterns(stocks, demands):
    current_patterns = []
    for stock in stocks:
        new_pattern = CutPattern(stock, demands, [0] * len(demands))
        current_patterns.append(new_pattern)
    for i in xrange(len(demands)):
      current_patterns = current_patterns + InitialPatternsFactory.recursive_pattern(current_patterns, i)
    return current_patterns

  @staticmethod
  def recursive_pattern(current_patterns, demand_index):
    new_patterns = []
    for pattern in current_patterns:
      new_pattern = pattern
      while True:
        new_quantities = list(new_pattern.quantities)
        new_quantities[demand_index] = new_quantities[demand_index] + 1
        new_pattern = CutPattern(new_pattern.stock, new_pattern.demands, new_quantities)
        if new_pattern.leftover >= 0:
          new_patterns.append(new_pattern)
        else:
          break
    return new_patterns




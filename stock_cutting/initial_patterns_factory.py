from cut_pattern import *
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
  def simple_get(stocks, demands):
    patterns = []
    stock = stocks[0]
    for demand in demands:
      new_pattern = CutPattern(stock, [demand], [1])
      patterns.append(new_pattern)
    return patterns

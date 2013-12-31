from stock_cutting import *

# stocks = [Stock(400,4), Stock(260,1)]
# demands = [Demand(55,10), Demand(43,9), Demand(19,17), Demand(62,2)]
# stocks = [Stock(1200,10000)]
# demands = [Demand(100,100), Demand(200,2), Demand(300,2), Demand(493,250), Demand(590,2), Demand(630,2), Demand(780,2), Demand(930,2)]

# stocks = [Stock(218, 100000)]
# demands = [Demand(81, 44), Demand(70, 3), Demand(68,48)]

# stocks = [Stock(5600, 100)]
# demands =[Demand(1380,22),Demand(1520,25),Demand(1560,12),Demand(1710,14),Demand(1820,18),Demand(1880, 18),Demand(1930,20),Demand(2000,10),Demand(2050,12),Demand(2100,14),Demand(2140,16),Demand(2150,18),Demand(2200,20)]

stocks = [Stock(57,21)]
demands = [Demand(18, 35), Demand(21, 9), Demand(27,5)]

initial_patterns = InitialPatternsFactory.get(stocks, demands)
oc = OptimalCutting(stocks, demands)
lp, patterns = oc.solve()
print 'Z = %g;' % lp.obj.value
print '; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols)
print 'Status %s' % lp.status

patterns.pop()
used = 0

for index, pattern in enumerate(patterns):
  if lp.cols[index].primal >= 1:
    used += lp.cols[index].primal
    print "stock specs:"
    print "\tlength: %g" % pattern.stock.length
    print "\tavailable: %g" % pattern.stock.quantity
    print "\tuse: %g" % lp.cols[index].primal
    print '\tcuts:'
    for index, demand in enumerate(pattern.demands):
      print '\t\tlength: %g, number_cuts: %g' % (demand.length, pattern.quantities[index])
    print "\t\twaste: %g" % pattern.leftover
print "Stocks used: %g" % used

# print "This are all the new patterns generated-------"
# for index, pattern in enumerate(patterns[len(initial_patterns):len(patterns)]):
#   print "stock specs:"
#   print "\tlength: %g" % pattern.stock.length
#   print "\tavailable: %g" % pattern.stock.quantity
#   print "\tuse: %g" % lp.cols[index].primal
#   print '\tcuts:'
#   for index, demand in enumerate(pattern.demands):
#     print '\t\tlength: %g, number_cuts: %g' % (demand.length, pattern.quantities[index])
#   print "\t\twaste: %g" % pattern.leftover

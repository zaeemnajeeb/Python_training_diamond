############################################################
#
#    generators
#
############################################################

from math import sqrt

roots = (sqrt(x) for x in range(10))

print(sum(roots))   # consume the generator - calculates everything at once and outputs
print(sum(roots))   # the generator is now empty








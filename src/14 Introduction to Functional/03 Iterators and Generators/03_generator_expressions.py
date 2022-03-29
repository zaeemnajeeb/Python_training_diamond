############################################################
#
#    generator expressions
#
############################################################

from math import sqrt

# generator expressions are comprehensions
# evaluate each expression on demand (lazy evaluation)

# use round brackets to return a generator expression (comprehension):
#for every x in the rang 0 to 9, generate sqrt of x
#Generat will not calculate it UNTIL next is called (or in loop)
roots = (sqrt(x) for x in range(10))

# iterate using the generator
for r in roots:
    #calculates the sqrt and outputs it, removing it from the generator
    print("{0:6.2f}".format(r), end=' ')
print()


# comprehensions behave like generator expressions (but are evaluated immediately)
roots = [sqrt(x) for x in range(10)]
for r in roots:
    print("{0:6.2f}".format(r), end=' ')
print()



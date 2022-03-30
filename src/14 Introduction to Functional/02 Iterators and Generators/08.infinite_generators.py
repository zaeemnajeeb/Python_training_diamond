'''
Infinite Generators
===================

Generator functions that never return give rise to infinite generators.  These generators called by called
for ever.  In this example we use next() to get numbers from the generator.  Note the generator runs for ever
and never gets reset.
'''

def powers(x): # generator
    while(True): #THIS HAS NO LIMIT
        x = x * 2
        yield x

# create the infinite generator, initialized with 55
g = powers(55) #set x = 55 in the generator object

x = 0
while x < 1000: #would continue forever if no limit
    x = next(g)
    print(x, end=", ")
print()
    
for n in range(10): # will carry on from last x value
    print(next(g), end=", ") 
print()
       

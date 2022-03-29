############################################################
#
#    comprehensions
#
############################################################

from math import sqrt

def cube(x):
    return x * x * x

# set up a sequence
sequence = list(range(1, 20))

# apply a comprehension to entire sequence
#RESULT IS A LIST
#read as: for every x in this sequence, calculate sqrt(x)
#x is not changing, each x is a element in the sequence
roots = [sqrt(x) for x in sequence]
#for every x in the sequence, provided x<10, return x
n     = [   x    for x in sequence if x < 10 ]
#for every x in the sequence, provided x/2 has no remainder, cube x
cubes = [cube(x) for x in sequence if x%2==0 ]

print(roots)
print(n)
print(cubes)

# other examples
#a typical example
#for every x in the range 1 to 13 AND for every y in the range of 1 to 13, 
#if x*y>120, calculate the sum of x and y (only 4 ways here)
print([ x + y for x in range(1,13) for y in range(1,13) if x*y > 120])
#for every x in the range 1 to 13 AND for every y in the range of 1 to 13, 
#if x*y>120, return the tuple of x and y (only 4 ways here)
print([(x,y) for x in range(1,13) for y in range(1,13) if x*y > 120])

# primes
n = 1000 #some arbitrary stopping point
#BAD EXAMPLE
primes = [p for p in range(2, n)
           if p not in
            [np for i in range(2, int(n**0.5) + 1)  # i = 2,3,..31 
                for np in range(i * 2, n, i)]]  # np = 4,6,8 .. + 6,9,12 .. + 8,12,16 .. + 10,15,20 ..
print(primes)

#GOOD EXAMPLE
def isprime(num):
    #check that there is only 1 other way to get no remainder
    return not [y for y in range(2,num) if num%y==0]
#for every x in that range, if the function returns true, return x
print([x for x in range(2,1000) if isprime(x)])


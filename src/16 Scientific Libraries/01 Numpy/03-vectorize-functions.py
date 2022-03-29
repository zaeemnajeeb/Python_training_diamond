import numpy as np
np.set_printoptions(precision=3)

# this only works for scalars
#annonymous function of bytecode which function points at
def square(x): return x * x

# vectorize function to return floats
#new annonymous function of bytecode
#works with lists if there is more than 1 function
square = np.vectorize(square, otypes=[np.float])
x = range(5, 10)
print(square(x))         # now works for vectors
print(square(10))        # but still works for scalars


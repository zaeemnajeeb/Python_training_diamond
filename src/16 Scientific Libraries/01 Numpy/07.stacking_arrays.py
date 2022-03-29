'''
Stacking Arrays
===============

In some situations you will want to combine arrays; we can "stack" arrays horizontally or vertically:
'''

import numpy as np

a = np.ones( (3,5) ); print(a)
b = np.zeros( (3,5) ); print(b)

print("stacking")
h = np.hstack( (a,b) ); print(h) #maintain 1D array
v = np.vstack( (a,b) ); print(v)#make 2D array

<<<<<<< Updated upstream:src/16 Scientific Libraries/01 Numpy/07.stacking_arrays.py

=======
>>>>>>> Stashed changes:src/16 Scientific Libraries/01 Numpy/07-stacking-arrays.py

############################################################
#
#    reshaping arrays
#
############################################################

import numpy as np

# create array
a = np.arange(24); print(a)
# reshape it - NOTE the shape should match with the original dimension
b = a.reshape(2,3,4); print(b) # b points to a, different shape
a[13] = 99
print(a)
print(b) # ARRAYS ARE MUTABLE
# display properties held in the view
print(type(b))
print("Shape:", b.shape) #shows shape
print("Dimensions:", b.ndim) #dimensions (3 here as reshaped)
print("Size:", b.size) # number of elements?
print("Item type:", b.dtype.name) 
print("Item size:", b.itemsize)

1

import numpy as np
np.set_printoptions(precision=3) #limit to 3 decimal places

# start with a float64 array
#Creates a 4 by 4 function, numbered appropiately (1,1), (1,2) etc.
array1 = np.fromfunction(lambda i,j: (i+2)*(j+2)**1.4, (4,4))
print(array1.dtype)
print(array1)

# casting creates a new array of int
array2 = array1.astype(int) #cast to integers
#######NOTE THIS TRUNCATES
print(array2.dtype)
print(array2)

# casting creates a new array of bool
array3 = array1.astype(bool)
####If 0 present, make it a FALSE, others will be TRUE
print(array3.dtype) 
print(array3)

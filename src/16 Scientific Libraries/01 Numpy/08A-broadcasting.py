############################################################
#
#    broadcasting
#
############################################################

import numpy as np

X = np.arange(1,7) # 1D array
Y = np.arange(1,5) #1D array
print("X and Y are 1D arrays")
print(X)
print(Y)

Y = np.vstack(Y) #vertical stack makes into 2D array
# [[1], [2], [3], [4]]
print("\nY is now a 2D array")
print(Y)
print("\nX is still a 1D array")
print(X)

print("\nbroadcast X and Y, because arrays are different sizes")
M = X * Y 
print(M) #Creates a temporary array for X into a 2D array
''' 
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6

1 1 1 1 1 1
2 2 2 2 2 2
3 3 3 3 3 3
4 4 4 4 4 4
''' # CAN NOW DO ELEMENT BY ELEMENT OPERATIONS



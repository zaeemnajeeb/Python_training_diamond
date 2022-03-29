############################################################
#
#    try-except-else statements
#
############################################################

from math import sqrt
try:
    x = int(input("Enter positive integer: "))
    root = sqrt(x)
except Exception as e:
    print("sqrt() failed ...")
    print(e)
    return
else: #ONLY run if no Exception raised
    #THIS WILL NEVER RUN IF THERE IS EXCEPTION
    print("sqrt() succeeded ...")
    print(root)
 


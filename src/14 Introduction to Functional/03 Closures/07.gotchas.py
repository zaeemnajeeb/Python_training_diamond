'''
Gotchas
========

Recall the closures will be on mutable variables and r-valued immutable variables.  In this gotcha we are
trying to use y from the "outer" function in "inner".  The code looks OK, but the lines
        z = y * 2
        y = z
defines a new local variable "y" because y is used an an l-value (left hand side of =) on the second line.
The second line now refers to the local y which is so far undefined and hence the line raises an exception.

Thus the code fails.
'''

def f(x):
    y = x * x       # defines a local variable
    print(("locals for f(): ", locals()))  #show locals which are x and y so far      
    def inner(): # nested function
        print(("locals for inner(): ", locals())) #       
        z = y * 2   # defines a new local variable y
                    # hence the RHS of this expression refers to the local y which is undefined 
                    #SO ERROR CAUSED BY LINE 22 where you are trying to modify immutable object

        y = z       # this raises UnboundLocalError exception
        return y
    inner()
    print(y)
    return inner()

try:
    print((f(5)))
except UnboundLocalError as e:
    print(e)
    

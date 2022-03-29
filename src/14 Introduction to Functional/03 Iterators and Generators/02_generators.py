############################################################
#
#    generators
#
############################################################

# functions that contain yield return an iterator
# by calling said function
#THIS IS EASIER THAN WRITING AN ITERATOR
def powers():
    x = 1
    while(x < 1000):
        x = x * 2
        #yield is effectively the return within the __next__() of iterator
        yield x #yield so working with generator
        #effectively created an iterator in the background
        #THIS ALSO CHANGES THE FUNCTION TO A CLASS IN THE BACKGROUND
        pass # just to show execution resumes after the yield
    return # return here to make it the equiv of the Stop iteration of an iterator
    #If no return, python puts it in itself (return None)

# calling the function produces a generator object, which is also an iterator
# note: calling the function does NOT execute the code in the function
g = powers()
#CODE NOT DONE YET, calculation only occurs once tryin to print
print(g)

# check that g has both iterator methods - via hasattr()
print("Does g have an '__iter__' function:", hasattr(g, "__iter__"))
print("Does g have an '__next__' function:", hasattr(g, "__next__"))
#Both are TRUE therefore the function is now pointing to a background class

# look at all the methods
print(dir(g))

# check the identity of the generator object
print(f"{id(g):x}")
# check the identity of the object returned by __iter__() is the same
i = g.__iter__()
print(f"{id(i):x}")

# call __next__ directly (discouraged)
#goes into the function, stops at yield and prints x*2 = 2
print(g.__next__())
#THIS WILL RESUME ON LINE IMMEDIATELY AFTER THE YIELD
print(g.__next__())

# use the global function next (recommended) (same as above but neater)
print(next(g))
print(next(g))

# use g in a loop as an iterator (not the call powers() to instantiate a new generator)
for n in powers():
    #AKA retrieve things from the generator
    print(n)
    

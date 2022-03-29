############################################################
#
#    iterators
#
############################################################

# There is special language support for iterator in the for of a loop
# iterators must support two methods: __iter__ and __next__
 
class Fibonacci:
    def __init__(self): #called on initiation
        #self is something that points to the dictionary
        self.x,self.y = 0,1 # first 2 numbers to start with
        
    def __iter__(self):
        return self  # the object on which to call next() - usually yourself

    def __next__(self):
        if self.x > 100:
            #Alternatice exit path
            #this will remove you from the loop
            raise StopIteration # indicate end of iteration
        #Main exit path
        self.x, self.y = self.y, self.x + self.y
        return self.x

    
# create an instance of class and invoke iterator methods
# __iter__(self) will be called once
# __next__(self) will be called repeatedly until loop terminates

#Fibonacci will create an instance of that class
for f in Fibonacci():
    print(f, end=", ")


# The above loop gets translated to:
#
# try:
#     fib = Fibonacci() #same as iter
#     iter = fib.__iter__() #call the iter method to determine what object to iterate on

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")

#     f = iter.__next__()
#     print(f, end=", ")
# except StopIteration as e:
#     pass









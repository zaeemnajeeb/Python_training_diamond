############################################################
#
#    fibonacci sequence
#
############################################################

def fib(n):#fib is pointer to the bytecode
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

fib(1000)

# create another object reference to the function
f = fib #points to the same bytecode
# call the function through the new object reference
f(100)

# change the original reference
fib = 56.3 #fib now points to float
print(fib) #NO LONGER POINTS TO THE FUNCTION

# we can still call the function with the new reference
f(50) #unaffected by fib changing

1


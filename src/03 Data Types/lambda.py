#functions are both pointers and objects
def f(): #f is the pointer, the bytecode in the function is the object
    return ("Hi")

g = lambda: "Hello" #cant put print in this
#EQUIVALENT
print(g())
print(f())

def F(x):
    return x* x

G = lambda x : x*x

#EQUIVALENT
print(F(3))
print(G(4))
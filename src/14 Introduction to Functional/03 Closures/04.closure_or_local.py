'''
Closure or Local
================

Nested functions have access to their environment using closures.  However, this only applies to mutable items
or immutable items that are used as r-values (appear on the right hand sign of = or passed to other functions, 
such as print()).

In the example below, the nested function uses variables y1 and y2.  Since these are defined in the parent 
function its tempting to think they are part of the closure.  However, since we are assigning values to y1 an y2,
we can't be referring to the parent's y1 and y2.  In fact y1 and y2 are local variables.  Note that y3 is also 
immutable, but is used as an r-value and is therefore part of the closure and not a local variable. 
'''

def printClosures(fn): #prints closures
    closure = fn.__closure__
    if closure is None: return ""
    for c in closure:
        print("closure: {:20s}{}".format(str(c.cell_contents), c))
    print("locals:", fn.__code__.co_varnames)

def f1():
    x1 = [10, 20, 30, 40]     # mutable list
    x2 = {}                   # mutable dict
    y1 = 11                   # immutable
    y2 = None                 # immutable
    y3 = "hello"              # immutable
    def f2():
        # note y1 and y2 are locals, not closures
        # y3 is used as an r-value and is part of the closure

        x1[0] = 99 # act on closure as list is mutable - edits the closure
        x2['red'] = 255 #dict also mutable so act on closure
        y1 = 10 #immutable so dont change closure, so must define local variable (outer y1 not changed)
        y2 = y3 #putting on right hand side makes it an r-value. Just trying to read it so is closure.
        #
    f2()
    printClosures(f2)

f1()

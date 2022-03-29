#immutable variables

def addone(x):
    print(id(x))
    x += 1 #creates new object for x
    print(id(x))
    return x #return address

a = 100
print(id(a))
a = addone(a) #copy new address to a
#when f(a) done, x in function now also points
#to 100. This is then increased to 101 and new id
print(id(a)) # a had new address
#THEREFORE MUST ALSO ASSIGN new address

#mutable variable
def addonetolist(l):
    l[0] +=1 #NO return needed

mylist = [100, 200, 300]
addonetolist(mylist)
print(mylist) #LIST WAS UPDATED withoout assignment

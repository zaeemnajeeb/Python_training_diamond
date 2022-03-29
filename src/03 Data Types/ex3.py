x = [2, 3, 5] # x points at a list
y = x # y points at the same list

print(id(x))
print(id(y))
x[1] = 99 # lists are mutable, so we can change the list
print(x[1])
print(y[1])
print(id(x))
print(id(y))

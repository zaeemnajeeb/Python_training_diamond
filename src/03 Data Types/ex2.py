x = 100 # x points at integer 100
y = x # y points at the same place as x, being at 100. This effectively copies x address into y
x +=1 #add one. this points at a brand new integer rather than single increment.
#all interefers are IMMUTABLE - can not be changed. So integers CAN NOT BE CHANGED
#, instead creating something new
print(x, id(x))
print(y, id(y))
print(id(100))
print(id(101))
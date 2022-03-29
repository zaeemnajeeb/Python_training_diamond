wine = "MiXeD CaSe"

wine.upper()
print(wine) # THIS WILL NOT APPLY THE METHOD
new = wine.upper() #this is a function on a immutable object
#ABOVE METHOD WILL RETURN A NEW OBJECT SO MUST ASSIGN
print(new) # this will now print something

#Applying method to mutable objects
myList = [100 ,200, 300]
myList.append(99) 
print(myList) #THIS WILL WORK DUE TO BEING MUTABLE

myList = [100 ,200, 300]
myList = myList.append(99) 
#THIS WILL PRINT NOTHING AS .append() RETURNS NOTHING

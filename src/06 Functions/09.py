def average(*args):#wrap all params inside tuple
    print(args, type(args)) 
    result = sum(args)/len(args) #sum all things within tuple
    return result

result = average(4,6,7,8,3)
print(result)

#USING A LIST:
l = [4,6,7,8,3]
result = average(*l) #unwrap the list/tuple
print(result)#ALSO WORKS NOW for tuple or list
result = average(3,5,1,23,4)
def volume(height, depth, width):
    return (height + 2) * (width + 10) * depth

print( 'eg1:',volume (height = 12, depth = 20, width = 30))
#can pass named in any order you like unlike positional
print('eg2:', volume (depth = 20, height = 12, width = 30))

#THIS IS SIMILAR TO KEY-VALUE PAIRS
def volume2(**kwargs): #wrap key-word arguements 
    #now input is a dictionary
    #NOTE 2 *'s due to passing in a key and value
    print(type(kwargs), kwargs)
    return (kwargs['height'] + 2)* (kwargs['width']+10) * kwargs['depth']

print('eg3:',volume2 (height = 12, depth = 20, width = 30))

#IF INPUT IS ALREADY A DICTIONARY:
mydict = {'height':12, 'width': 30, 'depth':20}
print( 'eg4:', volume2(**mydict))#MUST UNWRAP FIRST

def both (*args, **kwargs): #args MUST BE FIRST
    print(*args, type(args))
    print(type(kwargs), kwargs)
both(321, 44, height = 12, depth = 20, width = 30,)

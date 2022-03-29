# dictionary comprehension
#for every x in the tuple, x squared is key and cube of x is the value
squares = {x**2: x**3 for x in (2, 4, 6)}
print(squares)

# BAD EXAMPLE BUT in the manual
department = 'Silly Walk'
#for every x in department, where x is a character, set the key as the character
#and the value is the number of occurences of that character (via count())
print({x: department.count(x) for x in department})
# {'a': 1, ' ': 1, 'i': 1, 'k': 1, 'l': 3, 'S': 1, 'W': 1, 'y': 1}

#for every x in department, can you put x in the set.
#THIS EFFECTIVELY REMOVES DUPLICATES
print({x for x in department})



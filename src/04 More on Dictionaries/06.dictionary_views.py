'''
Dictionary Views
================
The objects returned by dict.keys(), dict.values() and dict.items() are view objects.  They provide a dynamic 
view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
The view returned is essentially a list.  However, the view object has the best of both worlds: it behaves as 
a list container, and yet does not make a copy of the dictionary! It is, in fact, a kind of a virtual read-only 
container that works by linking to the underlying dictionary.  Furthermore, it is easy to created a separate
list from the view.

Let's take a look at how this works with dict.values().
'''

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
k = d.values()

# convert to a list
l = list(k)
print(f"list: {l}")

# check type
print(f"type: {type(k)}")

# print the values view
print(f"view: {k}")
d['one'] = 99

# check the view has changed
print(f"updated view: {k}")

# check the list hasn't changed
print(f"list: {l}")

import sys

'''
Add elements to a dictionary and print the 
size of the dictionary every time the size changes
'''

d = {} #empty dictionary
#as dictionary fills, hash codes can overlap
#if there are lots of collisions, algorithm slows down
#python will double the size of the dictionary when this occurs
#which therefore requires everything in the dictionary to be rehashed
old_size = sys.getsizeof(d)
for i in range(100000):
    key = f"key{i}"
    value = f"value{i}"
    d[key] = value
    new_size = sys.getsizeof(d)
    if new_size > old_size:
        print(f"no of keys = {i} : bytes = {new_size}")
    old_size = new_size

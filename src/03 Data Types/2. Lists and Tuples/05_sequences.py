############################################################
#
#    sequences
#
############################################################

# set up sequences
sequence1 = 2, 3, 5, 7, 11, 13, 17
print(type(sequence1))
sequence2 = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
sequence3 = 66, 24, 17, 25, 51, 98, 78

# iterate through sequence
for value in sequence1:
    print(value, end=' ... ')
print()

# use enumerate
for i, value in enumerate(sequence1):
    print(i, value, end=' ... ')
print()

# iterate through three sequences at once
for value1, value2, value3 in zip(sequence1, sequence2, sequence3):
    print(value1, value2, value3, end=' ... ')
print()

# iterate in reverse
for value in reversed(sequence3):
    print(value, end=' ... ')
print()

# iterate in sorted sequence
for value in sorted(sequence3):
    print(value, end=' ... ')
print()

<<<<<<< Updated upstream:src/03 Data Types/2. Lists and Tuples/05_sequences.py
# using range
for x in range(1, 5):
    print(x)

=======
for x in range(5) :
    print (x)
>>>>>>> Stashed changes:src/03 Data Types/Lists, Tuples/05_sequences.py

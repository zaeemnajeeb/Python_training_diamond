############################################################
#
#    sorting-dictionaries
#
############################################################

# dictionaries can't be sorted, but we can print out
# key value pairs in lexical order (see previous example)

# 1. Read in dictionary from file
phones = {} # empty dictionary
try: #in case things go wrong
    f = open("data/codes.txt", "r")
<<<<<<< Updated upstream:src/03 Data Types/4. Dictionaries/06_file_to_dictionary.py
    for line in f:
        theList = line.rstrip().split(' ')
        value = theList[0]
        x = theList[1:]
        print(x)
        y = "".join(x)
        print(y)
        key = " ".join(theList[1:])
        phones[key] = value
=======
    for line in f: #f is file object in memory, where f points to it
        theList = line.rstrip().split(' ') #split line string via space
        value = theList[0] #rstrip removes \n and spaces at end
        #names with spaces within will also be split therefore add all together
        key = " ".join(theList[1:]) # join all into a string, separated by " "
        phones[key] = value #add to dictionary
>>>>>>> Stashed changes:src/03 Data Types/Dictionaries/06_file_to_dictionary.py
except IOError as e:
    print("Reading data from file failed!")
    print(e)
finally: 
    f.close()

# 2. Sort the keys
sortedKeys = list(phones.keys())
sortedKeys.sort()

# 3. Iterate through sorted list
for key in sortedKeys:
    print(key + ":" + phones[key])

# 4. Search for a given value    
print(phones['District of Columbia'])
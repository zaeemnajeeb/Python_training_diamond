############################################################
#
#    Reading a file
#
############################################################

# successful read
#written as exception handling
#will look for problems
try: 
    #f points at a file object
    f = open("data/hello.txt", "r") #open in read only mode
    try:
        #allows to look at 1 line at a time
        for line in f:
            print(line, end=" ")
        #automatically exits the loop as f is an iterator
    finally:
        f.close()
        #can reach a limit to how many files can be open at once
        #therefore close to avoid obscure errors
        
except IOError as e:
    print(e)


# unsuccessful read
try: 
    f = open("./data/unknown-file.txt", "r")
    try:
        for line in f:
            print(line, end=" ")
    finally: #WILL ALWAYS BE CALLED REGARDLESS OF ERROR
        f.close()
#if any errors occur above, go to except branch
except IOError as e:
    print(e)


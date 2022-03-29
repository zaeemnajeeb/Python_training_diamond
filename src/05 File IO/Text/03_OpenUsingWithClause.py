############################################################
#
#    Using with
#
############################################################

# successful read
try:
    with open("data/hello.txt", "r") as f:
        for line in f:
<<<<<<< Updated upstream:src/05 File IO/Text/03_OpenUsingWithClause.py
            print(line, end="")
=======
            print(line, end=" ")
#WILL AUTOMATICALLY CLOSE THE FILE - as if a finally is here
>>>>>>> Stashed changes:src/05 File IO/03_OpenUsingWithClause.py
except IOError as e:
    print(e)

# unsuccessful read
try:
    with open("data/unknown-file.txt", "r") as f:
        for line in f:
<<<<<<< Updated upstream:src/05 File IO/Text/03_OpenUsingWithClause.py
            print(line, end="")
=======
            print(line, end=" ")
    #WILL AUTOMATICALLY CLOSE THE FILE - as if a finally is here
>>>>>>> Stashed changes:src/05 File IO/03_OpenUsingWithClause.py
except IOError as e:
    print(e)



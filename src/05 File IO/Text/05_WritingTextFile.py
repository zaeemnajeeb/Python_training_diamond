############################################################
#
#    Writing to a file
#
############################################################

def writeFileContents(filename, data):
    try: 
<<<<<<< Updated upstream:src/05 File IO/Text/05_WritingTextFile.py
        # w (write) will empty an existing file before opening it
        f = open(filename, "w")
        f.writelines(data)
=======
        #NOTE w+ will empty an existing file before opening it
        f = open(filename, "w+")
        f.writelines(data) #writes all lines in 1 go
>>>>>>> Stashed changes:src/05 File IO/05_WritingTextFile.py
    except IOError as e:
        print(e)
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws
<<<<<<< Updated upstream:src/05 File IO/Text/05_WritingTextFile.py

FILENAME = "data/text.txt"
=======
#tuple instead of a list, and \n for new lines
>>>>>>> Stashed changes:src/05 File IO/05_WritingTextFile.py
data = ("line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5\n")
writeFileContents(FILENAME, data)

import os
os.system(f"cat {FILENAME}")



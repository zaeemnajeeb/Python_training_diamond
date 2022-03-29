############################################################
#
#    Writing to a file
#
############################################################

def writeFileContents(filename, data):
    try: 
        #NOTE w+ will empty an existing file before opening it
        f = open(filename, "w+")
        f.writelines(data) #writes all lines in 1 go
    except IOError as e:
        print(e)
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws
#tuple instead of a list, and \n for new lines
data = ("line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5\n")
writeFileContents("data/text.txt", data)


1
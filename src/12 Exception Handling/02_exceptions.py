# define two tag classes
class TooBig(Exception): pass
class MuchTooBig(Exception): pass

import os; os.system("clear") #run unix command to clear 

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 400
        y = 0
        
        if x > 150:
            raise MuchTooBig() #instantiate the object
        if x > 50:
            raise TooBig() #instantiate the object
        print(f"x is {x}")
        print(f"x/y is {x/y}")
    except TooBig as e: #e is NOW blank
        print(f"--{e}--")# e = ""
        print("x is too big")
    except MuchTooBig as e:
        print("x is much too big")
    except Exception as e: #DONT PLACE 1st as the subclasses inherit this
        print(e) #if this except is first, only this will be raised


main()

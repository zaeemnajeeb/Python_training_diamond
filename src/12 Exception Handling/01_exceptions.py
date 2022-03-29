<<<<<<< Updated upstream
# C++ uses:    try throw catch
# Python uses: try raise except

import os; os.system("clear")
=======
# try throw catch
# try raise except
import os; os.system("clear") #run unix command to clear 

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 400
        y = 0
        
        if x > 150:
            raise Exception("x is much too big")
        if x > 50:
            raise Exception("x is too big")
    
        print(f"x is {x}")
        print(f"x/y is {x/y}") #exception thrown here
    except Exception as e: #error message is e
        #Python runtime also has some standard errors like divide by 0
        print(e) #this is the same as print(e.__str__())
        #__str__ is done by default if nothing specified


main() # run

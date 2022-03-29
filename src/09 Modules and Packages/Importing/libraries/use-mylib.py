#imports directly, requiring the __name__ check to prevent tests running
import mylib as lib 

#copies symbol table to this file directly
#CAN CAUSE NAME CLASHES
#from mylib import *

lib.f1()
lib.f2()
lib.f3()
lib.f4()

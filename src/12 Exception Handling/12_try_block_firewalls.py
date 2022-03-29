class BigProblem(Exception): pass
class SmallProblem(Exception): pass

# example to demonstrate structuring of try blocks
# to handle minor errors in low level code, 
# but major problems in top level code.

def main():
    try:
        part1()
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        part2(500)
        part3()
        part4()
    except BigProblem as e:
=======
=======
>>>>>>> Stashed changes
        part2(500) #2 types of exceptions possible
        part3() #always runs UNLESS BigProblem
        part4() #always runs UNLESS BigProblem
    except BigProblem as e: #handle BigProblem
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        print(e)
def part1():
    print("part 1")
def part2(x): #Try block in part 2
    try:
        if x > 100:
            raise BigProblem("part 2 failed spectacularly")
        elif x > 10:
            raise SmallProblem("part 2 failed")
        else:
            print("part 2 completed")
    # handle small problems locally, but
    # big problems break through the firewall
    except SmallProblem as e:
        print(e)
def part3(): #WILL RUN EVEN IF PART 2 FAILS
    print("part 3")

def part4(): #WILL RUN EVEN IF PART 2 FAILS
    print("part 4")
    
main()

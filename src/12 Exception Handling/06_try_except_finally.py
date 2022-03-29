############################################################
#
#    try-except-finally statements
#
############################################################

def f(x):
    if x > 50:
        raise Exception('exception thrown')

# RAII
# Resource Allocation is Initialization

try:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    x = 10
    f(x)
=======
    x = 100
    f(x) #can raise an exception
>>>>>>> Stashed changes
=======
    x = 100
    f(x) #can raise an exception
>>>>>>> Stashed changes
except Exception as e:
    print(f'caught exception ... {e}')
else:
    print('no exception thrown')
finally:
    print('finally block is always called ...')

print("End of program")


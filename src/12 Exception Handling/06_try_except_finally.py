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
    x = 100
    f(x) #can raise an exception
except Exception as e:
    print(f'caught exception ... {e}')
else:
    print('no exception thrown')
finally: # always run even if exception thrown
    print('finally block is always called ...')

print("End of program")


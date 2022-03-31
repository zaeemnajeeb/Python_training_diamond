############################################################
#
#    creating threads
#
############################################################

import random
import time
import sys

from threading import Thread

def myfunc(name):
    for i in range (1, 50):
        sys.stdout.write(name)        
        time.sleep(random.random() * 0.1) # this is just to make the demo more interesting
      

# define a callback function - to be called via start()
thread1 = Thread(target=myfunc, args=("1",))
thread2 = Thread(target=myfunc, args=("2",))
thread3 = Thread(target=myfunc, args=("3",))

thread1.start() #must start up thread explicitly
thread2.start()
thread3.start()

thread1.join() # wait for thread 1 to finish
thread2.join() # wait for thread 2 to finish
thread3.join() # wait for thread 3 to finish

print("\nEnd of main Thread") 




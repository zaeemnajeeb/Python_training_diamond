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
#        time.sleep(random.random() * 0.1)
      

# define a callback function - to be called via start()
#tell python how to make a thread - these are helper functions
thread1 = Thread(target=myfunc, args=("1",)) 
thread2 = Thread(target=myfunc, args=("2",))
thread3 = Thread(target=myfunc, args=("3",))
#NOW make a thread using the os system
thread1.start()#2 threads now run
thread2.start()#3 threads now run
thread3.start()#4 threads now run
#join means to wait for a thread to finish and rejoin the main thread
thread1.join()
thread2.join()
thread3.join()
#THREADS CAN START IN ANY ORDER
print("\nEnd of main Thread") #PRINT WHEN ALL THREADS END




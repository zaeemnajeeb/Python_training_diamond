import logging
import datetime
import time
import subprocess

# clear log file
subprocess.call("rm logs/example.log", shell=True)

t = time.mktime(time.localtime()) #local time is ridiculous, so must convert
t = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)) #then convert to GMT

# output added to the root logger
LOG_FILENAME = 'logs/example.log'

# set debug level
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# log some messages
logging.debug('This message goes to the log file')
logging.info(f'This message was timed at: {t}')

# inspect log file
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import os
os.system("cat logs/example.log")

subprocess.call("cat logs/example.log", shell=True)
=======
=======
>>>>>>> Stashed changes
#unix way to call
#import os
#os.system("cat logs/example.log")
subprocess.call("cat logs/example.log", shell=True) #run on bash shell (unix)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logs/rotation.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger') #creater logging object
my_logger.setLevel(logging.DEBUG) #specify level

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    #maxbytes is maximum number of bytes the file can contain
    #WHEN FULL, it create another file with .1, .2 etc
              LOG_FILENAME, maxBytes=20000, backupCount=5)

my_logger.addHandler(handler) #give the logging object the handler

# Log some messages
for i in range(10000):
    my_logger.debug(f'This is a logging message {i}')

# See what files are created
import subprocess
subprocess.call("ls -l logs/rotation*", shell=True)


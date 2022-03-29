############################################################
#
#    random access
#
############################################################
<<<<<<< Updated upstream:src/05 File IO/Binary/09_RandomAccessFiles.py

myFile = open('data/myfile2.bin', 'wb')

myFile.seek(40, 0)
=======
#NOTE you would need to state the file as binary on windows
myFile = open('data/myfile2.bin', 'wb')
#Go to byte 40 and write the string in binary
myFile.seek(40, 0)
#NOTE YOU MUST ENCODE THE STRING TO BYTES before writing
>>>>>>> Stashed changes:src/05 File IO/09_RandomAccessFiles.py
myFile.write("ABCDEFGH".encode())

myFile.seek(140, 0)
myFile.write("ABCDEFGH".encode())
<<<<<<< Updated upstream:src/05 File IO/Binary/09_RandomAccessFiles.py

=======
#Go to byte 240 and write the string in binary
>>>>>>> Stashed changes:src/05 File IO/09_RandomAccessFiles.py
myFile.seek(240, 0)
myFile.write("ABCDEFGH".encode())

myFile.seek(2560240, 0)
myFile.write("X".encode())

myFile.close()
#This is running a linux command within python
import os
os.system("hexdump data/myfile2.bin")
<<<<<<< Updated upstream:src/05 File IO/Binary/09_RandomAccessFiles.py
=======
#You may see byte swapping, leading to the letters being
#in a different order than what was written
>>>>>>> Stashed changes:src/05 File IO/09_RandomAccessFiles.py

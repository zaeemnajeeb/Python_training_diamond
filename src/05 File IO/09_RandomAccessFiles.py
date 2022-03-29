############################################################
#
#    random access
#
############################################################
#NOTE you would need to state the file as binary on windows
myFile = open('data/myfile2.bin', 'wb')
#Go to byte 40 and write the string in binary
myFile.seek(40, 0)
#NOTE YOU MUST ENCODE THE STRING TO BYTES before writing
myFile.write("ABCDEFGH".encode())

myFile.seek(140, 0)
myFile.write("ABCDEFGH".encode())
#Go to byte 240 and write the string in binary
myFile.seek(240, 0)
myFile.write("ABCDEFGH".encode())

myFile.seek(2560240, 0)
myFile.write("X".encode())

myFile.close()
#This is running a linux command within python
import os
os.system("hexdump data/myfile2.bin")
#You may see byte swapping, leading to the letters being
#in a different order than what was written
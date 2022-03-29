############################################################
#
#    Creating Groups
#
############################################################

import h5py
import numpy as np

def write(fileName):
    file = h5py.File(fileName,'w')
    group = file.create_group("MyGroup")
    subgroup = group.create_group("MySubGroup") #creates subgroup within group
    print("Writing data...")
    ds = subgroup.create_dataset("my_dset", (4, 6))
    ds[...] = np.arange(101, 125).reshape(4,6)    
    file.close()
    
def readBack(fileName): #NOTE Directories are named Groups in the file
    file = h5py.File(fileName,'r')
    subgroup = file['/MyGroup/MySubGroup'] #In subdirectory
    print("Reading data back...")
    data = subgroup['my_dset'][()]
    print(data)
    file.close()

fileName = 'data/dset.h5'
write(fileName)
readBack(fileName)

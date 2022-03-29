############################################################
#
#    Creating Attributes
#
############################################################

import h5py
import numpy as np

def write(fileName):
    file = h5py.File(fileName,'w')
    file.create_dataset("dset",(4, 6))
    dataset = file['/dset']
    dataset.attrs["Units"] = "Meters per second" #key-value pair 1
    dataset.attrs.create("Speed", np.array([100,200])) #key-value pair 1
    file.close()


def readBack(fileName):
    # read attrs back and print it
    file = h5py.File(fileName,'r')
    dataset = file['/dset']
    z = dataset.attrs.keys()
    print("Reading data back...")
    for k,v in dataset.attrs.items(): #retrieve all key-value pairs
        print(f"key={k}, value={v}")
    file.close()

fileName = 'data/dset.h5'
write(fileName)
readBack(fileName)

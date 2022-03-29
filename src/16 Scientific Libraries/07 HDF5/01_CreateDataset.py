############################################################
#
#    Creating Datasets
#
############################################################

import h5py, os
if not os.path.exists('data'): os.mkdir('data') #make in current directory

file = h5py.File('data/dset.h5','w')

dataset = file.create_dataset("dset",(4, 6))        # must specify a size
print("Dataset dataspace is", dataset.shape) #checks shape .. etc
print("Dataset Numpy datatype is", dataset.dtype)
print("Dataset name is", dataset.name)
print("Dataset is a member of the group", dataset.parent)
print("Dataset was created in the file", dataset.file)
#
# Close the file before exiting
#
file.close()

'''
The following code is a working utility code to unpack various files in a dedicated folder of choosing.

The current use-case is to reorganize OpenFOAM post-processing files as they save under different timesteps upon recovery from server.

It also has the functionality to rename post-processing files with a colon in the name, to an underscore so they can be transfered through the server to local. 
'''
import os
import shutil

destination = os.getcwd() + '/0/'

for folder, sub_folders, files in os.walk(os.getcwd()):
    count = 0
    for f in files:
        count = count+1
        fullpath = folder + '/' + f
        shutil.move(fullpath,destination+str(count)+'/'+f)

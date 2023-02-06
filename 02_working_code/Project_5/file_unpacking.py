'''
The following code is a working utility code to unpack various files in a dedicated folder of choosing.
The current use-case is to reorganize OpenFOAM post-processing files as they save under different timesteps upon recovery from server.
'''

import shutil
loc = str(input('Insert directory location: '))

with open(loc) as files:
    contents = files.read()
    print(contents)
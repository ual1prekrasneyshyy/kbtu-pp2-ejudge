import shutil
import os

WORKING_DIR = os.getcwd()

file = input(f'Choose file to delete:\n')

path = os.path.join(WORKING_DIR, file)

if not os.path.exists(path):
    print(f'File "{file}" does not exist')
else:
    if not os.access(path, os.R_OK): #remove ok
        print(f'File "{file}" can not be removed')
    else:
        os.remove(path)
        print(f'File "{file}" has successfully removed')

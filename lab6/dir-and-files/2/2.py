import os

WORKING_DIR = os.getcwd()

file_name = input('Write the name of a file to check:\n')

path = os.path.join(WORKING_DIR, file_name)

if os.path.exists(path):
    print(f'Path "{path}" exists')
else:
    print(f'Path "{path} doesn\'t" exists')

if os.path.isfile(path) and os.access(path, os.R_OK):
    print(f'Path "{path}" is readable')
else:
    print(f'Path "{path}" is not readable')

if os.path.isfile(path) and os.access(path, os.W_OK):
    print(f'Path "{path}" is writable')
else:
    print(f'Path "{path}" is now writable')

if os.access(path, os.X_OK):
    print(f'Path "{path}" is executable')
else:
    print(f'Path "{path}" is not executable')


import os

# WORKING_PATH = os.getcwd()
# path = os.path.join(WORKING_PATH, 'something.txt')

path = input('Insert some path:\n')

if os.path.exists(path):
    filename = os.path.basename(path)
    print(f'The filename is "{filename}"')
    print(f'The directory portion is "{path.strip(filename)}"')  #strip=delete
else:
    print(f'Path "{path}" does not exists')



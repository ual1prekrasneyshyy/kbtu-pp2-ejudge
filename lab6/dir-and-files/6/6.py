import os

WORKING_DIR = os.getcwd()

for i in range(65, 91):  #A-Z
    current_letter = chr(i)
    file_name = f'{current_letter}.txt'
    if os.path.exists(os.path.join(WORKING_DIR, file_name)):
        print(f'File {file_name} exists!')
    else:
        f = open(file_name, 'x')
        f.write(f'This is {current_letter}.txt file')


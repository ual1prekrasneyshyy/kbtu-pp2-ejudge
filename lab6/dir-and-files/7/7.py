import shutil

file = input('Write the file name:\n')

shutil.copy(file, f'{file}_2')

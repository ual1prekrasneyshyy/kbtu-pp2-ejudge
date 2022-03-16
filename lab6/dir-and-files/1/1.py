import os


def show_the_list_of_dirs_and_files(path, depth=0):
    for i in os.listdir(path):
        target_path = os.path.join(path, i)
        print('>>>'*depth, end='')

        if os.path.isfile(target_path):
            print(f'FILE: {i}')
        if os.path.isdir(target_path):
            print(f'DIR: {i}')
            show_the_list_of_dirs_and_files(target_path, depth+1)


WORKING_DIR = os.getcwd()
show_the_list_of_dirs_and_files(WORKING_DIR)

#! /usr/bin/python3
import pathlib
import os
import shutil
import sys
from glob import glob
import re
from colorama import Fore
from colorama import Style

DEBUG = False
DEBUG = True                                                                   # comment to toggle

# pretty print an array
def pretty_print_array(array,message,color=Fore.GREEN):
    if DEBUG : print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f'{color}'
        reset = f' : {Style.RESET_ALL}'
        if DEBUG : print(start + str(index) + reset + str(name))

def pretty_print_value(value,message,color=Fore.BLUE):
    if DEBUG : print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value))


current_path = pathlib.Path(__file__).parent.absolute()

dirs = glob(str(current_path) + '/*/')
dirs.sort()

# print(dirs)
# pretty_print_array(dirs, 'dirs')

folders_to_move = []
for dir in dirs:

    dir_name = dir.replace(str(current_path), '')
    dir_name = dir_name.replace('/', '')
    if 'videos' in dir_name:
        continue
    if 'converted' in dir_name:
        continue
    if 'files' in dir_name:
        continue

    # pretty_print_value(dir_name, 'dir_name')
    folders_to_move.append(dir)

pretty_print_array(folders_to_move, 'folders to move')

if not os.path.isdir('files'):
    os.mkdir('files')

for folder in folders_to_move:

    source = folder
    folder_name = folder.replace(str(current_path), '')
    destination = str(current_path) + '/files' + str(folder_name)
    # print(destination)

    shutil.move(source, destination)

files_folder_path = 'files'
files_zip_path = files_folder_path + '.7z'
command = 'zip -r ' + files_zip_path + ' ' + files_folder_path
os.system(command)


# found = False
# for folder in dirs:
#     folder_path = os.path.dirname(folder)
#     base_name = os.path.basename(folder_path)
#     # print(folder)
#     # print(base_name)
#     # print('\n')
#     if base_name.__contains__(sys.argv[1]):
#         # print(sys.argv[1])
#         found = True
#         new_name = base_name.replace(sys.argv[1],sys.argv[2])

#         source = folder_path
#         if DEBUG : print(f'{Fore.GREEN}from {Style.RESET_ALL}' +
#                         base_name + 
#                         f'{Fore.GREEN} to {Style.RESET_ALL}' + 
#                         new_name
#                         ) 
#         destination = os.path.dirname(folder_path) + '/' + new_name
#         shutil.move(source, destination)
#     pass













 

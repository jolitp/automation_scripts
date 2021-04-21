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

def pretty_print_array(array,message,color=Fore.GREEN):
    if DEBUG : print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f'{color}'
        reset = f' : {Style.RESET_ALL}'
        if DEBUG : print(start + str(index) + reset + str(name))

def pretty_print_value(value,message,color=Fore.BLUE):
    if DEBUG : print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value))

def have_extension(name, ext):
    is_video = False
    if name.lower().endswith(ext):
        is_video = True
    return is_video

path_to_current_directory = pathlib.Path(__file__).parent.absolute()

current_directory_name = os.path.basename(path_to_current_directory)

string_to_add = sys.argv[1]
ext = sys.argv[2]
# print(ext)

all_files_and_folders = os.listdir(path_to_current_directory)

all_files_with_extension = []
for file in all_files_and_folders:
    if have_extension(file, ext):
        all_files_with_extension.append(file)
all_files_with_extension.sort()

for file in all_files_with_extension:
    source = str(path_to_current_directory) + '/' + file
    pretty_print_value(source, "source")
    destination = str(path_to_current_directory) + '/' + string_to_add + file
    pretty_print_value(destination, "destination")
    
    shutil.move(source, destination)
    ...


# for name in files:

#     folder_path = os.path.dirname(name)
#     print(name)
#     # print(base_name)
#     # print('\n')
#     if name.__contains__(sys.argv[1]):
#         print(sys.argv[1])
#         found = True
#         new_name = name.replace(sys.argv[1],sys.argv[2])

#         source = os.path.join(root, name)
#         if DEBUG : print(f'{Fore.GREEN}from {Style.RESET_ALL}' +
#                         name + 
#                         f'{Fore.GREEN} to {Style.RESET_ALL}' + 
#                         new_name
#                         ) 
#         # destination = root + '/' + new_name
#         destination = os.path.join(root, new_name)

#         if os.path.isfile(destination):
#             destination += '(copy)'

#         if DEBUG : print(f'{Fore.GREEN}source {Style.RESET_ALL}' +
#             source + '\n'
#             f'{Fore.GREEN}destination {Style.RESET_ALL}' + 
#             destination
#             ) 
#         # shutil.move(source, destination)


 

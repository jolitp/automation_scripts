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

current_path = pathlib.Path(__file__).parent.absolute()

dirs = glob(str(current_path) + '/*/')

found = False
for folder in dirs:
    
    pass

for root, dirs, files in os.walk(".", topdown=False):
    
    
   for name in files:
        # print()

        folder_path = os.path.dirname(name)
        # base_name = os.path.basename(folder_path)
        print(name)
        # print(base_name)
        # print('\n')
        if name.__contains__(sys.argv[1]):
            print(sys.argv[1])
            found = True
            new_name = name.replace(sys.argv[1],sys.argv[2])

            source = os.path.join(root, name)
            if DEBUG : print(f'{Fore.GREEN}from {Style.RESET_ALL}' +
                            name + 
                            f'{Fore.GREEN} to {Style.RESET_ALL}' + 
                            new_name
                            ) 
            # destination = root + '/' + new_name
            destination = os.path.join(root, new_name)

            if os.path.isfile(destination):
                destination += '(copy)'

            if DEBUG : print(f'{Fore.GREEN}source {Style.RESET_ALL}' +
                source + '\n'
                f'{Fore.GREEN}destination {Style.RESET_ALL}' + 
                destination
                ) 
            shutil.move(source, destination)
#    for name in dirs:
    #   print(os.path.join(root, name))

if not found:
    if DEBUG : print(f'{Fore.RED}No matches found{Style.RESET_ALL}') 
















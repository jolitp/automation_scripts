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
    folder_path = os.path.dirname(folder)
    base_name = os.path.basename(folder_path)
    # print(folder)
    # print(base_name)
    # print('\n')
    if base_name.__contains__(sys.argv[1]):
        # print(sys.argv[1])
        found = True
        new_name = base_name.replace(sys.argv[1],sys.argv[2])

        source = folder_path
        if DEBUG : print(f'{Fore.GREEN}from {Style.RESET_ALL}' +
                        base_name + 
                        f'{Fore.GREEN} to {Style.RESET_ALL}' + 
                        new_name
                        ) 
        destination = os.path.dirname(folder_path) + '/' + new_name
        shutil.move(source, destination)
    pass


if not found:
    if DEBUG : print(f'{Fore.RED}No matches found{Style.RESET_ALL}') 
















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

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        first_character = name[0]
        if first_character == ' ':
            new_name = name[1:]
            print(new_name)
            
            source = os.path.join(root, name)
            destination = os.path.join(root, new_name)
            shutil.move(source, destination)
        # folder_path = os.path.dirname(name)
        # print(name)
        # if name.__contains__(sys.argv[1]):
        #     print(sys.argv[1])
        #     found = True
        #     new_name = name.replace(sys.argv[1],sys.argv[2])
        #     source = os.path.join(root, name)
        #     destination = os.path.join(root, new_name)
        #     if os.path.isfile(destination):
        #         destination += '(copy)'
        #     shutil.move(source, destination)

#! /usr/bin/python3

import pathlib
import os
import sys
import json
from glob import glob
import shutil
from colorama import Fore
from colorama import Style
import subprocess

DEBUG = False
DEBUG = True                                                                   # comment to toggle

current_path = pathlib.Path(__file__).parent.absolute()

dirs = glob(str(current_path) + '/*/')
dirs.sort()

# TODO show the folder name at the end of each iteration
count = 0
for dir in dirs:
    if DEBUG: print("start ----- ")
    if DEBUG : print(f'{Fore.MAGENTA}inside: {Style.RESET_ALL}' + str(dir))
    count += 1
    for i in range(len(sys.argv)):
        if sys.argv[i] == './call-command-in-subfolders.py':
            continue
        if DEBUG : print(f'{Fore.GREEN}argument number {Style.RESET_ALL}' +
                        str(1) +
                        f'{Fore.GREEN} is {Style.RESET_ALL}' +
                        str(sys.argv[i])
                        )
        os.chdir(dir)
        os.system(sys.argv[i])
    if DEBUG : print(f'{Fore.MAGENTA}PROCESSED {Style.RESET_ALL}' +
                str(count) +
                f'{Fore.MAGENTA} OF {Style.RESET_ALL}' +
                str(len(dirs))
                )
    if DEBUG: print("---- end ")
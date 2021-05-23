#! /usr/bin/python3
import shutil
import os 
from glob import glob
import pathlib
from os import listdir
from os.path import isfile, join

"""
copy all .py files to all subfolders
"""

def is_python_file(name):
    is_py = False
    if name.lower().endswith('.py'):
        is_py = True
    return is_py

current_path = pathlib.Path(__file__).parent.absolute()

dirs = os.listdir('.')

dirs = glob(str(current_path) + '/*/')
# print(dirs)

onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]
# print(onlyfiles)

files_to_copy = []
for file in onlyfiles:
    if is_python_file(file):
        files_to_copy.append(file)
        # print(file)
        
print(files_to_copy)
for file_to_copy in files_to_copy:
    src = str(current_path) + "/" + file_to_copy

    print("source:      " + src + "\n")

    for dir in dirs:
        dst = dir
        shutil.copy(src, dst)
        print("destination: " + dst)
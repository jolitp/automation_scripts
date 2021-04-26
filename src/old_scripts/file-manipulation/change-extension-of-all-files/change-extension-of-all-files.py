#! /usr/bin/python3

import pathlib
import os
import sys
import json
import shutil
from colorama import Fore
from colorama import Style
import subprocess

DEBUG = False
DEBUG = True  

path_to_current_directory = pathlib.Path(__file__).parent.absolute()

current_directory_name = os.path.basename(path_to_current_directory)

all_files_and_folders = os.listdir(path_to_current_directory)

for video in all_files_and_folders:
    source = str(path_to_current_directory) + '/' + video
    print(source)

    ext = sys.argv[1]
    # print(ext)

    video_without_ext = os.path.splitext(video)[0]
    # print(video_without_ext)

    destination = str(path_to_current_directory) + '/' + video_without_ext + '.' + ext
    print(destination)

    shutil.move(source,destination)

















 

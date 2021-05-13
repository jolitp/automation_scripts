#! /usr/bin/python3
import os
import shutil
from glob import glob
import pathlib
from colorama import Fore
from colorama import Style
import json 

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

current_path = pathlib.Path(__file__).parent.absolute()

dirs = glob(str(current_path) + '/*/')
print(f'\n{Fore.YELLOW}dirs{Style.RESET_ALL}: ' + str(dirs))
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(files)

dictionary_folders_and_files = {}
for folder in dirs:
    folder = folder[:folder.__len__() -1]
    dictionary_folders_and_files[folder] = []
    for current_file in files:
        if os.path.basename(folder) in current_file and is_video(current_file): 
            print('folder          : ' + folder)
            print('folder basename : ' + os.path.basename(folder))
            current_file_renamed = current_file.replace(os.path.basename(folder) + ' ','')
            print('current file    : ' + current_file)
            dictionary_folders_and_files[folder].append(folder + '/' + current_file)
            
            source = str(current_path) + '/' + current_file
            print(f'\n{Fore.CYAN}source{Style.RESET_ALL}: ' + str(source))
            destination = folder + '/' + current_file_renamed
            print(f'\n{Fore.CYAN}destination{Style.RESET_ALL}: ' + str(destination))

            shutil.move(source,destination)
        pass
    pass
    
json_object = json.dumps(dictionary_folders_and_files, indent=2)
print(json_object)
#! /usr/bin/python3.8

import pathlib
import os
# import sys
import json
# import shutil
import subprocess
from colorama import Fore
from colorama import Style

DEBUG = False
DEBUG = True  

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi',
                    '.webm', '.flv', '.mov', '.wmv', '.vob', '.ogm']

def is_video(name):
    """
    stop bugging me
    """
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

def add_to_histogram(key, histogram):
    """
    stop bugging me
    """
    if key in histogram:
        histogram[key] = int(histogram[key]) + 1
    else: 
        histogram[key] = 1

def remove_undesired_characters(path):
    """
    stop bugging me
    """
    new:str = str(path).replace('\'', "")
    new = new.replace('\"', "")
    new = new.replace('(', '')
    new = new.replace(')', '')
    new = new.replace('~', '')
    new = new.replace('`', '')
    new = new.replace('#', '')
    new = new.replace('@', '')
    new = new.replace('!', '')
    new = new.replace('$', '')
    new = new.replace('%', '')
    new = new.replace('^', '')
    new = new.replace('&', '')
    new = new.replace('*', '')
    new = new.replace('[', '')
    new = new.replace(']', '')
    new = new.replace('{', '')
    new = new.replace('}', '')
    new = new.replace(';', '')
    new = new.replace('<', '')
    new = new.replace('>', '')
    new = new.replace('?', '')
    new = new.replace(',', '')
    return new

path_to_current_directory = pathlib.Path(__file__).parent.absolute()
current_directory_name = os.path.basename(path_to_current_directory)

histogram_video_width = {}
histogram_video_height = {}

all_files_and_folders_in_videos_folder = os.listdir('.')

all_videos_in_videos_folder = []
for file in all_files_and_folders_in_videos_folder:
    if is_video(file):
        all_videos_in_videos_folder.append(file)
all_videos_in_videos_folder.sort()

csv = ''
csv += 'video name' + ',' + 'video_width' + ',' + 'video_height' + '\n'
for video in all_videos_in_videos_folder:
    if video == str(current_directory_name + ".mp4"):
        concatenated_video_found = True
        continue
    print(video)
    result = subprocess.run(["mediainfo",'--Inform=\"Video;%Height%\" ', '--Output=JSON', video],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    parsed = json.loads(result.stdout)
    video_category = parsed["media"]["track"][1]
    video_width = video_category["Width"]
    add_to_histogram(video_width, histogram_video_width)
    video_height = video_category["Height"]
    add_to_histogram(video_height, histogram_video_height)
    video = remove_undesired_characters(video)

    csv += video + ',' + video_width + ',' + video_height + '\n'

print(csv)

file = open('dimension.csv','w+')
file.write(csv)
file.close()

def make_different_dimensions_file():
    """
    stop bugging me
    """
    new_file = open('different_dimentions.txt', 'w+')
    new_file.close()

if not (len(histogram_video_height) == 1 or len(histogram_video_width) != 1):
    print(f'{Fore.RED}videos have different dimensions{Style.RESET_ALL}')
    make_different_dimensions_file()

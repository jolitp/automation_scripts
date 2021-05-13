#! /usr/bin/python3.8

import cv2
import pathlib
import os
import sys
import re
import json
import shutil
from colorama import Fore
from colorama import Style
import subprocess
import collections

DEBUG = False
DEBUG = True  

RELEASE = False
RELEASE = True                                                  # deactivate to test

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob', '.ogm' , '.mpg', '.rmvb']

# pretty print an array
def pretty_print_array(array,message,color=Fore.GREEN):
    if DEBUG : print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f'{color}'
        reset = f' : {Style.RESET_ALL}'
        if DEBUG : print(start + str(index) + reset + str(name))

def pretty_print_value(value,message,color=Fore.BLUE):
    if DEBUG : print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value))


def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video


def add_to_histogram(key, histogram):
    if key in histogram:
        histogram[key] = int(histogram[key]) + 1
    else: 
        histogram[key] = 1


def make_different_dimensions_file():
    f = open('different_dimentions.txt', 'w+')
    f.close()


def remove_undesired_characters(path):
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
    return new



def make_video_list_file(all_videos):
    f = open('vidlist.txt', 'w+')
    f.close()
    
    for video in all_videos:
        f = open('vidlist.txt', 'a')
        print(video)
        # video = os.path.splitext(video)
        f.write(f"file \'{str(path_to_current_directory) + '/videos/' + str(video)}\'\n")
    return 'vidlist.txt'


path_to_current_directory = pathlib.Path(__file__).parent.absolute()
pretty_print_value(path_to_current_directory, 'path_to_current_directory')

all_files_and_folders = os.listdir(path_to_current_directory)
pretty_print_value(all_files_and_folders, 'all_files_and_folders')

all_videos = []
for file in all_files_and_folders:
    if is_video(file):
        all_videos.append(file)
all_videos.sort()

pretty_print_array(all_videos, "all_videos")

current_directory_name = os.path.basename(path_to_current_directory)
pretty_print_value(path_to_current_directory, 'path_to_current_directory')


histogram_video_width = {}
histogram_video_height = {}


videos_folder_path = str(path_to_current_directory) + '/videos/'
has_videos_folder = os.path.isdir(videos_folder_path)
# print(isDirectory)

if not has_videos_folder:
    os.mkdir(videos_folder_path)

# move videos to videos folder
for video in all_videos:
    if video == str(current_directory_name + ".mp4"):
        print(f'{Fore.RED}concatenated video found{Style.RESET_ALL}: ' + str(video)) 
        concatenated_video_found = True
        continue
    print(f'{Fore.CYAN}video      {Style.RESET_ALL}: ' + str(video)) 
    source = str(path_to_current_directory) + '/' + str(video)
    print(f'{Fore.YELLOW}source     {Style.RESET_ALL}: ' + str(source)) 

    destination =  str(path_to_current_directory) + '/videos/' + str(video)
    print(f'{Fore.YELLOW}destination{Style.RESET_ALL}: ' + str(destination)) 
    shutil.move(source, destination)                                                   # deactivate to test

all_files_and_folders_in_videos_folder = os.listdir('./videos/')

# get all videos in videos folder
all_videos_in_videos_folder = []
for file in all_files_and_folders_in_videos_folder:
    if is_video(file):
        if file == str(current_directory_name + ".mp4"):
            concatenated_video_found = True
            continue
        old_path_to_file = str(path_to_current_directory) + '/videos/' + file
        file = remove_undesired_characters(file)
        new_path_to_file = str(path_to_current_directory) + '/videos/' + file
        shutil.move(old_path_to_file, new_path_to_file)
        print('file ' + file)
        # remove_undesired_characters(file)
        all_videos_in_videos_folder.append(file)
    pass
all_videos_in_videos_folder.sort()
# print(all_videos_in_videos_folder)

width_and_height_occurrences = []

# check wether or not the videos have the same dimentions and save on the 'histograms'
for video in all_videos_in_videos_folder:
    if video == str(current_directory_name + ".mp4"):
        concatenated_video_found = True
        continue
    path_to_video = videos_folder_path + '/' + video
    # print(path_to_video)
    pretty_print_value(str(video), "getting info for: ")
    result = subprocess.run(["mediainfo",'--Inform=\"Video;%Height%\" ', '--Output=JSON', path_to_video], 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    parsed = json.loads(result.stdout)
    video_category = parsed["media"]["track"][1]
    video_width = video_category["Width"]
    add_to_histogram(video_width, histogram_video_width)
    video_height = video_category["Height"]
    add_to_histogram(video_height, histogram_video_height)

    width_and_height_occurrences.append(str(video_width) + ':' +  str(video_height))

pretty_print_array(width_and_height_occurrences, "width_and_height_occurrences", Fore.YELLOW)


if not (len(histogram_video_height) == 1 and len(histogram_video_width) == 1):
    print(f'{Fore.RED}videos have different dimentions{Style.RESET_ALL}')
    make_different_dimensions_file()
    sys.exit()

output_video = str(path_to_current_directory) + '.mp4'
pretty_print_value(output_video,"output_video")


concatenated_folder_path = str(path_to_current_directory) + '/concatenated/'
has_concatenated_folder = os.path.isdir(concatenated_folder_path)

if not has_concatenated_folder:
    os.mkdir(concatenated_folder_path)

output_video = str(path_to_current_directory) + '/concatenated/' + str(current_directory_name) + '.mp4'
pretty_print_value(output_video,"output_video")

video_list_file = str(path_to_current_directory) + '/' + make_video_list_file(all_videos_in_videos_folder)
ffmpeg_command = 'ffmpeg -f concat -safe 0 -i \'' + video_list_file + '\' -c copy \'' + output_video + '\''
if DEBUG : print(f'{Fore.BLUE}ffmpeg command{Style.RESET_ALL}: ' + ffmpeg_command) 

if RELEASE: os.system(ffmpeg_command)                                                      # deactivate to test

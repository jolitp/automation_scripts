#! /usr/bin/python3.8

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

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video


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

concatenated_video_found = False

path_to_current_directory = pathlib.Path(__file__).parent.absolute()

current_directory_name = os.path.basename(path_to_current_directory)

source = path_to_current_directory
destination = remove_undesired_characters(source)

if source != destination:
    shutil.move(source, destination)
    path_to_current_directory = destination
print("Path current dir: " + path_to_current_directory)
all_files_and_folders = os.listdir(path_to_current_directory)

all_videos = []
for file in all_files_and_folders:
    if is_video(file):
        all_videos.append(file)
    pass
all_videos.sort()

histogram_video_width = {}
histogram_video_height = {}

videos_folder_path = str(path_to_current_directory) + '/videos/'
has_videos_folder = os.path.isdir(videos_folder_path)
# print(isDirectory)

if not has_videos_folder:
    os.mkdir(videos_folder_path)

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

all_videos_in_videos_folder = []
for file in all_files_and_folders_in_videos_folder:
    if is_video(file):
        if file == str(current_directory_name + ".mp4"):
            concatenated_video_found = True
            continue
        old_path_to_file = path_to_current_directory + '/videos/' + file
        file = remove_undesired_characters(file)
        new_path_to_file = path_to_current_directory + '/videos/' + file
        shutil.move(old_path_to_file, new_path_to_file)
        print('file ' + file)
        # remove_undesired_characters(file)
        all_videos_in_videos_folder.append(file)
    pass
all_videos_in_videos_folder.sort()
# print(all_videos_in_videos_folder)


def add_to_histogram(key, histogram):
    if key in histogram:
        histogram[key] = int(histogram[key]) + 1
    else: 
        histogram[key] = 1


for video in all_videos_in_videos_folder:
    if video == str(current_directory_name + ".mp4"):
        concatenated_video_found = True
        continue
    path_to_video = videos_folder_path + '/' + video
    # print(path_to_video)
    result = subprocess.run(["mediainfo",'--Inform=\"Video;%Height%\" ', '--Output=JSON', path_to_video], 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    parsed = json.loads(result.stdout)
    video_category = parsed["media"]["track"][1]
    video_width = video_category["Width"]
    add_to_histogram(video_width, histogram_video_width)
    video_height = video_category["Height"]
    add_to_histogram(video_height, histogram_video_height)

    # print(histogram_video_width)
    # print(histogram_video_height)

path_to_converted_directory = str(path_to_current_directory) + '/converted/'

if not os.path.isdir(path_to_converted_directory):
    os.mkdir(path_to_converted_directory)

def make_different_dimensions_file():
    f = open('different_dimentions.txt', 'w+')
    f.close()


for video in all_videos_in_videos_folder:
    output_video = path_to_converted_directory + '/' + video

    if os.path.isfile(output_video):
        continue

    path_to_video_in_videos_folder = str(path_to_current_directory) + '/videos/' + video
    print(f'{Fore.GREEN}video : {Style.RESET_ALL}' + str(path_to_video_in_videos_folder))
    command = f'ffmpeg -i \"{path_to_video_in_videos_folder}\" -r 30 -c:v libx264 -pix_fmt yuv420p -crf 17 -c:a aac -b:a 128k \"{output_video}\"'
    print(f'{Fore.GREEN}command : {Style.RESET_ALL}' + command)
    os.system(command)                                                       # comment to test 

if not (len(histogram_video_height) == 1 and len(histogram_video_width) == 1):
    print(f'{Fore.RED}videos have different dimensions{Style.RESET_ALL}')
    make_different_dimensions_file()
    sys.exit()

def make_video_list_file(all_videos):
    f = open('vidlist.txt', 'w+')
    f.close()
    
    for video in all_videos:
        f = open('vidlist.txt', 'a')
        f.write(f"file \'{path_to_converted_directory + video}\'\n")
    return 'vidlist.txt'

# if DEBUG : print(f'{Fore.GREEN}videos in video folder{Style.RESET_ALL}')

# for video in all_videos_in_videos_folder:
#     if DEBUG : print(f'{Fore.YELLOW}video {Style.RESET_ALL}: ' + str(video)) 

# output_video = str(path_to_current_directory) + '.mp4'


# output_video = path_to_current_directory + '/' + current_directory_name + '.mp4'
# if os.path.isfile(str(path_to_current_directory) + '/' + output_video):
#     print(f'{Fore.RED}output video already exists{Style.RESET_ALL}')
#     sys.exit()
#     pass

# if concatenated_video_found:
#     if DEBUG : print(f'{Fore.MAGENTA}concatenated video found{Style.RESET_ALL}') 
#     sys.exit()

# video_list_file = path_to_current_directory + '/' + make_video_list_file(all_videos_in_videos_folder)
# ffmpeg_command = 'ffmpeg -f concat -safe 0 -i \'' + video_list_file + '\' -c copy \'' + output_video + '\''
# if DEBUG : print(f'{Fore.GREEN}ffmpeg command{Style.RESET_ALL}: ' + ffmpeg_command) 

# os.system(ffmpeg_command)                                                      # deactivate to test






























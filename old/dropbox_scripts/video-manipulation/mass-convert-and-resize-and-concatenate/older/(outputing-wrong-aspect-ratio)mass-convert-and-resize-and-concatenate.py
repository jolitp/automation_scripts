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

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob', '.ogm' , '.mpg']


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


# def make_different_dimensions_file():
#     f = open('different_dimentions.txt', 'w+')
#     f.close()


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
# print("Path current dir: " + path_to_current_directory)
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


# move videos to videos folder
for video in all_videos:
    if video == str(current_directory_name + ".mp4"):
        # print(f'{Fore.RED}concatenated video found{Style.RESET_ALL}: ' + str(video)) 
        concatenated_video_found = True
        continue
    # print(f'{Fore.CYAN}video      {Style.RESET_ALL}: ' + str(video)) 
    source = str(path_to_current_directory) + '/' + str(video)
    # print(f'{Fore.YELLOW}source     {Style.RESET_ALL}: ' + str(source)) 

    destination =  str(path_to_current_directory) + '/videos/' + str(video)
    # print(f'{Fore.YELLOW}destination{Style.RESET_ALL}: ' + str(destination)) 
    if RELEASE:
        shutil.move(source, destination) 

all_files_and_folders_in_videos_folder = os.listdir('./videos/')

# get all videos in videos folder
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
        # print('file ' + file)
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
    pretty_print_value(str(video), 'getting info for: ')

    vid = cv2.VideoCapture(path_to_video)
    
    video_width = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_height = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    add_to_histogram(video_width, histogram_video_width)
    add_to_histogram(video_height, histogram_video_height)

    width_and_height_occurrences.append(str(video_width) + ':' +  str(video_height))


# USING MEDIAINFO
    # result = subprocess.run(["mediainfo ",'--Inform=\"Video;%Height%\" ', '--Output=JSON', path_to_video], 
    #                         stdout=subprocess.PIPE,
    #                         stderr=subprocess.STDOUT)
    # parsed = json.loads(result.stdout)
    # video_category = parsed["media"]["track"][1]
    # video_width = video_category["Width"]
    # add_to_histogram(video_width, histogram_video_width)
    # video_height = video_category["Height"]
    # add_to_histogram(video_height, histogram_video_height)


# USING OPENCV
    # import cv2
    # file_path = "./video.avi"  # change to your own video path
    # vid = cv2.VideoCapture(file_path)
    # height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

    # width_and_height_occurrences.append(str(video_width) + ':' +  str(video_height))

# pretty_print_array(width_and_height_occurrences, "width_and_height_occurrences ", Fore.YELLOW)

# get the most common dimensions
width_and_height_count = {}
for element in width_and_height_occurrences:
    if element in width_and_height_count:
        width_and_height_count[element] += 1
    else:
        width_and_height_count[element] = 1

width_and_height_count_array = []
for key, value in width_and_height_count.items():
    temp = [value,key]
    width_and_height_count_array.append(temp)

# pretty_print_array(width_and_height_count, "width_and_height_count ", Fore.YELLOW)

pretty_print_value(width_and_height_count, "width_and_height_count")

# pretty_print_array(width_and_height_count_array, "width_and_height_count_array ", Fore.YELLOW)

most_common_width_and_height = width_and_height_count_array[len(width_and_height_count_array) -1]
most_common_width_and_height_index = 0
highest_occurency = 0
for index, element in enumerate(width_and_height_count_array):
    print(element)
    print(index)
    number_of_occurencies_in_element = element[0]
    if index == 0:
        highest_occurency = number_of_occurencies_in_element
        continue
    else:
        if number_of_occurencies_in_element > highest_occurency:
            highest_occurency = number_of_occurencies_in_element
            most_common_width_and_height_index = index

most_common_width_and_height = width_and_height_count_array[most_common_width_and_height_index]
# pretty_print_value(most_common_width_and_height, "most_common_width_and_height")

most_common_width_and_height = re.findall('\'([^"]*)\'', str(most_common_width_and_height))
most_common_width_and_height : str = most_common_width_and_height[0]
most_common_width_and_height = most_common_width_and_height.replace('\'','')


pretty_print_value(most_common_width_and_height, "most_common_width_and_height")
# print(type(most_common_width_and_height))


path_to_converted_directory = str(path_to_current_directory) + '/converted/'

if not os.path.isdir(path_to_converted_directory):
    os.mkdir(path_to_converted_directory)

def color_relevant_directories(file_path : str, color=Fore.LIGHTCYAN_EX):
    path_separated = []
    path_separated = file_path.split('/')
    # print(path_separated)

    faint_color = Fore.CYAN
    path_colored = ""
    for index, folder in enumerate(path_separated):
        if current_directory_name in folder or index == len(path_separated) -1:
            path_colored += f'{color}'
        else:
            path_colored += f'{faint_color}'
        path_colored += folder
        path_colored += f'{Style.RESET_ALL}'
        path_colored += f'/'
        ...
    ...
    return path_colored

# convert the videos
for video in all_videos_in_videos_folder:
    output_video = path_to_converted_directory + '/' + video
    output_video = output_video.replace('//' , '/')

    if os.path.isfile(output_video):
        pretty_print_value(output_video, 'converted video found, skipping video.',Fore.LIGHTRED_EX)
        continue
    output_video = os.path.splitext(output_video)[0] + '.mp4'
    path_to_video_in_videos_folder = str(path_to_current_directory) + '/videos/' + video
    # print(f'{Fore.GREEN}video : {Style.RESET_ALL}' + str(path_to_video_in_videos_folder))
    
    # flags = f' {Fore.GREEN} -r {Fore.CYAN} 30 {Fore.GREEN} -c:v {Fore.CYAN} libx264 {Fore.CYAN} -pix_fmt {Fore.CYAN} yuv420p {Fore.GREEN} -crf {Fore.CYAN} 17 {Fore.GREEN} -c:a {Fore.CYAN} aac {Fore.GREEN} -b:a {Fore.CYAN} 128k {Fore.GREEN} -movflags {Fore.GREEN} +faststart  {Fore.GREEN} -vf {Fore.CYAN} scale={most_common_width_and_height} '
    
    flags = f' -r 30 -c:v libx264 -pix_fmt yuv420p -crf 17 -c:a  aac -b:a 128k  -movflags +faststart -vf scale={most_common_width_and_height} '
    
    # print(color_relevant_directories(output_video))

    # command = f'{Fore.YELLOW}ffmpeg {Fore.GREEN} -i {Style.RESET_ALL}\"{color_relevant_directories(path_to_video_in_videos_folder)}\" {flags} {Style.RESET_ALL} \"{color_relevant_directories(output_video)}\"'
    command = f'ffmpeg -i \"{path_to_video_in_videos_folder}\" {flags} \"{output_video}\"'
    print()
    print(f'{Fore.CYAN}command : {Style.RESET_ALL}' + command)
    print()
    if RELEASE: os.system(command)                                                       # comment to test 

# if not (len(histogram_video_height) == 1 and len(histogram_video_width) == 1):
#     print(f'{Fore.RED}videos have different dimentions{Style.RESET_ALL}')
#     make_different_dimensions_file()
#     # sys.exit()

def make_video_list_file(all_videos):
    f = open('vidlist.txt', 'w+')
    f.close()
    
    for video in all_videos:
        f = open('vidlist.txt', 'a')
        video = os.path.splitext(video)[0] + '.mp4'
        f.write(f"file \'{path_to_converted_directory + video}\'\n")
    return 'vidlist.txt'


# concatenate videos

# if DEBUG : print(f'{Fore.GREEN}videos in video folder{Style.RESET_ALL}')

# for video in all_videos_in_videos_folder:
#     if DEBUG : print(f'{Fore.YELLOW}video {Style.RESET_ALL}: ' + str(video)) 

output_video = str(path_to_current_directory) + '.mp4'
pretty_print_value(output_video,"output_video")

output_video = path_to_current_directory + '/' + current_directory_name + '.mp4'
if os.path.isfile(str(path_to_current_directory) + '/' + output_video):
    print(f'{Fore.RED}output video already exists{Style.RESET_ALL}')
    sys.exit()
    pass

if concatenated_video_found:
    if DEBUG : print(f'{Fore.MAGENTA}concatenated video found{Style.RESET_ALL}') 
    sys.exit()

video_list_file = path_to_current_directory + '/' + make_video_list_file(all_videos_in_videos_folder)
ffmpeg_command = 'ffmpeg -f concat -safe 0 -i \'' + video_list_file + '\' -c copy \'' + output_video + '\''
if DEBUG : print(f'{Fore.BLUE}ffmpeg command{Style.RESET_ALL}: ' + ffmpeg_command) 

if RELEASE: os.system(ffmpeg_command)                                                      # deactivate to test

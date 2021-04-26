#! /usr/bin/python3
import subprocess
import pathlib
import os
import shutil
from moviepy.editor import VideoFileClip
import datetime
from colorama import Fore
from colorama import Style

DEBUG = False
DEBUG = True  

"""
get all the videos in the directory and create files that contain the total length of them
"""
def get_length(filename):
    # print(filename)
    # result = subprocess.run(["ffprobe ", "-v ", "error ", "-show_entries ",
    #                         "format=duration ", "-of ",
    #                         "default=noprint_wrappers=1:nokey=1 ", filename],
    stream = os.popen(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{filename}"')
        # stdout=subprocess.PIPE,
        # stderr=subprocess.STDOUT)
    # final_result = str(result.stdout)
    result = stream.read()
    # if 'Header missing' in final_result:
    #     result.strout = b'0.0\n'
    #     final_result = '0.0\n'
    return float(result)

video_extensions = ['.mp4', '.m4v', '.f4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob', '.rmvb']

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

DEBUT_FROM_SECONDS_TO_TIME = False
# TODO convert days into hours
def from_seconds_to_time(sec):
    time_in_string : str = str(datetime.timedelta(seconds=sec))
    if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(time_in_string, "from_seconds_to_time / time_in_string ")
    if 'day' in time_in_string:
        days = time_in_string.split(',')[0]
        days = int(days.split(' ')[0])
        if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(days , 'from_seconds_to_time / days',Fore.LIGHTBLUE_EX)

        rest = time_in_string.split(',')[1]
        if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(rest , 'from_seconds_to_time / rest',Fore.LIGHTBLUE_EX)

        hours = int(rest.split(':')[0])
        hours = hours + days * 24
        if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(hours , 'from_seconds_to_time / hours',Fore.LIGHTBLUE_EX)

        minutes = rest.split(':')[1]
        if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(minutes , 'from_seconds_to_time / minutes',Fore.LIGHTBLUE_EX)

        seconds = rest.split(':')[2]
        seconds = seconds.split('.')[0]
        if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(seconds , 'from_seconds_to_time / seconds',Fore.LIGHTBLUE_EX)

        miliseconds = rest.split(':')[2]
        try:
            miliseconds = miliseconds.split('.')[1]
        except:
            miliseconds = 0
        if DEBUT_FROM_SECONDS_TO_TIME: pretty_print_value(miliseconds , 'from_seconds_to_time / miliseconds',Fore.LIGHTBLUE_EX)

        time_in_string = str(hours) + ':' + minutes + ':' + seconds + "."

    return time_in_string

current_path = pathlib.Path(__file__).parent.absolute()

all_files_and_folders = os.listdir('.')
# print(all_files_and_folders)

all_videos = []
for file in all_files_and_folders:
    if is_video(file):
        all_videos.append(file)
    pass
all_videos.sort()
# print(all_videos)

# change names of all videos to names without special characters
for index, video in enumerate(all_videos):
    new_name = remove_undesired_characters(video)
    # pretty_print_value(new_name, "new_name")

    source = video
    pretty_print_value(source, "source")
    destination = new_name
    pretty_print_value(destination, "destination")
    shutil.move(str(source), str(destination))

    all_videos[index] = new_name


accumulated_time_file = open("accumulated_time_of_videos.txt" , "w+")
time_file = open("time_of_videos.txt" , "w+")

accumulated_time = 0
for video in all_videos:
    pretty_print_value(video , "getting length for")
    length = get_length(video)
    # print('video : ' + str(video) + '\nlength : ' + str(length) + '\n')
    pretty_print_value(str(video), 'video : ',color=Fore.GREEN)
    pretty_print_value(str(length), 'Length : ',color=Fore.LIGHTGREEN_EX)

    time_formated = from_seconds_to_time(length)
    accumulated_time += length
    accumulated_time_formatted = from_seconds_to_time(accumulated_time)
    
    accumulated_time_file.write(video + " : " + str(accumulated_time_formatted) + "\n")
    time_file.write(video + " : " + str(time_formated) + "\n")

    formated = from_seconds_to_time(length)
    # print(video + '   ' + str(formated))
    pretty_print_value(str(formated), 'Formated : ',color=Fore.YELLOW)

accumulated_time_file.close()
time_file.close()

new_file = str(current_path) + "/" + "          " + str(from_seconds_to_time(accumulated_time))
f = open(new_file, "w+")
f.close()

src = current_path
total_length = str(from_seconds_to_time( accumulated_time))
file_with_length = str(current_path) + "/" + "mark-video-length-finished.data"

f = open(file_with_length, "w+")
f.write(total_length)
f.close()

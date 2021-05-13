#! /usr/bin/python3

import subprocess
import pathlib
import os
import sys
import json
import shutil
from colorama import Fore
from colorama import Style

DEBUG = False
DEBUG = True                                                                   # comment to toggle
# if DEBUG : print(f'{Fore.MAGENTA}message {Style.RESET_ALL}' + str(name))

# pretty print an array
def pretty_print_array(array,message,color=Fore.GREEN):
    if DEBUG : print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f'{color}'
        reset = f' : {Style.RESET_ALL}'
        if DEBUG : print(start + str(index) + reset + str(name))

def pretty_print_value(value,message,color=Fore.BLUE):
    if DEBUG : print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value))

video_extensions = \
    ['.mp4",', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def separate(name : str):
    start_of_name : str = ''
    check_for_numbers = False
    for letter in name:
        if start_of_name == '' and letter.isdigit():
            check_for_numbers = True

        elif start_of_name == '' and not letter.isdigit():
            check_for_numbers = False

        if check_for_numbers:
            if letter.isdigit():
                start_of_name += letter
            else:
                break
        else:
            if not letter.isdigit():
                start_of_name += letter
            else:
                break

    return (start_of_name,name.replace(start_of_name,'',1))

def has_only_0(name):
    non_zero_found = False
    for letter in name:
        if not '0' in letter:
            non_zero_found = True
    if non_zero_found:
        return False
    else:
        return True

def pad_zeros(list_of_names : []):
    list_of_names_sorted = sorted(list_of_names,key=len)
    list_of_names_sorted.reverse()
    biggest_length = len(list_of_names_sorted[0])

    for index , name in enumerate( list_of_names):
        if not name.isdigit():
            continue
        name_with_padded_zeros = name.zfill(biggest_length)
        if has_only_0(name_with_padded_zeros):
            name_with_padded_zeros = name
        list_of_names[index] = name_with_padded_zeros
    return list_of_names

def biggest_length_in_array(array):
    biggest_length = 0
    for name in array:
        length_of_name = len(name)

        if length_of_name > biggest_length:
            biggest_length = length_of_name
    return biggest_length


# TODO add numbers to the start of names without numbers
def main():

    pass

# get the path to current directory
path_to_current_directory = os.getcwd()
# get all the "s and folders of current directory
all_files_and_folders = os.listdir('.')

# check every " and separate all videos
all_videos = []
for filename in all_files_and_folders:
    if is_video(filename):
        all_videos.append(filename)
all_videos.sort()

# get the size of the name of every video
all_videos_name_size = []
for video in all_videos:
    name_without_extension = os.path.splitext(video)[0]
    length_of_video_name = len(name_without_extension)
    all_videos_name_size.append(length_of_video_name)

# sort and reverse, then get the first element which will be the biggest name in the list
all_videos_name_size.sort()
all_videos_name_size_reversed = list(reversed(all_videos_name_size))
if len(all_videos_name_size_reversed) == 0:
    print("no video found")
    sys.exit()
biggest_size = all_videos_name_size_reversed[0]

# array of tuples
names_separated = []
for index in range(len(all_videos_name_size)):
    # get a variable with strong typing to aid with autocompletion
    svideo:str = all_videos[index]

    # get the name of the " without the extension
    name_without_extension = os.path.splitext(svideo)[0]
    # prepare for the loop by creating a tuple
    # the first element starts empty and the second is the entire name
    result = ( '',name_without_extension)

    name_separated = []
    while not result[1] == '':
        result = separate(result[1])
        name_separated.append(result[0])
    names_separated.append(name_separated)

# get the biggest array length
biggest_length = biggest_length_in_array(names_separated)

# append '' strings to the array so all of them have the same length
for name in names_separated:
    for index in range(biggest_length):
        if index >= len(name):
            name.append('')

reversed_array = []

# each 'level' is a part of the name separated by the change in numbers or 'letters'
# or not number characters

for level in range(biggest_length):

    new_array = []
    for name in names_separated:
        new_array.append(name[level])

    # pad the numbers of every member of the array with zeros
    # add enough zeros to get to the length of the biggest member/number
    result = pad_zeros(new_array)
    reversed_array.append(result)

names_padded = []
biggest_length = biggest_length_in_array(reversed_array)
for level in range(biggest_length):

    name_zero_padded = ''
    for index,value in enumerate(reversed_array):
        cell = reversed_array[index][level]
        name_zero_padded += cell
    names_padded.append(name_zero_padded)

original_names = []
for index,value in enumerate(names_separated):
    original_name = ''
    for name in value:
        original_name += name
    original_names.append(original_name)

extensions = []
# pretty_print_array(all_videos, 'all videos ')
# pretty_print_array(original_names, 'original name ')
for video in all_videos:
    # pretty_print_value(name in video, 'name in video ',Fore.RED)
    # pretty_print_value(name, 'name ',Fore.GREEN)
    # pretty_print_value(video, 'video ')
    ext = os.path.splitext(video)[1]
    extensions.append(ext)

# pretty_print_array(extensions,'extensions')

padded_names_with_ext = []
for index,name in enumerate(names_padded):
    new_name = name + extensions[index]
    padded_names_with_ext.append(new_name)

for index,name in enumerate(padded_names_with_ext):
    source = str(path_to_current_directory) + '/' + str(all_videos[index])
    pretty_print_value(source, 'source',Fore.YELLOW)
    destination = str(path_to_current_directory) + '/' + str(padded_names_with_ext[index])
    pretty_print_value(destination, 'source',Fore.CYAN)

    shutil.move(source,destination)                                  # comment to test

# BUG if there is a name without numbers the program pad the initial zeros with the length of the name

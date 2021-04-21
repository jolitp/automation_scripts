#! /usr/bin/python3
import os
from os import path
import shutil
from colorama import Fore
from colorama import Style

DEBUG = False
DEBUG = True  

RELEASE = False
RELEASE = True

undesirable_files = [ "video-renamer-and-mover.py",
                    "remove-videos",
                    "show-width-and-height-of-videos.py",
                    "mass-convert-and-resize-and-concatenate.py",
                    "mark-video-length.py",
                    "make-org.py",
                    "check-if-ffmpeg-is-finished.py"
                    "mark-if-ffmpeg-is-finished.py",
                    "add-padding-zeros.py",
                    "clean-up-undesirable-files.py",
                    "rename-folders.py",
                    "rename-files.py",
                    "mark-if-ffmpeg-is-finished",
                    "check-if-ffmpeg-is-finished",
                    "remove-empty-folders.py",
                    "copy-py-files-to-subdirs.py",
                    "call-command-in-subfolders.py",
                    "[CourseClub.NET].url",
                    "[FreeCourseSite.com].url",
                    "[FCS Forum].url",
                    "concatenated_video_found.txt",
                    "vidlist.txt",
                    "total_length.data",
                    "accumulated_time_of_videos.txt",
                    "different_dimentions.txt",
                    "dimension.csv",
                    "mass-convert-only.py",
                    "clean-up-py-files.py",
                    ".srt",
                    ".vtt",
                    "remove-videos.py"
]

def is_undesirable_file(name:str):
    is_undesirable_file = False
    for file_name in undesirable_files:
        if file_name in name:
            is_undesirable_file = True
    return is_undesirable_file

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

# pretty print an array
def pretty_print_array(array,message,color=Fore.GREEN):
    if DEBUG : print(f'{color}========== ' + message + f' ========== {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f'{color}'
        reset = f' : {Style.RESET_ALL}'
        if DEBUG : print(start + str(index) + reset + str(name))
    print()

def pretty_print_value(value,message,color=Fore.BLUE):
    if DEBUG : print(f'{color}' + message + f' : {Style.RESET_ALL}' + str(value))


current_dir_path = os.getcwd()
current_dir = os.path.basename(current_dir_path)

# print(current_dir)

all_files_full_path = []

for root, directories, filenames in os.walk(current_dir_path):
  for filename in filenames: 
    all_files_full_path.append(os.path.join(root,filename))

all_undesirable_files = []
for file_path in all_files_full_path:
  if is_undesirable_file(file_path):
    all_undesirable_files.append(file_path)

this_file_path = os.path.realpath(__file__)



# pretty_print_array(all_files_full_path, "all files")

for file in all_undesirable_files:
    path_separated = file.split('/')
    current_path = ''
    for index, subdir in enumerate(path_separated):
        current_path += subdir + '/'
        # print(current_path)

        if index == len(path_separated) -1:
            break
        if subdir == 'undesirable_files':
            pretty_print_value(subdir, "subdir:")
        if 'undesirable_files' in current_path:

# BUG if you have undesirable files inside the undesirable_files folder and inside a nested folder
# the file will be included in the all_undesirable_files array and trigger a exception on the remove method
            all_files_full_path.remove(file)
            pretty_print_value(file, "file: ")

# pretty_print_array(all_files_full_path, "all files")


for file in all_undesirable_files:

# ignore files in the root directory
    file_in_root = False
    for elem in undesirable_files: 
        root_file = current_dir_path + '/' + elem
        if file == root_file:
            file_in_root = True

    if file_in_root:
        continue
    # print(file)

    source = file
    # pretty_print_value(source,"source: ")
    destination = str(file).replace(current_dir_path , '')
    undesirable_files_path = current_dir_path + '/undesirable_files'
    
    if not os.path.exists(undesirable_files_path):
        os.mkdir(undesirable_files_path)
    
    destination = undesirable_files_path + destination
    # pretty_print_value(destination,"destination: ")

    path_separated = destination.split('/')
    current_path = ''
    for index, subdir in enumerate(path_separated):
        current_path += subdir + '/'
        # print(current_path)

        if index == len(path_separated) -1:
            break
        # print(os.path.exists(current_path))
        if not os.path.exists(current_path):
            os.mkdir(current_path)


    os.rename(source,destination)
#   os.remove(file)   
    ...
 

#! /usr/bin/python3
import os
import sys
# import re
# import collections
import importlib.util


# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# cSpell:enable

spec = importlib.util.spec_from_file_location("module.name",
                                        python_scripts_folder_path +  "helpers/is_video/is_video.py")
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)


def get_all_video_files_in_dir(basepath):
    videos_array = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                if helpers.is_video(entry.name):
                    videos_array.append(entry.name)
        videos_array.sort()
        return videos_array

def create_org_file(cwd, root_videos, dict_with_subfolder_videos):
    file = open('youtube-links.org','w+')

    # create the title header of the file
    file.write('* ' + os.path.basename(cwd) + '\n')

    for video in root_videos:
        filename, ext = os.path.splitext(video)
        file.write('** ' + filename + '\n\n')

    dictlist = []
    for key, value in dict_with_subfolder_videos.items():
        temp = [key,value]
        dictlist.append(temp)

    for directories in dictlist:
        for directory in directories:
            check_list = isinstance(directory, list)
            if not check_list:
                file.write('** ' + str(directory) + '\n')
            else :
                for file_in_directory in directory:
                    filename, ext = os.path.splitext(file_in_directory)
                    file.write('*** ' + filename + '\n\n')

    # file.write('* CGPeers page' + '\n\n\n')

cwd = os.getcwd()

all_files_in_root = get_all_video_files_in_dir(cwd)

dictionary_with_dirs_and_files = {}
# for current_dir in all_dirs:
#   all_files_in_dir = get_all_video_files_in_dir(current_dir)
    # dictionary_with_dirs_and_files[current_dir] = all_files_in_dir

# print(dictionary_with_dirs_and_files)
create_org_file(cwd, all_files_in_root, dictionary_with_dirs_and_files)

# what i want to do

# get all the video files and folders of the current folder
#
# make a nested list that represent the current folder
# elements of the array will be videos
# internal arrays should be directories
#
# crate a text file with the extention of .org
# make the org file with the hierarchy of the arrays
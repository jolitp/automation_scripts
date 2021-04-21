#! /usr/bin/python3
import subprocess
import pathlib
import os
from moviepy.editor import VideoFileClip
import datetime
import shutil

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video


path_to_current_directory = pathlib.Path(__file__).parent.absolute()

current_directory_name = os.path.basename(path_to_current_directory)

all_files_and_folders = os.listdir(path_to_current_directory)

all_videos = []
for file in all_files_and_folders:
    if is_video(file):
        all_videos.append(file)
    pass
all_videos.sort()

for video in all_videos:
    if current_directory_name in video:
        f = open('concatenated_video_found.txt', 'w+')
        f.close()

        print(path_to_current_directory)
        print(current_directory_name)
        path_to_parent_dir = str(path_to_current_directory).replace(current_directory_name, '')
        print(path_to_parent_dir)
        new_folder_name = "[+] " + current_directory_name
        new_path = path_to_parent_dir + new_folder_name
        print(new_path)

        shutil.move(path_to_current_directory, new_path)
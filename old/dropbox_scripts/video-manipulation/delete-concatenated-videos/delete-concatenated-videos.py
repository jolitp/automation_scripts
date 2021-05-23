#! /usr/bin/python3
import pathlib
import os

path_to_current_directory = pathlib.Path(__file__).parent.absolute()

current_directory_name = os.path.basename(path_to_current_directory )

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

# check for video file with the same name as the directory in the emmediate directory
video_path = str(path_to_current_directory) + '/' + current_directory_name + '.mp4'
if os.path.isfile(video_path):
    print(video_path)
    os.remove(video_path)

# check for video file with the same name as the directory in every sub directory
for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        if is_video(name):
            if name == str(current_directory_name + ".mp4"):
                path = str(path_to_current_directory) + '/' + root[2:] + '/' + name
                os.remove(path)
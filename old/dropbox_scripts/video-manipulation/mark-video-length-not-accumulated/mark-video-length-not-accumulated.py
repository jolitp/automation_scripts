#! /usr/bin/python3
import subprocess
import pathlib
import os
from moviepy.editor import VideoFileClip
import datetime

"""
get all the videos in the directory and create files that contain the total length of them
"""
def get_length(filename):
    # print(filename)
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration", "-of",
                            "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    print(result.stdout)
    return float(result.stdout)

video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob']

def is_video(name):
    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video

def from_seconds_to_time(sec):
    return datetime.timedelta(seconds=sec)

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

accumulated_time_file = open("accumulated_time_of_videos.txt", "w+")

accumulated_time = 0
for video in all_videos:
    # clip = VideoFileClip(video)
    # length = clip.duration
    length = get_length(video)
    print('video : ' + str(video) + '\nlength : ' + str(length) + '\n')
    accumulated_time = length
    accumulated_time_formatted = from_seconds_to_time(accumulated_time)
    accumulated_time_file.write(video + " : " + str(accumulated_time_formatted) + "\n")
    formated = from_seconds_to_time(length)
    # print(video + '   ' + str(formated))

accumulated_time_file.close()

print(from_seconds_to_time( accumulated_time ) )

src = current_path
total_length = str(from_seconds_to_time( accumulated_time))
dst = str(current_path) + "/          " + total_length
file_with_length = str(current_path) + "/" + "total_length.data"
print(dst)

#f = open(dst, "w+")
#f.close()

f = open(file_with_length, "w+")
f.write(total_length)
from_seconds_to_time( accumulated_time)
f.close()

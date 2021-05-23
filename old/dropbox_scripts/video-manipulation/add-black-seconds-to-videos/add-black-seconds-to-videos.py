#! /usr/bin/python3.8

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

path_to_current_directory = pathlib.Path(__file__).parent.absolute()

current_directory_name = os.path.basename(path_to_current_directory)

all_files_and_folders = os.listdir(path_to_current_directory)

all_videos = []
for file in all_files_and_folders:
    if is_video(file):
        all_videos.append(file)
all_videos.sort()


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
        # if file == str(current_directory_name + ".mp4"):
        #     concatenated_video_found = True
        #     continue
        old_path_to_file = str(path_to_current_directory) + '/videos/' + str(file)
        new_path_to_file = str(path_to_current_directory) + '/videos/' + str(file)
        shutil.move(old_path_to_file, new_path_to_file)
        print('file ' + file)
        # remove_undesired_characters(file)
        all_videos_in_videos_folder.append(file)
    pass
all_videos_in_videos_folder.sort()
# print(all_videos_in_videos_folder)

duration_occurrences = []
width_and_height_occurrences = []

# get the width and height of each video and put on an array
for video in all_videos_in_videos_folder:
    path_to_video = videos_folder_path + '/' + video
    # print(path_to_video)
    pretty_print_value(str(video), "getting info for: ")
    result = subprocess.run(["mediainfo",'--Inform=\"Video;%Height%\" ', '--Output=JSON', path_to_video], 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    parsed = json.loads(result.stdout)
    video_category = parsed["media"]["track"][1]
    video_width = video_category["Width"]
    video_height = video_category["Height"]
    video_duration = video_category["Duration"]
    # print(video_duration)

    width_and_height_occurrences.append(str(video_width) + ':' +  str(video_height))
    duration_occurrences.append(str(video_duration))
video_info_combined = []

for index, video in enumerate(all_videos_in_videos_folder):
    # pretty_print_value(index,"index")
    # pretty_print_value(video,"video")
    video_name = video
    video_width = width_and_height_occurrences[index].split(':')[0]
    video_height = width_and_height_occurrences[index].split(':')[1]
    video_duration = duration_occurrences[index]
    # pretty_print_value(width_and_height_occurrences[index],"width_and_height_occurrences[index]")
    # pretty_print_value(video_width,"video_width")
    # pretty_print_value(video_height,"video_height")
    data = {
        "name": video_name,
        "width": video_width,
        "height": video_height,
        "duration": video_duration
    }
    video_info_combined.append(data)




# # TODO create blank video with the name of the original video + blank(at the start of filenam or the end?),
# #      or create in a subfolder, the video should have at least 1 second, better to have 10(I know it already works) 
# def create_black_videos(data):
# # command to create a black frame with ffmpeg
# # ffmpeg -f lavfi -i color=black:s=1920x1080:r=24000/1001 -f lavfi -i anullsrc -ar 48000 -ac 2 -t 20 empty.avi

#     video_name = data["name"]
#     video_width = data["width"]
#     video_height = data["height"]
#     ...

# TODO concatenate the blank video at the start and at the end

# TODO nother strategy that maybe work is copy the first second of the video and apend it to the start and end

def remove_chunk_of_video(video_name_local, start, end):
# ffmpeg command to cut part of a video
# ffmpeg -ss 00:01:10 -to 00:02:10 -i input -c copy output

    pretty_print_value(video_name_local, "video_name_local")
    pretty_print_value(start, "start")
    pretty_print_value(end, "end")


    video_path = str(path_to_current_directory) + '/videos/'
    output = video_path +  "black_" + video_name
    pretty_print_value(output, "output")

    ffmpeg_command = 'ffmpeg -ss ' + start + ' -to ' + end + ' -i ' + video_name + ' -c copy ' + output
    pretty_print_value(ffmpeg_command, "ffmpeg_command")
    os.system(ffmpeg_command) 
    ...



pretty_print_array(video_info_combined, "video_info_combined")

for video in all_videos_in_videos_folder:

    video_path = str(path_to_current_directory) + '/videos/' + video
    remove_chunk_of_video(video_path, "00:00:00", "00:01:00")
    ...

# TODO third strategy can be concatenate the videos with itself


# width_and_height_occurrences = []

# # check wether or not the videos have the same dimentions and save on the 'histograms'
# for video in all_videos_in_videos_folder:
#     if video == str(current_directory_name + ".mp4"):
#         concatenated_video_found = True
#         continue
#     path_to_video = videos_folder_path + '/' + video
#     # print(path_to_video)
#     pretty_print_value(str(video), "getting info for: ")
#     result = subprocess.run(["mediainfo",'--Inform=\"Video;%Height%\" ', '--Output=JSON', path_to_video], 
#                             stdout=subprocess.PIPE,
#                             stderr=subprocess.STDOUT)
#     parsed = json.loads(result.stdout)
#     video_category = parsed["media"]["track"][1]
#     video_width = video_category["Width"]
#     add_to_histogram(video_width, histogram_video_width)
#     video_height = video_category["Height"]
#     add_to_histogram(video_height, histogram_video_height)

#     width_and_height_occurrences.append(str(video_width) + ':' +  str(video_height))

# pretty_print_array(width_and_height_occurrences, "width_and_height_occurrences", Fore.YELLOW)




# # get the most common dimensions
# width_and_height_count = {}
# for element in width_and_height_occurrences:
#     if element in width_and_height_count:
#         width_and_height_count[element] += 1
#     else:
#         width_and_height_count[element] = 1

# width_and_height_count_array = []
# for key, value in width_and_height_count.items():
#     temp = [value,key]
#     width_and_height_count_array.append(temp)

# # pretty_print_array(width_and_height_count, "width_and_height_count", Fore.YELLOW)

# pretty_print_value(width_and_height_count, "width_and_height_count")

# pretty_print_array(width_and_height_count_array, "width_and_height_count_array", Fore.YELLOW)

# most_common_width_and_height = width_and_height_count_array[len(width_and_height_count_array) -1]
# # pretty_print_value(most_common_width_and_height, "most_common_width_and_height")

# most_common_width_and_height = re.findall('\'([^"]*)\'', str(most_common_width_and_height))
# most_common_width_and_height : str = most_common_width_and_height[0]
# most_common_width_and_height = most_common_width_and_height.replace('\'','')


# pretty_print_value(most_common_width_and_height, "most_common_width_and_height")
# # print(type(most_common_width_and_height))


# path_to_converted_directory = str(path_to_current_directory) + '/converted/'

# if not os.path.isdir(path_to_converted_directory):
#     os.mkdir(path_to_converted_directory)

# # convert the videos
# for video in all_videos_in_videos_folder:
#     output_video = path_to_converted_directory + '/' + video

#     if os.path.isfile(output_video):
#         continue
#     output_video = os.path.splitext(output_video)[0] + '.mp4'
#     path_to_video_in_videos_folder = str(path_to_current_directory) + '/videos/' + video
#     print(f'{Fore.GREEN}video : {Style.RESET_ALL}' + str(path_to_video_in_videos_folder))
#     flags = f' -r 30 -c:v libx264 -pix_fmt yuv420p -crf 17 -c:a aac -b:a 128k -movflags +faststart -vf scale={most_common_width_and_height} '
#     command = f'ffmpeg -i \"{path_to_video_in_videos_folder}\" {flags} \"{output_video}\"'
#     # command = f'ffmpeg -i \"{path_to_video_in_videos_folder}\" -r 30 -c:v libx264 -pix_fmt yuv420p -crf 17 -c:a aac -b:a 128k \"{output_video}\"'
#     print(f'{Fore.GREEN}command : {Style.RESET_ALL}' + command)
#     os.system(command)                                                       # comment to test 

# # if not (len(histogram_video_height) == 1 and len(histogram_video_width) == 1):
# #     print(f'{Fore.RED}videos have different dimentions{Style.RESET_ALL}')
# #     make_different_dimensions_file()
# #     # sys.exit()

# def make_video_list_file(all_videos):
#     f = open('vidlist.txt', 'w+')
#     f.close()
    
#     for video in all_videos:
#         f = open('vidlist.txt', 'a')
#         video = os.path.splitext(video)[0] + '.mp4'
#         f.write(f"file \'{path_to_converted_directory + video}\'\n")
#     return 'vidlist.txt'


# # concatenate videos

# if DEBUG : print(f'{Fore.GREEN}videos in video folder{Style.RESET_ALL}')

# for video in all_videos_in_videos_folder:
#     if DEBUG : print(f'{Fore.YELLOW}video {Style.RESET_ALL}: ' + str(video)) 

# output_video = str(path_to_current_directory) + '.mp4'
# pretty_print_value(output_video,"output_video")

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
# if DEBUG : print(f'{Fore.BLUE}ffmpeg command{Style.RESET_ALL}: ' + ffmpeg_command) 

# os.system(ffmpeg_command)                                                      # deactivate to test
 

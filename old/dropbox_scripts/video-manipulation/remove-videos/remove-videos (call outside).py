#! /usr/bin/python3

import subprocess
import os
from colorama import Fore
from colorama import Style

DEBUG = False
DEBUG = True                                                                   # comment to toggle
# TODO get the filesize of videos and display the total size removed
# pretty print an array
def pretty_print_array(array,message,color=Fore.GREEN):
    if DEBUG : print(f'{color} = ' + message + f' = {Style.RESET_ALL}')
    for index, name in enumerate(array):
        start = f' {color} '
        reset = f' : {Style.RESET_ALL} '
        if DEBUG : print(start + str(index) + reset + str(name))



def pretty_print_value(value,message,color=Fore.BLUE):
    if DEBUG : print(f' {color} ' + message + f' : {Style.RESET_ALL} ' + str(value))



def is_video(name):
    video_extensions = ['.mp4', '.m4v', '.mkv', '.ts', '.avi', '.webm', '.flv', '.mov', '.wmv', '.vob', '.ogm' , '.mpg', '.divx']

    is_video = False
    for ext in video_extensions:
        if name.lower().endswith(ext):
            is_video = True
    return is_video



def remove_folder_recursively(folder_path):
    """removes a folder from the file system

    Args:
        folder_path (path): the path of the folder
    """

    print()
    message : str = "removing folder"
    pretty_print_value(folder_path,message,Fore.YELLOW)
    print()

    command = "rm -rf \"" + folder_path + "\""
    print(command)
    os.system(command)
    ...



def remove_video(video_path):
    """removes a video from the file system

    Args:
        video_path (path): the path of the video file
    """
    print()
    message : str = "removing folder"
    pretty_print_value(video_path,message,Fore.YELLOW)
    print()


    command = "rm \"" + video_path + "\""
    print(command)
    os.system(command)
    ...



# BUG get_all_folders_in_directory not returning any folder
def get_all_folders_in_directory(directory: str):
    """get all folders inside a directory

    Args:
        directory (str): the directory path

    Returns:
        list: all folders inside directory
    """
    # print()
    # print()
    # print("[def] get_all_folders_in_directory(")
    # print("      directory : ")
    # print("                                  " +  directory )
    # print("                                  )")
    # print("{")

    all_files_and_folders = os.listdir(directory)
    absolute_path_to_all_files_and_folders = []
    for item in all_files_and_folders:
        # print("item: " + item)
        absolute_path = directory + "/" + item
        absolute_path_to_all_files_and_folders.append(absolute_path)
        ...
    # print()
    # pretty_print_array(all_files_and_folders,"all_files_and_folders")
    # print()

    only_folders = []

    # print("[for] item in all_files_and_folders:")
    for item in absolute_path_to_all_files_and_folders:
        # print("item: " + item)
        # print()
        # print("[if] os.path.isdir(item):    " + str(os.path.isdir(item)))
        # print()
        if os.path.isdir(item):
            # print()
            # print("!!")
            # print("!! adding " + item + " to only_folders")
            # print("!!")
            # print()
            only_folders.append(item)
            # pretty_print_array(only_folders,"only_folders")
            # print()
        ...
    # print(only_folders)

    # print()
    # pretty_print_array(only_folders,"only_folders")
    # print()

    # print("}")
    # print()
    # print()

    return only_folders



def get_all_videos_in_directory(directory: str):
    """get all videos inside a directory

    Args:
        directory (str): the directory path

    Returns:
        list: all videos inside directory
    """

    all_files_and_folders = os.listdir(directory)

    only_videos = []
    for file in all_files_and_folders:
        if is_video(file):
            only_videos.append(file)
        ...

    return only_videos



def get_all_compressed_files_in_directory(directory: str):
    """get all compressed files inside a directory

    Args:
        directory (str): the directory path

    Returns:
        list: all compressed files inside directory
    """

    all_files_and_folders = os.listdir(directory)

    only_compressed_files = []
    for file in all_files_and_folders:
        if '.zip' in file or '.7z' in file:
            only_compressed_files.append(file)
        ...

    return only_compressed_files


path_to_current_directory = str(os.getcwd())
# print(path_to_current_directory)
all_folders = get_all_folders_in_directory(path_to_current_directory)

# print()
# pretty_print_array(all_folders,"all_folders")
# print()

for current_folder in all_folders:

    # print("current_folder " + current_folder)
    all_inside_folders = get_all_folders_in_directory(current_folder)

    # print()
    # pretty_print_array(all_inside_folders,"all_inside_folders")
    # print()

    all_videos = get_all_videos_in_directory(current_folder)

    # print()
    # pretty_print_array(all_videos,"all_videos")
    # print()

    all_compressed_files = get_all_compressed_files_in_directory(current_folder)

    # print()
    # pretty_print_array(all_compressed_files,"all_compressed_files")
    # print()

    for video in all_videos:
        full_path : str = current_folder + "/" + video

        # print(full_path)
        # print()
        # print(path_to_current_directory)
        # print()
        # print(current_folder)
        # print()
        # print(video)
        # print()
        remove_video(full_path)
        # print()
        # print("-> removing video: \n\t" + video)
        ...

    for folder in all_inside_folders:
        full_path : str = path_to_current_directory + "/" + current_folder + "/" + folder
        # print("loop")
        # print()
        # print(path_to_current_directory)
        # print()
        # print(current_folder)
        # print()
        # print(folder)
        # print()
        folders_to_delete = [
            'converted',
            'videos',
            'broken',
            'undesirable_files',
        ]

        if 'files' in folder:
            if folder in all_compressed_files:
                print(folder)

            ...
# BUG files folder is being deleted even though it is not in the folders to be deleted list
        for folder_to_delete in folders_to_delete:
            print()
            print("[if] if folder_to_delete in folder: " + folder_to_delete in folder)
            print("     folder_to_delete             : " + folder_to_delete)
            print("     folder                       : " + folder)
            print()
            if folder_to_delete in folder:
                remove_folder_recursively(folder)
                print()
                # print("-> remove folder: \n\t" + full_path)
                ...
            ...
        ...

    ...


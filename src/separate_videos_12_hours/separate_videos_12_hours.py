#! /usr/bin/env python3
"""
moves this folder depending on wether or not the video data in it
have an accumulated duration of 12 hours or less

if duration is more than 12 hours, move folder to:
0000_long/
else:
0000_short/
"""
# cSpell: word jolitp pytest miliseconds avidemux
import os
import csv
from pathlib import Path

from natsort import natsorted, ns
from rich.console import Console
from rich.table import Table
from rich.traceback import install
install()


# region load_video_infos_csv
def load_video_infos_csv(
    file_path: str,
    debug_function: bool = None
    ):
    """load the values of a .csv file
    containing the info of all videos
    in the directory

    Args:
        file_path (str): the file path to the file

        debug_function (bool, optional): Defaults to None.

    Returns:
        (list(dict)): the values from .csv file parsed into a dictionary
    """
    # debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START load_video_infos_csv")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def load_video_infos_csv(                                                    |")
        print(f"|   file_path = {file_path}")
        print("|                                                                              |")

    video_info_list = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for ordered_dict in csv_reader:
            video_info_list.append(ordered_dict)


    if debug_function:
        print()
        print("return video_infos = [                                                         |")
        for element in video_info_list:
            print("|   {                                                                          |")
            for key in element:
                print(f"|     '{key}': {element[key]}")
            print("|   }                                                                          |")
        print("|  ]")
        print("| }                                                                            |")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   load_video_infos_csv")
    return video_info_list
# endregion load_video_infos_csv




# region main
def main(
    debug_function = None
):
    debug_function = True # comment to toggle

    c = Console()
    cwd = os.getcwd()

    if debug_function:
        print()
        print("current_working_directory:")
        print(cwd)

    all_nested_videos = []
    videos_folder_path = cwd + "/videos"
    videos_infos_csv_file_on_videos = ""
    if os.path.isdir(videos_folder_path):
        all_nested_videos = os.listdir(videos_folder_path)
        videos_infos_csv_file_on_videos = videos_folder_path + "/.generated/video_infos.csv"

        if debug_function:
            print()
            print("all_nested_videos = [")
            for element in all_nested_videos:
                print("  {}".format(element))
            print("]")
            print()
            print("videos_infos_csv_file_on_videos:")
            print(videos_infos_csv_file_on_videos)
            print()

    all_immediate_items = os.listdir(cwd)
    videos_infos_csv_file_on_root = cwd + "/.generated/video_infos.csv"

    if debug_function:
        print()
        print("all_immediate_items = [")
        for element in all_immediate_items:
            print("  {}".format(element))
        print("]")
        print()
        print("videos_infos_csv_file_on_root:")
        print(videos_infos_csv_file_on_root)
        print()

    has_video_data: bool = False
    if os.path.isdir(videos_folder_path):
        if os.path.isfile(videos_infos_csv_file_on_videos):
            has_video_data = True
            video_info_list = \
                load_video_infos_csv(videos_infos_csv_file_on_videos)
    else:
        if os.path.isfile(videos_infos_csv_file_on_root):
            has_video_data = True
            video_info_list = \
                load_video_infos_csv(videos_infos_csv_file_on_root)

    if debug_function:
        c.log(video_info_list)

    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   main")
# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START concatenate_videos.py START"
    print(msg)
    print()

    main()

    msg = "END concatenate_videos.py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":


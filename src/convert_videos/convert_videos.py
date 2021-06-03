#! /usr/bin/env python3
"""
convert videos with ffmpeg
"""
# cSpell: word jolitp chdir ffmpeg
import os
import sys
from pathlib import Path
import csv
from collections import Counter

from natsort import natsorted, ns
from rich.console import Console
from rich.traceback import install
import snoop

install()

# region ========================================= load_video_infos_csv
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
    ...
# endregion -------------------------------------- load_video_infos_csv


# region ============================================= assemble_command
def assemble_command(
    video_info_list:dict,
    ):
    """
    assemble the ffmpeg command to convert videos

    Args:
        video_info_list (dict): the data for the videos
    """

    c = Console()

    src_data = simplify_data(video_info_list)

    src_dimmensions_list = []
    for data in src_data:
        dimmension = data["dimensions"]
        src_dimmensions_list.append(dimmension)

    dst_dimmension = most_common_dimension(src_dimmensions_list)

    dst_paths = get_dst_paths(src_data)

    are_same_ar = same_aspect_ratio(src_data)


# endregion ------------------------------------------ assemble_command


# region ============================================= same_aspect_ratio
def same_aspect_ratio(src_data):
# TODO check if aspect ratio is the same for all videos

    first_ar = src_data[0]["aspect_ratio"]
    c = Console()
    c.print(first_ar)

# TODO map other values of list if have the same as first, return bool
    ...
# endregion ------------------------------------------ same_aspect_ratio


# region ================================================ get_dst_paths
# @snoop
def get_dst_paths(video_info_list):
    dst_paths = []
    for video_info in video_info_list:
        src_path = video_info["path"]
        src_basename = Path(os.path.basename(src_path))
        cwd = Path(os.getcwd())
        converted_folder_path = cwd / 'converted'

        dst_path = converted_folder_path / src_basename
        dst_paths.append(dst_path)
        ...
    return dst_paths
    ...
# endregion --------------------------------------------- get_dst_paths


# region ======================================== most_common_dimension
def most_common_dimension(
    dimmensions_list:list
    ):
    c = Counter(dimmensions_list)
    most_common = c.most_common(1)
    most_common_dimension = most_common[0][0]
    return most_common_dimension
# endregion ------------------------------------- most_common_dimension


# region ================================================ simplify_data
def simplify_data(
    video_info_list:dict
):
    src_videos_data = []
    for video_info in video_info_list:
        src_video_path = Path(video_info["full_path"])
        src_video_width = int(video_info["width"])
        src_video_height = int(video_info["height"])
        src_video_dimensions = (src_video_width, src_video_height)
        src_video_ar = float(video_info["aspect_ratio"])
        src_video_arf:str = video_info["aspect_ratio_fraction"]
        src_video_arf = src_video_arf.split(":")
        src_video_arf = (int(src_video_arf[0]), int(src_video_arf[1]))

        src_data = {
            "path" : src_video_path,
            "dimensions" : src_video_dimensions,
            "aspect_ratio" : src_video_ar,
            "aspect_ratio_fraction" : src_video_arf,
        }

        src_videos_data.append(src_data)
    return src_videos_data
# endregion --------------------------------------------- simplify_data


# region =============================================== process_folder
def process_folder(
    folder_path:Path,
    debug_function = None
):
    """do the actual logic of the script on a specified folder

    Args:
        folder_path (Path): the path to the folder
        debug_function (bool, optional): Defaults to None.
    """
    debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START === process_folder() === START ")
        print()
        print("def process_folder(")
        print(f"|   folder_path:Path = {folder_path}")
        print()

# TODO handle case: more than one videos folder
    csv_file_path = folder_path / ".generated/video_infos.csv"

    csv_file_exists = os.path.isfile(csv_file_path)

    c = Console()
    videos_data = None
    if csv_file_exists:
        videos_data = load_video_infos_csv(csv_file_path)
        ...
    else:
        c.print("[bold red]no csv file found at[/] {}"\
            .format(csv_file_path))
        ...

    # c.print(videos_data)
    assemble_command(videos_data)

    if debug_function:
        print()
        print("END === process_folder() === END")
        print()
# endregion -------------------------------------------- process_folder


# region ========================================================= main
def main(
):
    """main function from script

    """
    cwd = Path(os.getcwd())

    videos_folder_path = cwd / "videos"

    process_folder(videos_folder_path)
# endregion ------------------------------------------------------ main


# region ================================================= current_test
def current_test():
    c = Console()
    input = [
        (1920, 1080),
        (1920, 1080),
        (1080, 720),
    ]
    c.print("input {}".format(input))
    expected_output = (1920, 1080)
    c.print("expected_output {}".format(expected_output))
    actual_output = most_common_dimension(input)
    c.print("actual_output {}".format(actual_output))
    assertion = expected_output == actual_output
    c.print("assertion {}".format(assertion))
# endregion ---------------------------------------------- current_test


# region =================================== if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START call_command_in_all_folders.py START"
    print(msg)
    print()

    main()

    # current_test()

    msg = "END call_command_in_all_folders.py END"
    print()
    print(msg)
    print()
# endregion -------------------------------- if __name__ == "__main__":


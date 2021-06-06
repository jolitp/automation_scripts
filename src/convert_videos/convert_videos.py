#! /usr/bin/env python3
"""
convert videos with ffmpeg
"""
# cSpell: word jolitp chdir ffmpeg libx movflags cmdline Popen
import os
import sys
from pathlib import Path
import csv
from collections import Counter
from typing import Tuple
import subprocess
from subprocess import *

from natsort import natsorted, ns
from rich.console import Console
from rich.traceback import install as install_rich_traceback
import snoop

install_rich_traceback()

# region load_video_infos_csv ========================== load_video_infos_csv
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
# endregion load_video_infos_csv ------------------- load_video_infos_csv


# region assemble_command ============================= assemble_command
def assemble_command(
    src_path:Path,
    dst_path:Path,
    subtitle_path:Path,
    output_dimensions:Tuple[int,int]
    ):
    """
    assemble the ffmpeg command to convert videos

    Args:
        video_info_list (dict): the data for the videos
    """

# ffmpeg -i input.mkv -c:v libx264 -c:a aac -s 1080:720 -aspect 16:9 output.mkv
# ❯ ffmpeg -y -i input.mkv -c:v libx264 -c:a aac -s 1080:720 -aspect 16:9 -vf subtitles=input.vtt output.mkv


    ffmpeg_command = ["ffmpeg"]
    ffmpeg_flags = ["-n"]
    video_codec_flags = ["-c:v", "libx264"]
    audio_codec_flags = ["-c:a", "aac"]
    width, height = output_dimensions
    dimension_flags = ["-s", f"{width}:{height}"]
    subs_flags = []
    if subtitle_path:
        subs_flags = ["-vf", f"subtitles={subtitle_path}"]

    src_flags = ["-i", str(src_path)]
    dst_flags = [ str(dst_path)]

    pv_command = ["pv", str(src_path), "|"]
    ffmpeg_command_pv_additions = ["-i","pipe:0", "-v", "warning"]

    final_command = []
    final_command.extend(pv_command)
    final_command.extend(ffmpeg_command)
    final_command.extend(ffmpeg_command_pv_additions)
    final_command.extend(ffmpeg_flags)
    final_command.extend(src_flags)
    final_command.extend(video_codec_flags)
    final_command.extend(audio_codec_flags)
    final_command.extend(dimension_flags)
    final_command.extend(subs_flags)
    final_command.extend(dst_flags)

    return final_command

# endregion assemble_command -------------------------- assemble_command


# region get_src_paths ================================== get_src_paths
def get_src_paths(src_data):
    src_paths = []
    for video_info in src_data:
        src_path = video_info["path"]
        src_basename = Path(src_path)
        cwd = Path(os.getcwd())

        src_path = cwd / src_basename
        src_paths.append(src_path)
        ...
    return src_paths
    ...
# endregion get_src_paths ------------------------------- get_src_paths


# region are_aspect_ratios_the_same ================== same_aspect_ratio
def are_aspect_ratios_the_same(src_data):
    same_ar = True
    if src_data:
        first_ar = src_data[0]["aspect_ratio"]
        c = Console()
        # c.print(first_ar)
        for data in src_data:
            if data["aspect_ratio"] != first_ar:
                same_ar = False
    else:
        same_ar = None
    return same_ar
# endregion are_aspect_ratios_the_same --------------- same_aspect_ratio


# region get_dst_paths ================================== get_dst_paths
# @snoop
def get_dst_paths(video_info_list):
    dst_paths = []
    for video_info in video_info_list:
        src_path = video_info["path"]
        src_path = str(src_path).replace("videos", "converted")
        src_basename = Path(src_path)
        cwd = Path(os.getcwd())

        dst_path = cwd / src_basename
        dst_paths.append(dst_path)
        ...
    return dst_paths
    ...
# endregion get_dst_paths ------------------------------- get_dst_paths


# region most_common_dimension ======================= most_common_dimension
def most_common_dimension(src_data:list):
    src_dimmensions_list = []
    for data in src_data:
        dimmension = data["dimensions"]
        src_dimmensions_list.append(dimmension)
    c = Counter(src_dimmensions_list)
    most_common = c.most_common(1)
    most_common_dimension = most_common[0][0]
    return most_common_dimension
# endregion most_common_dimension -------------------- most_common_dimension


# region simplify_data ================================== simplify_data
def simplify_data(video_info_list:dict):
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
# endregion simplify_data ----------------------------- simplify_data


# region get_subs_path_from_video_path == get_subs_path_from_video_path
def get_subs_path_from_video_path(src_video_path:Path):
    cwd = os.getcwd()
    videos_folder_path = src_video_path.parent
    videos_folder_basename = os.path.basename(videos_folder_path)
    subs_folder_basename = Path(videos_folder_basename.replace("videos", "subs"))
    subs_folder_path = cwd / subs_folder_basename
    subsubtitle_file = None
    subs_folder_exists = os.path.exists(subs_folder_path)

    if subs_folder_exists:
        src_video_basename = os.path.basename(src_video_path)
        basename_no_ext = os.path.splitext(src_video_basename)[0]
        # search for filename in subs directory
        files_in_subfolder = os.listdir(subs_folder_path)
        for file in files_in_subfolder:
            if basename_no_ext in file:
                subsubtitle_file = subs_folder_path / Path(file)
        return subsubtitle_file
    else:
        return None
# endregion get_subs_path_from_video_path -- get_subs_path_from_video_path


# region create_converted_folder ======================= create_converted_folder
def create_converted_folder(videos_folder_path:Path):
    videos_folder_basename = os.path.basename(videos_folder_path)
    videos_folder_parent = videos_folder_path.parent
    converted_basename = videos_folder_basename.replace("videos", "converted")

    converted_path = videos_folder_parent / Path(converted_basename)
    if not os.path.exists(converted_path):
        os.mkdir(converted_path)
# endregion create_converted_folder -------------------- create_converted_folder


# region print_entire_line ================================== print_entire_line
def print_entire_line(
    console:Console,
    text:str,
    foreground:str="white",
    background:str="black",
    ):
    c = console
    console_width = c.width
    remaining_width = console_width - len(text)
    output_style = "[" + foreground + " on " + background + "]"
    c.print(output_style + \
        " "*int(remaining_width/2) + \
        text + \
        " "*int(remaining_width/2) + \
        "[/]")
# endregion print_entire_line ----------------------------------- print_entire_line

# region process_folder ================================== process_folder
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
    c = Console()

    if debug_function:
        print()
        print("START === process_folder() === START ")
        print()
        print("def process_folder(")
        print(f"|   folder_path:Path = {folder_path}")
        print()

    csv_file_path = folder_path / ".generated/video_infos.csv"
    csv_file_exists = os.path.isfile(csv_file_path)

    videos_data = None
    if csv_file_exists:
        videos_data = load_video_infos_csv(csv_file_path)

        if videos_data:
            src_data = simplify_data(videos_data)
            src_paths = get_src_paths(src_data)
            dst_paths = get_dst_paths(src_data)
            are_same_ar = are_aspect_ratios_the_same(src_data)
            if are_same_ar:
                output_dimmension = most_common_dimension(src_data)
                for index, _ in enumerate(videos_data):
                    src_path = src_paths[index]
                    subs_path = get_subs_path_from_video_path(src_path)
                    dst_path = dst_paths[index]
                    create_converted_folder(folder_path)

                    command = assemble_command(src_path, dst_path, subs_path, output_dimmension)
                    cmd_string = subprocess.list2cmdline(command)

                    src_basename = os.path.basename(src_path)
                    msg = f"converting: {src_basename}"
                    # TODO print more information about the convertion
                    print_entire_line(c, msg, "#03014f", "#cccccc")
                    c.print(cmd_string)
                    # TODO check if required programs are installed
                    # ffmpeg and pv

                    os.system(cmd_string)
                    # TODO capture output into a file
            else:
                c.print("[bold red]the aspect ratio of videos are not the same![/]")
        else:
            c.print(f"[bold red]there are no videos in {folder_path}[/]")

    else:
        c.print("[bold red]no csv file found at[/]: \n{}"\
            .format(csv_file_path))
        ...

    # c.print(videos_data)


# TODO make converted folders before trying to run command
    if debug_function:
        print()
        print("END === process_folder() === END")
        print()
# endregion =============  ----------------------------- process_folder


# region main ========================================================= main
def main(
):
    """main function from script

    """
    cwd = Path(os.getcwd())

    all_items = os.listdir(cwd)

    all_videos_folders = []
    all_subs_folders = []
    for item in all_items:
        if os.path.isdir(item):
            if "videos" in item:
                folder_path = cwd / Path(item)
                all_videos_folders.append(folder_path)

    for folder in all_videos_folders:
        process_folder(folder)
# endregion main ------------------------------------------------------ main


# region current_test ================================================= current_test
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
# endregion current_test ---------------------------------------------- current_test


# region if __name__ == "__main__": =============== if __name__ == "__main__":
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
# endregion if __name__ == "__main__": ------------ if __name__ == "__main__":


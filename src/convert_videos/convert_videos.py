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
import datetime

from natsort import natsorted, ns
from rich.console import Console
from rich.traceback import install as install_rich_traceback
from rich.panel import Panel
import snoop

install_rich_traceback()

MAX_NUMBER_OF_FOLDERS = None
CURRENT_FOLDER = None
NUMBER_OF_VIDEOS_IN_EACH_FOLDER = {}

CONSOLE = Console(record=True)


# TODO put function in a library
# region _remove_dot_from_extension
def _remove_dot_from_extension(
    extensions
):
    """remove the dot from an extension

    Args:
        extensions (str or list): the extension
    Returns:
        the extension without the dot
    """
    if isinstance(extensions, str):
        ext : str = extensions
        extensions = ext.replace(".","")
    return extensions
# endregion _remove_dot_from_extension


# TODO put function in a library
# region filter_files_by_extension
def filter_files_by_extension(
    files: list ,
    extensions: list
):
    """
    filter the files in a list to have only files of the given extensions

    Args:
        files (list):
            the list of files
        extensions (list):
            the list of extensions

    Returns:
        filtered_files (list):
            the list of files with only files of the given extensions
    """
    filtered_files = []
    for file in files:
        file_ext = os.path.splitext(file)[-1].lower()
        file_ext = _remove_dot_from_extension(file_ext)
        for extension in extensions:
            ext = _remove_dot_from_extension(extension).lower()
            # print("ext \n", ext)
            # print("file_ext \n", file_ext)
            if file_ext == ext:
                filtered_files.append(file)

    return filtered_files
    ...
# endregion filter_files_by_extension


# TODO put function in a library
# region filter_subtitles
def filter_subtitles(
    files: list
):
    """filter a list of files to contain only subtitle type files
    the filtering happens based on the extension of the files

    Args:
        files (list): the list of files

    Returns:
        videos (list): the list of subtitles
    """
#cSpell:words ttml dfxp
    subtitles_extensions = [
            "srt",
            "vtt",
            "ssa",
            "ttml",
            "sbv",
            "dfxp",
    ]
    return filter_files_by_extension(files, subtitles_extensions)
    ...
# endregion filter_videos


# TODO put function in a library
# region filter_videos
def filter_videos(
    files: list
):
    """filter a list of files to contain only video type files
    the filtering happens based on the extension of the files

    Args:
        files (list): the list of files

    Returns:
        videos (list): the list of videos
    """
#cSpell:words webm vchd rmvb gifv xvid vidx
    video_extensions = [
        "WEBM",
        "MPG","MP2", "MPEG", "MPE", "MPV",
        "OGV","OGG",
        "MP4", "M4P", "M4V",
        "AVI",
        "WMV",
        "MOV","QT",
        "FLV","SWF",
        "F4V","F4P","F4A","F4B",
        "VCHD",
        "RMVB","RM",
        "VOB",
        "MKV",
        "MTS", "M2TS", "TS",
        "MNG",
        "GIFV",
        "GIF",
        "DRC",
        "XVID",
        "VIDX",
        "ASF",
        "AMV",
        "M2V",
        "SVI",
        "3GP",
        "MXF",
        "ROQ",
        "NSV",
        "3G2",
    ]
    return filter_files_by_extension(files, video_extensions)
    ...
# endregion filter_videos


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
        # CONSOLE.print(first_ar)
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
    text:str,
    foreground:str="white",
    background:str="black",
    ):

    console_width = CONSOLE.width
    remaining_width = console_width - len(text)
    output_style = "[" + foreground + " on " + background + "]"
    CONSOLE.print(output_style + \
        " "*int(remaining_width/2) + \
        text + \
        " "*int(remaining_width/2) + \
        "[/]")
# endregion print_entire_line ----------------------------------- print_entire_line


# region print_info_panel ============================= print_info_panel
def print_info_panel(
    video_data,
    basename,
    src_path,
    dst_path,
    subs_path,
    output_dimension
    ):
    # print info panel
    conversion_info = ""
    conversion_info += "Paths:\n"
    conversion_info += \
        f"[yellow]video name[/]: [cyan]{basename}[/]\n"
    conversion_info += \
        f"[yellow]source path[/]: [cyan]{src_path}[/]\n"
    conversion_info += \
        f"[yellow]destination path[/]: [cyan]{dst_path}[/]\n"
    conversion_info += \
        f"[yellow]subs path[/]: [cyan]{subs_path}[/]\n"
    conversion_info += "\nData:\n"
    for data in video_data:
        conversion_info += \
            f"[yellow]{data}[/]: [cyan]{video_data[data]}[/]\n"
    conversion_info += \
        f"[yellow]output dimension[/]: [cyan]{output_dimension}[/]"

    CONSOLE.print(Panel(conversion_info, title="video info"))
    ...
# endregion print_info_panel --------------------------- print_info_panel


# region print_conversion_summary ================== print_conversion_summary
def print_conversion_summary(folder_path,index):
    # print panel with conversion summary

    current_video_number = index + 1
    videos_converted_string = ""
    number_of_videos_in_this_folder = \
        NUMBER_OF_VIDEOS_IN_EACH_FOLDER[folder_path]["number_of_videos"]
    remaining_number_of_videos = \
    number_of_videos_in_this_folder - current_video_number
    converted_videos_metter = "●" * (index)
    current_video_metter = "◐"
    remaining_video_metter = "○" * remaining_number_of_videos
    videos_converted_string += converted_videos_metter + \
        current_video_metter + remaining_video_metter
    CONSOLE.print(Panel(videos_converted_string,
                        title="videos converted"))
# endregion print_conversion_summary --------------- print_conversion_summary


# region convert_video ==================================== convert_video
def convert_video(
    index,
    videos_data,
    folder_path,
    src_paths,
    dst_paths,
    output_dimension
    ):
    max_videos = len(videos_data)
    current_video_number = index + 1
    src_path = src_paths[index]
    subs_path = get_subs_path_from_video_path(src_path)
    dst_path = dst_paths[index]
    create_converted_folder(folder_path)
    command = assemble_command(src_path,
                                dst_path,
                                subs_path,
                                output_dimension)
    cmd_string = subprocess.list2cmdline(command)
    src_basename = os.path.basename(src_path)
    msg = f"converting: {src_basename}"
    print_entire_line(msg, "#03014f", "#cccccc")
    print_info_panel(videos_data[index],
                    src_basename,
                    src_path,
                    dst_path,
                    subs_path,
                    output_dimension)
    new_cmd_string = ""
    for part in command:
        part = add_random_color(part,min=120)
        new_cmd_string += " " + part + "\n"
    CONSOLE.print(Panel(new_cmd_string, title="command parts"))
    CONSOLE.print(Panel(cmd_string, title="command called"))
    print_conversion_summary(folder_path,index)
    print_progress_bar(
        "folder",
        CURRENT_FOLDER,
        MAX_NUMBER_OF_FOLDERS,
        foreground="bold #000000",
        background="#aaaaaa")
    print_progress_bar(
        "video",
        current_video_number,
        max_videos,
        foreground="bold #000000",
        background="#aaaaaa")
    os.system(cmd_string)
    ...
# endregion convert_video ------------------------------- convert_video


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
    # debug_function = True # comment to toggle

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
                output_dimension = most_common_dimension(src_data)
                for index, _ in enumerate(videos_data):
                    convert_video(
                            index,
                            videos_data,
                            folder_path,
                            src_paths,
                            dst_paths,
                            output_dimension)
            else:
                CONSOLE.print("[bold red]the aspect ratio of videos are not the same![/]")
                with open(folder_path / "_000_different_aspect_ratio", "w") as file:
                    file.write("different_aspect_ratio")
                output_dimension = most_common_dimension(src_data)
                for index, _ in enumerate(videos_data):
                    convert_video(
                            index,
                            videos_data,
                            folder_path,
                            src_paths,
                            dst_paths,
                            output_dimension)
        else:
            CONSOLE.print(f"[bold red]there are no videos in {folder_path}[/]")
    else:
        CONSOLE.print("[bold red]no csv file found at[/]: \n{}"\
            .format(csv_file_path))
    if debug_function:
        print()
        print("END === process_folder() === END")
        print()
# endregion =============  ----------------------------- process_folder


# TODO add to function library
# region add_color =========================================== add_color
def add_color(color, msg):
    return "[" + color + "]" + msg + "[/]"
# endregion add_color ---------------------------------------- add_color


# TODO add to function library
# region add_random_color =========================================== add_random_color
def add_random_color(msg, min=0,max=255):
    import random
    color = ""
    r = lambda: random.randint(min,max)
    color = '#%02X%02X%02X' % (r(),r(),r())
    return "[" + color + "]" + msg + "[/]"
# endregion add_random_color ---------------------------------------- add_random_color


# region print_progress_bar ============================== print_progress_bar
def print_progress_bar(msg, current_value, total_value, background, foreground):
    text = f"{msg} : {current_value}/{total_value}"
    console_width = CONSOLE.width
    remaining_width = console_width - len(text)
    output_style = "[" + foreground + " on " + background + "]"
    filled = "▰"
    empty = "▱"
    section_length = console_width / total_value
    filled_length = section_length * current_value
    empty_length = console_width - filled_length

    CONSOLE.print(output_style + \
        " "*int(remaining_width/2) + \
        text + \
        " "*int(remaining_width/2) + \
        "[/]")
    CONSOLE.print(output_style + \
        filled*int(filled_length)+ \
        empty*int(empty_length) + \
        "[/]")
# endregion print_progress_bar ----------------------------- print_progress_bar


# region get_number_of_videos_in_folders ============= get_number_of_videos_in_folders
def videos_converted_in_each_folder():
    global NUMBER_OF_VIDEOS_IN_EACH_FOLDER
    for key,value in NUMBER_OF_VIDEOS_IN_EACH_FOLDER.items():
        CONSOLE.print("key:{}\nvalue:{}".format(key,value))
        ...
    ...
# endregion get_number_of_videos_in_folders --------- get_number_of_videos_in_folders


# region get_number_of_videos_in_folders ============= get_number_of_videos_in_folders
def get_number_of_videos_in_folders(videos_folders:list):
    global NUMBER_OF_VIDEOS_IN_EACH_FOLDER
    for video_folder in videos_folders:
        this_folder_items = os.listdir(video_folder)
        this_folder_videos = filter_videos(this_folder_items)
        number_of_videos_in_this_folder = len(this_folder_videos)
        data = {
            "number_of_videos": number_of_videos_in_this_folder,
        }
        NUMBER_OF_VIDEOS_IN_EACH_FOLDER[video_folder] = data
    ...
# endregion get_number_of_videos_in_folders --------- get_number_of_videos_in_folders


# region main ========================================================= main
def main(
):
    """main function from script

    """
    cwd = Path(os.getcwd())

    all_items = os.listdir(cwd)

    all_videos_folders = []
    for item in all_items:
        if os.path.isdir(item):
            if "videos" in item:
                folder_path = cwd / Path(item)
                all_videos_folders.append(folder_path)
    global MAX_NUMBER_OF_FOLDERS
    MAX_NUMBER_OF_FOLDERS = len(all_videos_folders)
    # for index, folder in enumerate(all_videos_folders):
    from rich.progress import Progress
    length = len(all_videos_folders)

# TODO put the amount of videos in each folder into a global variable
# to use in the summary before converting
    get_number_of_videos_in_folders(all_videos_folders)

    for index, folder in enumerate(all_videos_folders):
        global CURRENT_FOLDER
        CURRENT_FOLDER = index + 1

        print_progress_bar(
            "folder",
            CURRENT_FOLDER,
            MAX_NUMBER_OF_FOLDERS,
            foreground="bold #000000",
            background="#cccccc")

        process_folder(folder)

            # progress.update(process_folder_task, advance=1)
# endregion main ------------------------------------------------------ main


# region current_test ================================================= current_test
def current_test():
    input = [
        (1920, 1080),
        (1920, 1080),
        (1080, 720),
    ]
    CONSOLE.print("input {}".format(input))
    expected_output = (1920, 1080)
    CONSOLE.print("expected_output {}".format(expected_output))
    actual_output = most_common_dimension(input)
    CONSOLE.print("actual_output {}".format(actual_output))
    assertion = expected_output == actual_output
    CONSOLE.print("assertion {}".format(assertion))
# endregion current_test ---------------------------------------------- current_test


# TODO put on library
# region change_background_of_html ============================ change_background_of_html
def change_background_of_html(html_file):
    lines = None
    with open(html_file, "r") as file:
        lines = file.readlines()

    for index, current_line in enumerate(lines):
        if "    background-color: #ffffff;\n" in current_line:
            lines[index] = current_line.replace("#ffffff","#000000")
            ...
        ...
    with open(html_file, "w") as file:
        for line in lines:
            file.write(line)
        ...
# endregion change_background_of_html ------------------------- change_background_of_html


# region if __name__ == "__main__": =============== if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START call_command_in_all_folders.py START"
    print(msg)
    print()

    main()

    cwd = Path(os.getcwd())
    now = datetime.datetime.now()
    now = str(now).split(".")[0]
    save_path = cwd / ".generated" / f"{now}.html"
    CONSOLE.print("saving output to:",save_path)
    from rich.terminal_theme import TerminalTheme
    CONSOLE.save_html(save_path)
    change_background_of_html(save_path)
    # current_test()

    msg = "END call_command_in_all_folders.py END"
    print()
    print(msg)
    print()
# endregion if __name__ == "__main__": ------------ if __name__ == "__main__":


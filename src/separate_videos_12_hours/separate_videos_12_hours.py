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
import time
import datetime

from natsort import natsorted, ns
from rich.console import Console
from rich.table import Table
from rich.traceback import install
import snoop
install()

CONSOLE = Console(record=True)

# region load_video_infos_csv
# region load_video_infos_csv header
def load_video_infos_csv(
    file_path: str,
    debug_function: bool = None
    ):
# endregion load_video_infos_csv header
# region load_video_infos_csv docstring
    """load the values of a .csv file
    containing the info of all videos
    in the directory

    Args:
        file_path (str): the file path to the file

        debug_function (bool, optional): Defaults to None.

    Returns:
        (list(dict)): the values from .csv file parsed into a dictionary
    """
# endregion load_video_infos_csv docstring
# region load_video_infos_csv implementation
    # debug_function = True # comment to toggle
    video_info_list = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for ordered_dict in csv_reader:
            video_info_list.append(ordered_dict)
    return video_info_list
# endregion load_video_infos_csv implementation
# endregion load_video_infos_csv


# region separate_videos_in_sections
# region separate_videos_in_sections header
# @snoop(watch_explode=['video_data'])
def separate_videos_in_sections(
    video_data_list: list
    ):
# endregion separate_videos_in_sections header
# region separate_videos_in_sections docstring
    """separate the videos in sections of 12 hours or less duration

        43200 seconds == 12 hours
    Args:
        video_data_list (list): the list of video data

    Returns:
        (list) : a list of sections
    """
# endregion separate_videos_in_sections docstring
# region separate_videos_in_sections implementation
    sections = []

    # 12 hours in sections is actually 43200
    # use less to be sure
    _12_hours_in_seconds = 43000
    _12_hours_in_string = "12:00:00"
    acc_duration = 0.0
    section = []
    for index, video_data in enumerate(video_data_list):
        # order = video_data["alphabetical_order"]
        duration = float(video_data["duration_seconds"])
        # dur_h = video_data["duration_hours"]
        # dur_h_obj = time.strptime(dur_h, '%H:%M:%S')
        acc_duration += duration

        acc_dur_h = datetime.timedelta(seconds=acc_duration)

        if acc_duration < _12_hours_in_seconds:
            section.append(index)
            last_index = len(video_data_list) -1
            if index == last_index:
                sections.append(section)
            ...
        else:
            sections.append(section)
            acc_duration = duration
            section = [index]
            last_index = len(video_data_list) -1
            if index == last_index:
                sections.append(section)
            ...
        ...


    return sections
    ...
# endregion separate_videos_in_sections implementation
# endregion separate_videos_in_sections


# region main
# @snoop
def main():
    cwd = Path(os.getcwd())
    print(cwd)
    all_nested_videos = []
    videos_folder_path = cwd / "videos"
    csv_file_path = None

    move_locations = []
    diretories_to_create = []
    videos_folder_exists = os.path.isdir(videos_folder_path)
    if videos_folder_exists:
        all_nested_videos = os.listdir(videos_folder_path)
        csv_file_path = \
            videos_folder_path / ".generated/video_infos.csv"
        csv_file_exists = os.path.isfile(csv_file_path)
        if csv_file_exists:
            video_data_list = load_video_infos_csv(csv_file_path)

            sections = separate_videos_in_sections(video_data_list)

            for index, section in enumerate(sections):
                videos_folder_numbered_path = \
                    Path(str(videos_folder_path) + str(index + 1))
                diretories_to_create.append(videos_folder_numbered_path)
                for index in section:
                    element_data = video_data_list[index]

                    full_path = Path(element_data["full_path"])
                    parent_path = full_path.parent
                    basename = Path(os.path.basename(full_path))
                    src = full_path
                    dst = videos_folder_numbered_path / basename
                    move_locations.append((src, dst))
                    ...
                ...
    else:
        CONSOLE.print()
        CONSOLE.print("[red]There is no videos/ folder[/red]")
        CONSOLE.print()

    for dir in diretories_to_create:
        if not os.path.isdir(dir):
            CONSOLE.print("creating directory:\n{}"\
                .format(dir))
            os.mkdir(dir)
            ...
        else:
            CONSOLE.print("trying to create directory:\n{}"\
                .format(dir))
            CONSOLE.print("directory already exists.", style="bold red")
            ...
        ...
    for loc in move_locations:
        src, dst = loc

        basename = os.path.basename(src)
        print()
        CONSOLE.print("moving \"{}\"\nfrom: \"{}\"\nto:   \"{}\""\
            .format(basename, src, dst))

        os.rename(src, dst)
        ...

# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START concatenate_videos.py START"
    print(msg)
    print()

    try:
        main()
    except:
        CONSOLE.print_exception()

    msg = "END concatenate_videos.py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":


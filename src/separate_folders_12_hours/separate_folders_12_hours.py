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
        csv_file_path = \
            videos_folder_path / ".generated/video_infos.csv"
        csv_file_exists = os.path.isfile(csv_file_path)
        if csv_file_exists:
            video_data_list = load_video_infos_csv(csv_file_path)
            last_index = len(video_data_list) - 1
            last_value = video_data_list[last_index]
            acc_dur_secs = float(last_value["accumulated_duration_seconds"])
            # 12 hours in sections is actually 43200
            # use less to be sure
            _12_hours_in_seconds = 43000.0
            _12_hours_in_string = "12:00:00"
            parent_folder = cwd.parent
            folder_name = cwd.name
            src = cwd
            dst = None
            long_folder = parent_folder / Path("000_long")
            short_folder = parent_folder / Path("000_short")
            if acc_dur_secs >= _12_hours_in_seconds:
                dst = long_folder / folder_name
                if not os.path.isdir(long_folder):
                    os.mkdir(long_folder)
            else:
                dst = short_folder / folder_name
                if not os.path.isdir(short_folder):
                    os.mkdir(short_folder)

            CONSOLE.print("moving:")
            CONSOLE.print("from:")
            CONSOLE.print(src)
            CONSOLE.print("to:")
            CONSOLE.print(dst)
            os.rename(src, dst)
    else:
        CONSOLE.print()
        CONSOLE.print("[red]There is no videos/ folder[/red]")
        CONSOLE.print()
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


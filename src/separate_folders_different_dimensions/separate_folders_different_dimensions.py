#! /usr/bin/env python3
"""
moves this folder to 000_same_dimensions
if all videos in every videos#/ folder
are the same dimension

moves this folder to 000_different_dimensions
if not
"""
# cSpell: word jolitp pytest miliseconds avidemux isdigit
import os
import csv
from pathlib import Path
from collections import Counter

from rich.console import Console
import snoop

ANY_DIFFERENT_DIMMENSION_VIDEO_FOUND = False
CONSOLE = Console()

# region ========================================== load_video_infos_csv
def load_video_infos_csv(file_path: str):
    """load the values of a .csv file
    containing the info of all videos
    in the directory

    Args:
        file_path (str): the file path to the file

        debug_function (bool, optional): Defaults to None.

    Returns:
        (list(dict)): the values from .csv file parsed into a dictionary
    """
    c = Console()
    if not os.path.isfile(file_path):
        return []
    video_info_list = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for ordered_dict in csv_reader:
            video_info_list.append(ordered_dict)

    return video_info_list
# endregion --------------------------------------- load_video_infos_csv


# region filter_dimensions ======================================== filter_dimensions
def filter_dimensions(data_list:list):
    filtered_data = []
    for input_data in data_list:
        width = input_data["width"]
        height = input_data["height"]
        dimensions = (width,height)
        filtered_data.append(dimensions)
    return filtered_data
    ...
# endregion filter_dimensions ------------------------------------ filter_dimensions


# region process_folder ================================================ process_folder
def process_folder(folder_path:Path):
    CONSOLE.print("Processing: {}".format(folder_path))
    print()
    csv_file = folder_path / ".generated/video_infos.csv"
    csv_file_exists = os.path.isfile(csv_file)
    if csv_file_exists:
        videos_data_list = load_video_infos_csv(csv_file)
        dimensions = filter_dimensions(videos_data_list)

        counter = Counter(dimensions)
        number_of_different_dimensions = len(counter)

        if number_of_different_dimensions == 0:
            CONSOLE.print("number_of_different_dimensions == 0")
            CONSOLE.print("[bold red]no videos in path[/]: {}".format(folder_path))
        if number_of_different_dimensions == 1:
            CONSOLE.print("[bold green]All videos in[/]:")
            CONSOLE.print("{}".format(folder_path))
            CONSOLE.print("[bold green]have the same dimensions[/]")
        if number_of_different_dimensions > 1:
            CONSOLE.print("[bold red]videos have different dimensions at path[/]:")
            CONSOLE.print("{}".format(folder_path))
            ANY_DIFFERENT_DIMMENSION_VIDEO_FOUND = True
    else:
        CONSOLE.print("[bold red]no csv file in path:{}[/]".format(csv_file))
# endregion process_folder ---------------------------------------------- process_folder


# region main =========================================================== main
def main():
    cwd = Path(os.getcwd())
    videos_folder_paths = []
    for item in cwd.iterdir():
        item_path = Path(item)
        if item_path.is_dir():
            basename = os.path.basename(item_path)
            if "videos" in basename:
                videos_folder_paths.append(item_path)
    if videos_folder_paths:
        for path in videos_folder_paths:
            process_folder(path)

    src = cwd
    folder_name = cwd.name
    parent_folder = cwd.parent
    same_dim_folder = Path("000_same_dimensions")
    same_dim_folder_abs_path = parent_folder / same_dim_folder
    different_dim_folder = Path("000_different_dimensions")
    different_dim_folder_abs_path = parent_folder / different_dim_folder
    dst = None
    if ANY_DIFFERENT_DIMMENSION_VIDEO_FOUND:
        dst = parent_folder / different_dim_folder / folder_name
        if not os.path.isdir(different_dim_folder_abs_path):
            parent_folder.mkdir(different_dim_folder)
    else:
        dst = parent_folder / same_dim_folder / folder_name
        if not os.path.isdir(same_dim_folder_abs_path):
            parent_folder.mkdir(same_dim_folder)
    CONSOLE.print("[bold red]moving\nfrom:\n{}\nto:\n{}[/]"\
        .format(src, dst))
    # os.rename(src, dst)


# endregion main -------------------------------------------------------- main


# region if __name__ == "__main__": ========== if __name__ == "__main__":
if __name__ == "__main__":
    main()

# endregion if __name__ == "__main__": ------- if __name__ == "__main__":



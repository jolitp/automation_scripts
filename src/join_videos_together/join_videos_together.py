#! /usr/bin/env python3
"""
concatenate(join) videos together using avidemux
"""
# cSpell: word jolitp pytest miliseconds avidemux isdigit
import os
import csv
from pathlib import Path
import subprocess
import sys

from rich.console import Console
import cv2

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
    if not os.path.isfile(file_path):
        return []
        ...
    video_info_list = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for ordered_dict in csv_reader:
            video_info_list.append(ordered_dict)

    return video_info_list
    ...
# endregion --------------------------------------- load_video_infos_csv


# region =========================================== create_project_file
def create_project_file(
    file_path:str,
    video_info_list:list,
):
    """create a file named project.py on the specified file path

    Args:
        file_path (str): the path of the file, to be created

        video_info_list (list):
            the information on each video to be put into the project file

        debug_function (bool, optional): Defaults to None.
    """
    c = Console()

    def project_py_lines(video_info_list:list):
        lines = ""
        lines += "#PY  <- Needed to identify #\n"
        lines += "#--automatically built--\n\n"
        lines += "adm = Avidemux()\n"

        for index, video_info in enumerate(video_info_list):
            cwd = os.getcwd()
            video_path = cwd + "/" + video_info["full_path"]
            if index == 0:
                lines += \
                f"if not adm.loadVideo(\"{video_path}\"):\n" + \
                f"    raise(\"Cannot load {video_path}\")\n"
            else:
                lines += \
                f"if not adm.appendVideo(\"{video_path}\"):\n" + \
                f"    raise(\"Cannot append {video_path}\")\n"
        lines += "adm.videoCodec(\"Copy\")\n"
        lines += "adm.audioCodec(0, \"copy\")\n"
        lines += "adm.setContainer(\"MKV\")\n"

        print(lines)
        return lines

    lines = project_py_lines(video_info_list)

    # print(lines)

    with open(file_path, "w") as output_file:
        c.print("\ncreating project file at: \n\"{}\"\n".format(file_path))
        output_file.write(lines)
# endregion ----------------------------------------- create_project_file


# region ===================================== compare_concatenated_video
def compare_concatenated_video(
    concatenated_video_path: str,
    last_video_info: dict,
):
    expected_duration = int(
        float(last_video_info["accumulated_duration_seconds"]))

    capture = cv2.VideoCapture(concatenated_video_path)
    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_in_sec = 0
    if frame_count:
        duration_in_sec = frame_count/fps

    concatenated_video_duration = int(duration_in_sec)

    return concatenated_video_duration == expected_duration
# endregion ---------------------------------- compare_concatenated_video


# region ================================================ process_folder
def process_folder(folder_path:Path):
    c = Console()
    c.print("\nprocessing folder: \n\"{}\"\n".format(folder_path))

    folder_basename = os.path.basename(folder_path)
    folder_number = ''
    if str(folder_path)[-1].isdigit():
        if "videos" in folder_basename:
            only_number = folder_basename.replace("videos", "")
            folder_number = int(only_number)
        elif "converted" in folder_basename:
            only_number = folder_basename.replace("converted", "")
            folder_number = int(only_number)

    csv_file = folder_path / ".generated/video_infos.csv"

    videos_data_list = load_video_infos_csv(csv_file)

    cwd = Path(os.getcwd())

    if folder_number == "":
        project_file_path = cwd / "project.py"
        file_name = os.path.basename(cwd) + ".mkv"
    if isinstance(folder_number, int):
        project_file_path = cwd / "project {}.py".format(folder_number)
        file_name = os.path.basename(cwd) + " " + str(folder_number) + ".mkv"

    create_project_file(project_file_path, videos_data_list)

    concatenated_video_path = cwd / Path(file_name)
    avidemux_path = "/home/jolitp/Applications/avidemuxLinux.appImage"
    command = [
        avidemux_path,
        "--run",
        project_file_path,
        "--quit",
        "--save",
        concatenated_video_path,
    ]

    subprocess.run(
        command,
        capture_output=True,
        text=True
        ) # comment to test
# endregion ---------------------------------------------- process_folder


# region =========================================================== main
def main():
    cwd = Path(os.getcwd())

    c = Console()

    converted_folder_paths = []
    videos_folder_paths = []
    for item in cwd.iterdir():
        item_path = Path(item)
        if item_path.is_dir():
            basename = os.path.basename(item_path)
            if "videos" in basename:
                videos_folder_paths.append(item_path)
            if "converted" in basename:
                converted_folder_paths.append(item_path)

    if converted_folder_paths:
        c.print("found \"converted\" folders")
        for path in converted_folder_paths:
            c.print("\"{}\"".format(path))
            process_folder(path)

    if videos_folder_paths and not converted_folder_paths:
        c.print("found \"videos\" folders")
        for path in videos_folder_paths:
            c.print("\"{}\"".format(path))
            process_folder(path)

#     last_video_info = video_info_list[len(video_info_list) - 1]
#     # for key in last_video_info:
#     #     print(key ,"=", last_video_info[key])

#     # TODO check if concatenated video exists

#     if not os.path.exists(concatenated_video_path):
#         with open(concatenated_video_path, "w") as file:
#             file.write("an error has ocurred")

#     concatenate_video_okay \
#         = compare_concatenated_video(
#             concatenated_video_path,
#             last_video_info
#         )

#     this_folder_path = Path(cwd)
#     parent_folder = this_folder_path.parent
#     this_folder_name = os.path.basename(cwd)

# # TODO move folder to directory

#     directory_ok = Path(parent_folder / "000_converted")
#     if not os.path.exists(directory_ok):
#         os.mkdir(directory_ok)

#     directory_error = Path(parent_folder / "000_error")
#     if not os.path.exists(directory_error):
#         os.mkdir(directory_error)

#     concatenate_video_okay = False
#     src = cwd
#     if concatenate_video_okay:
#         dst = directory_ok / this_folder_name
#     else:
#         dst = directory_error / this_folder_name

#     print("moving: ")
#     print("src = " + str(src))
#     print("dst = " + str(dst))

#     os.rename(src, dst)
# endregion -------------------------------------------------------- main


# region ===================================== if __name__ == "__main__":
if __name__ == "__main__":
    main()
# endregion ---------------------------------- if __name__ == "__main__":

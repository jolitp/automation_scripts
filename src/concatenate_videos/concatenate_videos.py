#! /usr/bin/env python3
"""
concatenate(join) videos together using avidemux
"""
# cSpell: word jolitp pytest miliseconds avidemux isdigit
import os
import csv
import datetime
import calendar
import concurrent.futures
import subprocess
from pathlib import Path

from natsort import natsorted, ns
from rich.console import Console
import cv2

# region ========================================== load_video_infos_csv
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

    # if debug_function:
    #     print()
    #     print("START load_video_infos_csv")
    #     print("---------=---------=---------=---------=---------=---------=---------=---------=")
    #     print("| def load_video_infos_csv(                                                    |")
    #     print(f"|   file_path = {file_path}")
    #     print("|                                                                              |")

    if not os.path.isfile(file_path):
        return []
        ...
    video_info_list = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for ordered_dict in csv_reader:
            video_info_list.append(ordered_dict)


    # if debug_function:
    #     print()
    #     print("return video_infos = [                                                         |")
    #     for element in video_info_list:
    #         print("|   {                                                                          |")
    #         for key in element:
    #             print(f"|     '{key}': {element[key]}")
    #         print("|   }                                                                          |")
    #     print("|  ]")
    #     print("| }                                                                            |")
    #     print("---------=---------=---------=---------=---------=---------=---------=---------=")
    #     print("END   load_video_infos_csv")
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
        # lines += "# cSpell: word adm jolitp\n"
        lines += "adm = Avidemux()\n"

        for index, video_info in enumerate(video_info_list):
            video_path = video_info["full_path"]
            if index == 0:
                lines += \
                f"if not adm.loadVideo(\"{video_path}\"):\n" + \
                f"    raise(\"Cannot load {video_path}\")\n"
            else:
                lines += \
                f"if not adm.appendVideo(\"{video_path}\"):\n" + \
                f"    raise(\"Cannot append {video_path}\")\n"
        # lets try not aditing this
        # lines += "adm.clearSegments()\n"
        for video_info in video_info_list:
            order = video_info["alphabetical_order"]
            frame_count = video_info["frame_count"]
            # the number passed to the 3rd parameter
            # is not the frame count
            # the documentation says it's duration
            # the number given: 191668
            # is actually 191 seconds
            miliseconds = int(float(video_info["duration_seconds"]) * 1000)
            # print(miliseconds)
            # lines += f"adm.addSegment({order}, 0, {miliseconds})\n"
            # print()
            # for key in video_info:
            #     print(f'{key} : {video_info[key]}')
            # print()
        # lines += "adm.markerA = 0\n"
        acc_dur_sec = 0
        if video_info_list:
            last_video_info = len(video_info_list) -1
        # acc_frame_count = video_info_list[last_video_info]["accumulated_frame_count"]
            acc_dur_sec = video_info_list[last_video_info]["accumulated_duration_seconds"]
        # change here too, it's not frame count
        # it's accumulated duration in miliseconds
        # lines += f"adm.markerB = {acc_frame_count}\n"
        # lines += f"adm.markerB = {int(float(acc_dur_sec) * 1000)}\n"
        lines += "adm.videoCodec(\"Copy\")\n"
        # lines += "adm.audioClearTracks()\n"
        # do I need this?
        # lines += "adm.setSourceTrackLanguage(0, \"und\")\n"
        # lines += "if adm.audioTotalTracksCount() <= 0:\n"
        # lines += "    raise(\"Cannot add audio track 0, total tracks: \" + str(adm.audioTotalTracksCount()))\n"
        # lines += "adm.audioAddTrack(0)\n"
        lines += "adm.audioCodec(0, \"copy\")\n"
        # lines += "adm.audioSetDrc(0, 0)\n"
        # lines += "adm.audioSetShift(0, 0, 0)\n"
        lines += "adm.setContainer(\"MKV\")\n"

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
    c.print("\nprocessing folder: \n{}\n".format(folder_path))

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

    # print(folder_number)
    concatenated_video_path = cwd / Path(file_name)
    avidemux_path = "/home/jolitp/Applications/avidemuxLinux.appImage"
    command = [
        avidemux_path,
        "--run",
        project_file_path,
        "--quit",
        "--save",
        concatenated_video_path
    ]

    c.print("\njoining videos together: \n[bold purple]{}[/]\n" \
        .format(concatenated_video_path))
    # subprocess.run(command) # comment to test
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
            process_folder(path)

    if videos_folder_paths and not converted_folder_paths:
        for path in videos_folder_paths:
            process_folder(path)



    # videos_folder_path = cwd + "/videos/"
    # converted_folder_path = cwd + "/converted/"

    # is_videos_folder = os.path.isdir(videos_folder_path)
    # is_converted_folder = os.path.isdir(converted_folder_path)

    # TODO call process function for each dir that have
    # converted or videos in the name
    # if there are converted don't call videos


    # all_immediate_items = os.listdir(cwd)
    # all_nested_videos = []
    # if is_videos_folder:
    #     all_nested_videos = os.listdir(videos_folder_path)
    # all_converted_videos = []
    # if is_converted_folder:
    #     all_converted_videos = os.listdir(converted_folder_path)


    # videos_infos_csv_file_on_root = cwd + "/.generated/video_infos.csv"
    # videos_infos_csv_file_on_videos = ""
    # if is_videos_folder:
    #     videos_infos_csv_file_on_videos = cwd + "/videos/.generated/video_infos.csv"
    # videos_infos_csv_file_on_converted = ""
    # if is_converted_folder:
    #     videos_infos_csv_file_on_converted = cwd + "/converted/.generated/video_infos.csv"

    # video_info_list = []
    # if is_converted_folder:
    #     video_info_list = load_video_infos_csv(videos_infos_csv_file_on_converted)
    # elif is_videos_folder:
    #     video_info_list = load_video_infos_csv(videos_infos_csv_file_on_videos)
    # else:
    #     video_info_list = load_video_infos_csv(videos_infos_csv_file_on_root)

    # project_file_path = cwd + "/project.py"

    # create_project_file(project_file_path, video_info_list)
    # concatenated_video_path = cwd + "/" + os.path.basename(cwd) + ".mkv"
    # avidemux_path = "/home/jolitp/Applications/avidemuxLinux.appImage"
    # command = [
    #     avidemux_path,
    #     "--run",
    #     project_file_path,
    #     "--quit",
    #     "--save",
    #     concatenated_video_path
    # ]

    # subprocess.run(command) # comment to test

# ====
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
    # print()
    msg = "START concatenate_videos.py START"
    # print(msg)
    # print()

    main()

    # msg = "END concatenate_videos.py END"
    # print()
    # print(msg)
    # print()
    ...
# endregion ---------------------------------- if __name__ == "__main__":

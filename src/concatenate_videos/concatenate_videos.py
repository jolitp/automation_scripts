#! /usr/bin/env python3
"""
concatenate(join) videos together using avidemux
"""
# cSpell: word jolitp pytest miliseconds avidemux
import os
import csv
import datetime
import calendar
import concurrent.futures
import subprocess
from pathlib import Path

from natsort import natsorted, ns
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
# endregion --------------------------------------- load_video_infos_csv


# region =========================================== create_project_file
def create_project_file(
    file_path:str,
    video_info_list:list,
    debug_function:bool = None
):
    """create a file named project.py on the specified file path

    Args:
        file_path (str): the path of the file, to be created

        video_info_list (list):
            the information on each video to be put into the project file

        debug_function (bool, optional): Defaults to None.
    """
    # debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START load_video_infos_csv")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def load_video_infos_csv(                                                    |")
        print(f"|   file_path = {file_path}")
        print("return video_info_list = [                                                         |")
        for element in video_info_list:
            print("|   {                                                                          |")
            for key in element:
                print(f"|     '{key}': {element[key]}")
            print("|   }                                                                          |")
        print("|  ]")
        print("| }                                                                            |")
        print("|                                                                              |")

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
            print(miliseconds)
            # lines += f"adm.addSegment({order}, 0, {miliseconds})\n"
            print()
            for key in video_info:
                print(f'{key} : {video_info[key]}')
            print()
        # lines += "adm.markerA = 0\n"
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

    print(lines)

    with open(file_path, "w") as output_file:
        output_file.write(lines)

    if debug_function:
        print()
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   create_project_file")
# endregion ----------------------------------------- create_project_file


# region ===================================== compare_concatenated_video
def compare_concatenated_video(
    concatenated_video_path: str,
    last_video_info: dict,
    debug_function = None
):
    debug_function = True # comment to toggle

    expected_duration = int(
        float(last_video_info["accumulated_duration_seconds"]))

    if debug_function:
        print()
        print("expected_duration =", expected_duration)
        print()

    capture = cv2.VideoCapture(concatenated_video_path)
    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_in_sec = 0
    if frame_count:
        duration_in_sec = frame_count/fps

    concatenated_video_duration = int(duration_in_sec)

    if debug_function:
        print()
        print("concatenated_video_duration =", concatenated_video_duration )
        print()

    return concatenated_video_duration == expected_duration
# endregion ---------------------------------- compare_concatenated_video


# region =========================================================== main
def main(
    debug_function = None
):
    # debug_function = True # comment to toggle
    cwd = os.getcwd()

    if debug_function:
        print()
        print("current_working_directory:")
        print(cwd)

    videos_folder_path = cwd + "/videos/"
    all_immediate_items = os.listdir(cwd)
    all_nested_videos = os.listdir(videos_folder_path)
    videos_infos_csv_file_on_root = cwd + "/.generated/video_infos.csv"
    videos_infos_csv_file_on_videos = cwd + "/videos/.generated/video_infos.csv"

    if debug_function:
        print()
        print("all_immediate_items = [")
        for element in all_immediate_items:
            print("  {}".format(element))
        print("]")
        print()
        print("all_nested_videos = [")
        for element in all_nested_videos:
            print("  {}".format(element))
        print("]")
        print()
        print("videos_infos_csv_file_on_root:")
        print(videos_infos_csv_file_on_root)
        print()
        print("videos_infos_csv_file_on_videos:")
        print(videos_infos_csv_file_on_videos)

    video_info_list = \
        load_video_infos_csv(videos_infos_csv_file_on_videos)

    project_file_path = cwd + "/project.py"

    create_project_file(project_file_path, video_info_list)

    concatenated_video_path = cwd + "/" + os.path.basename(cwd) + ".mkv"
    avidemux_path = "/home/jolitp/Applications/avidemuxLinux.appImage"
    command = [
        avidemux_path,
        "--run",
        project_file_path,
        "--quit",
        "--save",
        concatenated_video_path
    ]

    # subprocess.run(command) # comment to test

    last_video_info = video_info_list[len(video_info_list) - 1]
    # for key in last_video_info:
    #     print(key ,"=", last_video_info[key])

    # TODO check if concatenated video exists

    if not os.path.exists(concatenated_video_path):
        with open(concatenated_video_path, "w") as file:
            file.write("video was not concatenated")

    # concatenate_video_okay \
    #     = compare_concatenated_video(
    #         concatenated_video_path,
    #         last_video_info
    #     )

    # this_folder_path = Path(cwd)
    # parent_folder = this_folder_path.parent
    # this_folder_name = os.path.basename(cwd)

# TODO move folder to directory

    # directory_ok = Path(parent_folder / "000_converted")
    # if not os.path.exists(directory_ok):
    #     os.mkdir(directory_ok)

    # directory_error = Path(parent_folder / "000_error")
    # if not os.path.exists(directory_error):
    #     os.mkdir(directory_error)

    # concatenate_video_okay = False
    # src = cwd
    # if concatenate_video_okay:
    #     dst = directory_ok / this_folder_name
    # else:
    #     dst = directory_error / this_folder_name

    # print("moving: ")
    # print("src = " + str(src))
    # print("dst = " + str(dst))

    # os.rename(src, dst)

    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   main")
# endregion -------------------------------------------------------- main


# region ===================================== if __name__ == "__main__":
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
# endregion ---------------------------------- if __name__ == "__main__":

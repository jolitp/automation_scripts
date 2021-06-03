#! /usr/bin/env python3
"""
get the information of videos in the videos/ directory
"""
# cSpell: word jolitp pytest miliseconds
import os
import cv2
import csv
import datetime
import calendar
import concurrent.futures

from natsort import natsorted, ns

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
# endregion filter_subtitles


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
# region convert_to_bytes
def convert_to_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
# endregion convert_to_bytes


# TODO put function in a library
# region convert_sec_to_time
def convert_sec_to_time(duration_in_sec: float):
    """converts time in seconds to HH:MM:SS

    Args:
        duration_in_sec (float): duration in seconds

    Returns:
        (str): the time in the format: HH:MM:SS
    """
    hours = int(duration_in_sec/3600)
    remainder = duration_in_sec%3600
    minutes = int(remainder/60)
    seconds = int(duration_in_sec%60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
# endregion convert_sec_to_time


# region get_video_info
def get_video_info(
    video_path:str,
    alphabetical_order: int,
    debug_function = None
    ):
    """get the following information from the video received
    and save it to a dictionary:
    {
        alphabetical_order: the alphabetical order

        filename: the name of the file

        full_path: the full path to the file

        working: if the video can be opened, or if it's not corrupted

        fps: frames per second

        length_seconds: the length of the video in seconds

        length_hours:
            the length of the video in hours:minutes:seconds:miliseconds

        number_of_frames: the total number of frames of the video

        width: the width of the video

        height: the height of the video

        aspect_ratio: the aspect ratio of the video

        aspect_ratio_fraction: the aspect ratio of the video, 16:10, 3:4, etc

        size: the size of the video file in bytes

        size_bytes: the size in a human readable format, in bytes (bytes,Kb, Mb, GB, etc)
    }
    Args:
        video_path (str): the absolute path to the video file

    Return value:
        video_info (dict): the dictionary containing the info
    """
    # debug_function = True  # comment to toggle
    if debug_function:
        print()
        print("START get_info_for_video")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def get_info_for_video(                                                      |")
        print("|   video_path = {}".format(video_path))
        print("| ):                                                                           |")

    info = {}

    capture = cv2.VideoCapture(video_path)
    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_in_sec = 0
    if frame_count:
        duration_in_sec = frame_count/fps
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = os.path.getsize(video_path)

    def gcd_ (a,b):
        if b == 0:
            return a
        return gcd_ (b, a % b)

    aspect_ratio = 0
    if height:
        aspect_ratio = width / height
    gcd = gcd_(height, width)
    try:
        aspect_ratio_fraction = f"{int(width/gcd)}:{int(height/gcd)}"
    except ZeroDivisionError:
        aspect_ratio_fraction = 0

    info["alphabetical_order"] = alphabetical_order
    info["filename"] = os.path.basename(video_path)
    info["full_path"] = video_path
    info["working"] = capture.isOpened()
    info["duration_seconds"] = duration_in_sec
    info["duration_hours"] = convert_sec_to_time(duration_in_sec)
    info["frame_count"] = frame_count
    info["fps"] = int(fps)
    info["width"] = int(width)
    info["height"] = int(height)
    info["size"] = int(size)
    info["size_bytes"] = convert_to_bytes(size)
    info["aspect_ratio_fraction"] = aspect_ratio_fraction
    info["aspect_ratio"] = aspect_ratio

    capture.release()

    if debug_function:
        print("|                                                                              |")
        print("| return info = {                                                              |")
        for element in info:
            print("|   {} : {}".format(element, info[element]))
        print("| }                                                                            |")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   get_info_for_video")

    return info
    ...
# endregion


# region process_folder
def process_folder(
    folder: str,
    debug_function = None
    ):
    """process the videos that are in the root directory

    Args:
        folder (str): the path to the folder to be processed

        immediate_videos (list):
    """
    # debug_function = True # comment to toggle
    if debug_function:
        print()
        print("START process_folder")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def process_folder(                                                      |")
        print("|   folder = {}".format(folder))
        print("| ):                                                                           |")

    all_items = os.listdir(folder)

    if debug_function:
        print()
        print("all_immediate_items = [")
        for element in all_items:
            print("  {}".format(element))
        print("]")

    videos = filter_videos(all_items)
    # videos.sort()
    videos = natsorted(videos, alg=ns.PATH)

    if debug_function:
        print()
        print("immediate_videos = [")
        for element in videos:
            print("  {}".format(element))
        print("]")

    video_paths = []
    for video in videos:
        video_paths.append(folder + "/" + video)

    if debug_function:
        print()
        print("immediate_video_paths = [")
        for element in video_paths:
            print("  {}".format(element))
        print("]")

    # not using multiprocessing
    # video_infos = []
    # for index, video in enumerate(video_paths):
    #     video_infos.append(get_video_info(video, index))
    # video_infos = get_accumulated_values(video_infos)

    # using multiprocessing
    video_infos = [0] * len(video_paths)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # video_infos = executor.map(get_video_info, video_paths)
        ...
        results = []
        for index, item in enumerate(video_paths):
            print(f"index: {index}")
            print(f"item: {item}")
            results.append(executor.submit(get_video_info, item, index))

        # prints the results in the order they are completed
        for result in concurrent.futures.as_completed(results):
            # print(f"restult: {result.result()}")
            video_infos[result.result()["alphabetical_order"]] = result.result()
            ...

    video_infos = get_accumulated_values(video_infos)

    if debug_function:
        print()
        print("video_infos = [")
        for infos in video_infos:
            print()
            for key in infos:
                print("  {} : {}".format(key, infos[key]))
        print("]")

    dot_generated_folder_path = folder + "/.generated"
    if not os.path.exists(dot_generated_folder_path):
        os.mkdir(dot_generated_folder_path)
    create_csv_file(video_infos, folder + "/.generated/video_infos.csv")
    create_org_file(video_infos, folder + "/.generated/video_infos.org")

    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   process_folder")
# endregion process_folder


# region create_org_file
def create_org_file(
    infos_list: dict,
    file_path: str,
    debug_function = None
):
    """
    creates a .org file

    Args:
        infos_list (dict): dictionaries list containing the information for each video

        file_path (str): the path to save the .org file to
    """
    debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START create_org_file")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def create_org_file(                                                      |")
        print()
        print("|   infos_list = [")
        for infos in infos_list:
            print()
            for key in infos:
                print("  {} : {}".format(key, infos[key]))
        print("]")
        print("|   file_path = {}".format(file_path))
        print("| ")
        print("|   opening file: {}".format(file_path))
        print("| ")

    with open(file_path, "w") as output_file:
        folder_name = os.path.basename(os.getcwd())

        time_of_creation = datetime.datetime.now()
        year = time_of_creation.year
        month = time_of_creation.month
        day = time_of_creation.day
        day_abbr = calendar.day_abbr[time_of_creation.weekday()]
        hour = time_of_creation.hour
        minute = time_of_creation.minute

        # the format of the date and time:
        # #+DATE: <2006-11-01 Wed 19:15>
        formatted_date = \
            f'{year:04d}-{month:02d}-{day:02d} {day_abbr} {hour:02d}:{minute:02d}'
        date_line = "#+DATE: <" + formatted_date + ">"

# TODO refactor: remove repetition
        duration_table = ""
        for index, infos in enumerate(infos_list):
            if index == 0:
                duration_table += \
                    "| alpha_ord " + \
                    "| working " + \
                    "| name " + \
                    "| dur_sec " + \
                    "| dur_hrs " + \
                    "| acc_dur_sec " + \
                    "| acc_dur_hrs |\n"

                duration_table += \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| |\n"

            alpha_ord = infos["alphabetical_order"]
            working = infos["working"]
            name = infos["filename"]
            dur_sec = int(infos["duration_seconds"])
            dur_hr = infos["duration_hours"]
            acc_dur_sec = infos["accumulated_duration_seconds"]
            acc_dur_hr = infos["accumulated_duration_hours"]
            duration_table \
                += f"| {alpha_ord}" + \
                    f"| {working}" + \
                    f"| {name}" + \
                    f"| {dur_sec}" + \
                    f"| {dur_hr}" + \
                    f"| {acc_dur_sec:.3f}" + \
                    f"| {acc_dur_hr} | \n"

        frames_table = ""
        for index, infos in enumerate(infos_list):
            if index == 0:
                frames_table += \
                    "| alpha_ord " + \
                    "| working " + \
                    "| name " + \
                    "| fr_count " + \
                    "| fps " + \
                    "| acc_fr_cnt |\n"

                frames_table += \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| |\n"

            alpha_ord = infos["alphabetical_order"]
            name = infos["filename"]
            frame_count = infos["frame_count"]
            fps = infos["fps"]
            acc_frame_count = infos["accumulated_frame_count"]
            frames_table \
                += f"| {alpha_ord}" + \
                    f"| {working}" + \
                    f"| {name}" + \
                    f"| {frame_count}" + \
                    f"| {fps}" + \
                    f"| {acc_frame_count} | \n"

        dimension_table = ""
        for index, infos in enumerate(infos_list):
            if index == 0:
                dimension_table += \
                    "| alpha_ord " + \
                    "| working " + \
                    "| name " + \
                    "| width " + \
                    "| height " + \
                    "| AR " + \
                    "| AR_frc |\n"

                dimension_table += \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| |\n"

            alpha_ord = infos["alphabetical_order"]
            working = infos["working"]
            name = infos["filename"]
            width = infos["width"]
            height = infos["height"]
            a_r = infos["aspect_ratio"]
            a_r_frc = infos["aspect_ratio_fraction"]
            dimension_table \
                += f"| {alpha_ord} | {working} | {name} | {width} | {height} | {a_r:.2f} | {a_r_frc} |\n"
            ...

        size_table = ""
        for index, infos in enumerate(infos_list):
            if index == 0:
                size_table += \
                    "| alpha_ord " + \
                    "| working " + \
                    "| name " + \
                    "| bytes " + \
                    "| acc_bytes |\n"

                size_table += \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| " + \
                    "| |\n"

            alpha_ord = infos["alphabetical_order"]
            working = infos["working"]
            name = infos["filename"]
            size_bytes = infos["size_bytes"]
            acc_size_bytes = infos["accumulated_size_bytes"]
            size_table \
                += f"| {alpha_ord} | {working} | {name} | {size_bytes} | {acc_size_bytes} |\n"
            ...

        output_file.write(f"{date_line} \n")
        output_file.write(f"* {folder_name}\n")
        output_file.write(f"** duration table\n")
        output_file.write(duration_table)
        output_file.write(f"** frames table\n")
        output_file.write(frames_table)
        output_file.write(f"** dimension_table\n")
        output_file.write(dimension_table)
        output_file.write(f"** size_table\n")
        output_file.write(size_table)
        ...

    if debug_function:
        print("|                                                                              |")
        print("| closing file: {}".format(file_path))
        print("|                                                                              |")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   create_org_file")
        print()
    ...
# endregion create_org_file


# region create_csv_file
def create_csv_file(
    infos_list: dict,
    file_path: str,
    debug_function = None
    ):
    """
    creates a .csv file

    Args:
        infos_list (dict): dictionaries list containing the information for each video

        file_path (str): the path to save the .csv file to
    """
    # debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START create_csv_file")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def create_csv_file(                                                      |")
        print()
        print("|   infos_list = [")
        for infos in infos_list:
            print()
            for key in infos:
                print("  {} : {}".format(key, infos[key]))
        print("]")
        print("|   file_path = {}".format(file_path))
        print("| ")
        print("| opening file: {}".format(file_path))

    with open(file_path, "w") as output_file:
        filed_names = [
            "alphabetical_order",
            "working",
            "filename",
            "full_path",
            "duration_seconds",
            "duration_hours",
            "frame_count",
            "fps",
            "width",
            "height",
            "size",
            "size_bytes",
            "aspect_ratio_fraction",
            "aspect_ratio",
            "accumulated_duration_seconds",
            "accumulated_duration_hours",
            "accumulated_frame_count",
            "accumulated_size",
            "accumulated_size_bytes",
        ]

        csv_writer = csv.DictWriter(output_file, fieldnames=filed_names)

        csv_writer.writeheader()

        for row in infos_list:
            csv_writer.writerow(row)

    if debug_function:
        print("| closing file: {}".format(file_path))
        print("| ):                                                                           |")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   create_csv_file")
        print()
    ...
# endregion create_csv_file


# region get_accumulated_values
def get_accumulated_values(
    infos_list: dict,
    debug_function = None
    ):
    """get the accumulated values for:

    duration_seconds,
    duration_hours,
    frame_count,
    size,
    size_bytes,

    Args:
        infos_list (dict): a dictionary containing the infos
    """
    # debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START get_accumulated_values")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def get_accumulated_values(                                                      |")
        print("|   infos_list = [")
        for infos in infos_list:
            print()
            for key in infos:
                print("      {} : {}".format(key, infos[key]))
        print("]")
        print("| ):                                                                           |")

    accumulated_duration_seconds = 0
    # accumulated_duration_hours = convert()
    accumulated_frame_count = 0
    accumulated_size = 0
    # accumulated_size_bytes = convert()
    for infos in infos_list:
        accumulated_duration_seconds += infos["duration_seconds"]
        infos["accumulated_duration_seconds"] = accumulated_duration_seconds
        infos["accumulated_duration_hours"] = \
            convert_sec_to_time(accumulated_duration_seconds)
        accumulated_frame_count += infos["frame_count"]
        infos["accumulated_frame_count"] = accumulated_frame_count
        accumulated_size += infos["size"]
        infos["accumulated_size"] = accumulated_size
        infos["accumulated_size_bytes"] = convert_to_bytes(accumulated_size)

    if debug_function:
        print()
        print("return infos_list = {                                                          |")
        for infos in infos_list:
            print("|                                                                          |")
            for key in infos:
                print("|   {} : {}".format(key, infos[key]))
        print("|  }")
        print("| }                                                                            |")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   get_accumulated_values")

    return infos_list
# endregion get_accumulated_values


# region main
def main(
    debug_function = None
):
    cwd = os.getcwd()

    if debug_function:
        print()
        print("current_working_directory:")
        print(cwd)

    all_immediate_items = os.listdir(cwd)

    if debug_function:
        print()
        print("all_immediate_items = [")
        for element in all_immediate_items:
            print("  {}".format(element))
        print("]")

    immediate_videos = filter_videos(all_immediate_items)
    # immediate_videos.sort()
    immediate_videos = natsorted(immediate_videos, alg=ns.PATH)

    if immediate_videos:
        process_folder(cwd)

    separated_videos = []
    if "videos" in all_immediate_items:
        separated_videos = os.listdir(cwd + "/videos")
    # separated_videos.sort()
    separated_videos = natsorted(separated_videos, alg=ns.PATH)

    if separated_videos:
        process_folder(cwd + "/videos")
        ...

        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   main")


# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START get_videos_info_csv.py START"
    print(msg)
    print()

    main()

    msg = "END get_videos_info_csv.py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":

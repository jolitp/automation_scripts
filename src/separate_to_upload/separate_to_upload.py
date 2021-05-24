#! /usr/bin/env python3
"""
checks wether or the folder this script is called in
have 15 videos or less, if so move the volder to:
YT_upload_to_youtube/
if there are more than 15 videos, move to:
separate_12_hours/
"""
# cSpell: word jolitp pytest miliseconds
import os
import sys
from pathlib import Path

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


# region process_folder
def process_folder(
    folder_path:Path,
    debug_function=None,
):
    """process the videos that are in the root directory

    Args:
        folder_path (str): the path to the folder to be processed

        immediate_videos (list):
    """
    debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START process_folder")
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("| def process_folder(                                                      |")
        print("|   folder = {}".format(folder_path))
        print("| ):                                                                           |")



    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   process_folder")
# endregion process_folder


# region main
def main(
    debug_function = None
):
    debug_function = True # comment to toggle

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

    if debug_function:
        print()
        print("immediate_videos = [")
        for element in immediate_videos:
            print("  {}".format(element))
        print("]")

    immediate_videos_length = len(immediate_videos)

    if debug_function:
        print()
        print(f"immediate_videos_length = {immediate_videos_length}")
        print()

    separated_videos = []
    if os.path.isdir(cwd + "/videos/"):
        separated_videos = os.listdir(cwd + "/videos")
    separated_videos = natsorted(separated_videos, alg=ns.PATH)

    if debug_function:
        print()
        print("separated_videos = [")
        for element in separated_videos:
            print("  {}".format(element))
        print("]")

    separated_videos_length = len(separated_videos)

    if debug_function:
        print()
        print(f"separated_videos_length = {separated_videos_length}")
        print()

    how_many_videos:int = immediate_videos_length + separated_videos_length
    _15_or_less_videos: bool = False

    if debug_function:
        print()
        print(f"how_many_videos = {how_many_videos}")
        print()

    if how_many_videos <= 15:
        _15_or_less_videos = True

    no_videos_found:bool = False
    if how_many_videos == 0:
        no_videos_found = True

    if debug_function:
        print()
        print(f"no_videos_found = {no_videos_found}")
        print()

    parent_dir = Path(cwd).parent
    this_dir_name = os.path.basename(Path(cwd))

    if _15_or_less_videos:
        src = cwd
        dst = parent_dir / "0000_YT_upload_to_youtube" / this_dir_name

        if not os.path.isdir(parent_dir / "0000_YT_upload_to_youtube"):
            os.mkdir(parent_dir / "0000_YT_upload_to_youtube")
        if not os.path.isdir(dst):
            os.mkdir(dst)
    else:
        src = cwd
        dst = parent_dir / "0000_separate_12_hours" / this_dir_name

        if not os.path.isdir(parent_dir / "0000_separate_12_hours"):
            os.mkdir(parent_dir / "0000_separate_12_hours")
        if not os.path.isdir(dst):
            os.mkdir(dst)

    if no_videos_found:
        print()
        print("no videos found.")
        print()
        src = cwd
        dst = parent_dir / "0000_no_videos_found" / this_dir_name

        if not os.path.isdir(parent_dir / "0000_no_videos_found"):
            os.mkdir(parent_dir / "0000_no_videos_found")
        if not os.path.isdir(dst):
            os.mkdir(dst)

    print(f"moving directory: {this_dir_name}")
    print(f"form: {src}")
    print(f"to: {dst}")
    # os.rename(src, dst)

    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   main")
# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START .py START"
    print(msg)
    print()

    main()

    msg = "END .py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":


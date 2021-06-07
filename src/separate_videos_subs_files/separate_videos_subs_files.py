#! /usr/bin/env python3
"""
separate files into folders:

videos/
subs/
files/
folders/
"""
# FIXME it is working on laptop
# BUG not getting any files in a real directory
# the cwd is the right one

# TODO move remaining folders to folders/ dolder
# TODO ignore videos/ subs/ files/ folders/

# TODO make the print statements colored using the rich package
# TODO install rich traceback

import os
import os.path
from pathlib import Path

from rich.console import Console
from rich.traceback import install as install_rich_traceback
import snoop

CONSOLE = Console()
install_rich_traceback()

# TODO put function in a library
# TODO make a non recursive version, to be used by parameters
# region get_nested_files
def get_nested_files(
    path: str
):
    """
    gets the nested files in the directory recursively

    Args:
        path (str):
            the path to the folder to get the files
            defaults to current working directory.

    Returns:
        nested_files (list(str)):
            a list of paths containing the absolute path to each file.
    """
    nested_files = []
    for root, _, files in os.walk(path, topdown=False):
        for name in files:
            full_path = (os.path.join(root, name))
            nested_files.append(full_path)
    return nested_files
# endregion get_nested_files


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


# region filter_folders ================================= filter_folders
def get_all_folders(path:str):
    nested_folders = []
    for root, folders, _ in os.walk(path, topdown=False):
        for name in folders:
            full_path = (os.path.join(root, name))
            nested_folders.append(full_path)
    return nested_folders
    ...
# endregion filter_folders ------------------------------ filter_folders


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
# region ignore_project_files ======================= ignore_project_files
def ignore_project_files(files: list):
    """remove the files that should
    only be present on the project folder

    Args:
        files (list): the list of files in the directory

    Returns:
        remaining_files (list): the remaining files
    """
    #cSpell: words pytest
    ignored_items = {
        "__pycache__": [],
        "test_bed": [],
        ".pytest_cache": [],
        "separate_videos_subs_files.py": [],
        "test_separate_videos_subs_files.py": [],
        "/videos/": [],
        "/subs/": [],
        "/files/": [],
        "/folders/": [],
    }
    c = Console()
    # not_ignored_files = [x for x in files if x not in ignored_items]
    for key in ignored_items:
        for file in files:
            if key in file:
                ignored_items[key].append(file)

    # CONSOLE.print(ignored_items)

    for key in ignored_items:
        for item in ignored_items[key]:
            if item in files:
                files.remove(item)

    return files
# endregion ignore_project_files ------------------- ignore_project_files


# region print_list ======================================== print_list
def print_list(list_name:str,list:list):
    c = Console()
    print()
    print(f"{list_name} = [")
    for element in list:
        CONSOLE.print("  {}".format(element))
    print("]")
    print()
# endregion print_list ------------------------------------- print_list


# region print_src_dst_paths ============================ print_src_dst_paths
def print_src_dst_paths(name:str, src_dst_paths:dict):
    c = Console()
    print()
    print(f"{name} = [")
    for element in src_dst_paths:
        print()
        CONSOLE.print("  'name': {}".format(element["name"]))
        CONSOLE.print("  'src': {}".format(element["src"]))
        CONSOLE.print("  'dst': {}".format(element["dst"]))
        print()
    print("]")
    print()
# endregion ----------------------------------------------- print_src_dst_paths


# region create_folder =========================================== create_folder
def create_folder(path_to_directory:str):
    c = Console()
    p = Path(path_to_directory)
    if not p.exists():
        CONSOLE.print("creating directory:\n{}" \
            .format(add_color("bold #00ff00",str(path_to_directory))))
        p.mkdir(exist_ok=True, parents=True)
    else:
        CONSOLE.print("directory already exists at path: \n{}" \
            .format(add_color("bold #ff0000",str(path_to_directory))))
    return p
# endregion create_folder ------------------------------------------- create_folder


# region get_src_dst_paths ============================== get_src_dst_paths
def get_src_dst_paths(name:str, files:list):
    cwd = Path(os.getcwd())
    files_src_dst_paths = []
    for nested_files_file_path in files:
        nested_files_file_path:Path = nested_files_file_path
        path_string_without_cwd = str(nested_files_file_path).replace(str(cwd), "")
        path_string_without_cwd = path_string_without_cwd.replace("/", "...")
        if path_string_without_cwd.startswith("..."):
            path_string_without_cwd = path_string_without_cwd[3:]
        file_destination_path = cwd / Path(name) / Path(path_string_without_cwd)
        paths = {
            "name": Path(os.path.basename(nested_files_file_path)),
            "src": Path(nested_files_file_path),
            "dst": Path(file_destination_path)
        }
        files_src_dst_paths.append(paths)
    return files_src_dst_paths
# endregion get_src_dst_paths ------------------------------- get_src_dst_paths


# region delete_folders ================================== delete_folders
def delete_folders(folder_list:list):
    for folder in folder_list:
        os.rmdir(folder)
# endregion delete_folders ------------------------------- delete_folders


# region
# @snoop
def filter_folders():
    cwd = Path(os.getcwd())
    nested_folders = get_all_folders(cwd)
    nested_folders = ignore_project_files(nested_folders)

    for folder in nested_folders:
        basename = os.path.basename(folder)
        ignored_names = ["videos","subs","files","folders"]
        for name in ignored_names:
            if name == basename:
                nested_folders.remove(folder)
    nested_folders = ignore_project_files(nested_folders)
    return nested_folders
# endregion


# region move_files_from_list ========================== move_files_from_list
def move_files_from_list(folder_name:str, file_list:list):
    c = Console()
    cwd = Path(os.getcwd())
    create_folder(cwd / folder_name)
    for video in get_src_dst_paths(folder_name, file_list):
        CONSOLE.print("moving: {}".format(video["name"]))
        os.rename(video["src"], video["dst"])
    ...
# endregion move_files_from_list -------------------------- move_files_from_list


# region move_folders_from_list ========================= move_folders_from_list
def move_folders_from_list(folder_name:str,folders_list:list):
    c = Console()
    cwd = Path(os.getcwd())
    create_folder(cwd / "folders")
    folders_src_dst_paths = get_src_dst_paths("folders", folders_list)
    # filter out created folders
    for folder_data in folders_src_dst_paths:
        if folder_data["name"] == Path("folders"):
            folders_src_dst_paths.remove(folder_data)
        if folder_data["name"] == Path("subs"):
            folders_src_dst_paths.remove(folder_data)
        if folder_data["name"] == Path("videos"):
            folders_src_dst_paths.remove(folder_data)
        if folder_data["name"] == Path("files"):
            folders_src_dst_paths.remove(folder_data)
    # create destination folders
    src_folders = []
    dst_folders = []
    extraneous_folders = []
    for folder_data in folders_src_dst_paths:
        dst_folder = folder_data["dst"]
        # create_folder(dst_folder)
        if "folders" == os.path.basename(dst_folder):
            continue
        src_folders.append(folder_data["src"])
        dst_folders.append(folder_data["dst"])
        if "..." in str(dst_folder):
            extraneous_folders.append(dst_folder)
    dst_folders = sorted(dst_folders)
    for dst in dst_folders:
        # TODO create dst folders
        create_folder(dst)
        ...
    src_folders = sorted(src_folders,reverse=True)
    for src in src_folders:
        src: Path = src
        # TODO remove src folder
        src.rmdir()
        ...
    # delete source folders and extraneous
    # delete_folders(src_folders)
    delete_folders(extraneous_folders)
# endregion move_folders_from_list ---------------------- move_folders_from_list


# region main
def main():
    cwd = Path(os.getcwd())
    c = Console()
    CONSOLE.print("cwd:", cwd)
    print()

    all_nested_files = get_nested_files(cwd)
    all_nested_files = ignore_project_files(all_nested_files)

    nested_videos = filter_videos(all_nested_files)
    nested_subtitles = filter_subtitles(all_nested_files)
    files_wo_videos \
        = [x for x in all_nested_files if x not in nested_videos]
    files_wo_videos_and_subtitles \
        = [x for x in files_wo_videos if x not in nested_subtitles]
    remaining_files = files_wo_videos_and_subtitles
    nested_folders = filter_folders()

    if nested_videos:
        move_files_from_list("videos", nested_videos)
    if nested_subtitles:
        move_files_from_list("subs", nested_subtitles)
    if remaining_files:
        move_files_from_list("files", remaining_files)
    if nested_folders:
        move_folders_from_list("folders", nested_folders)

    # TODO print the directory structure with colors for each type of file
    # use this tutorial to make the tree structure:
    # https://realpython.com/directory-tree-generator-python/
    # TODO write a file with a summary of how many files were moved
    # write the tree printed earlier
# endregion main


# TODO add to function library
# region add_color =========================================== add_color
def add_color(color, msg):
    return "[" + color + "]" + msg + "[/]"
# endregion add_color ---------------------------------------- add_color


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START separate_videos_subs_files START"
    print(msg)
    print()

    main()

    msg = "END separate_videos_subs_files END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":

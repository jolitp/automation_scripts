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
# region ignore_project_files
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
    }

    not_ignored_files = [x for x in files if x not in ignored_items]
    for key in ignored_items:
        for file in files:
            if key in file:
                ignored_items[key].append(file)

    # print()
    # print("  ignored_items = {")
    # for key in ignored_items:
    #     print("    {}: ".format(key))
    #     for item in ignored_items[key]:
    #         print("      {}".format(item))
    # print("  }")
    # print()

    for key in ignored_items:
        for item in ignored_items[key]:
            if item in files:
                files.remove(item)

    return files
# endregion


# region main
def main():
    cwd = os.getcwd()
    print()
    print("current_working_directory:")
    print(cwd)
    print()

# TODO refactor repetitive statements

    all_nested_files = get_nested_files(cwd)
    all_nested_files = ignore_project_files(all_nested_files)

    print()
    print("all_nested_files = [")
    for element in all_nested_files:
        print("  {}".format(element))
    print("]")
    print()

    nested_videos = filter_videos(all_nested_files)

    print()
    print("nested_videos = [")
    for element in nested_videos:
        print("  {}".format(element))
    print("]")
    print()

    nested_subtitles = filter_subtitles(all_nested_files)

    print()
    print("nested_subtitles = [")
    for element in nested_subtitles:
        print("  {}".format(element))
    print("]")
    print()

    files_wo_videos \
        = [x for x in all_nested_files if x not in nested_videos]

    files_wo_videos_and_subtitles \
        = [x for x in files_wo_videos if x not in nested_subtitles]

    print()
    print("files w/o videos and subtitles = [")
    for element in files_wo_videos_and_subtitles:
        print("  {}".format(element))
    print("]")
    print()

    remaining_files = files_wo_videos_and_subtitles

    if nested_videos:
        videos_dir_path = cwd + "/videos/"
        if not os.path.isdir(videos_dir_path):
            print("creating directory: {}".format(videos_dir_path))
            os.mkdir(videos_dir_path)

    if nested_subtitles:
        subtitles_dir_path = cwd + "/subs/"
        if not os.path.isdir(subtitles_dir_path):
            print("creating directory: {}".format(subtitles_dir_path))
            os.mkdir(subtitles_dir_path)

    if remaining_files:
        remaining_files_dir_path = cwd + "/files/"
        if not os.path.isdir(remaining_files_dir_path):
            print("creating directory: {}".format(remaining_files_dir_path))
            os.mkdir(remaining_files_dir_path)

    files_src_dst_paths = []
    for nested_files_file_path in remaining_files:
        nested_files_file_path: str = nested_files_file_path
        path_wo_cwd = nested_files_file_path.replace(cwd, "")
        path_wo_cwd = path_wo_cwd.replace("/", "...")
        if path_wo_cwd.startswith("..."):
            path_wo_cwd = path_wo_cwd[3:]
        file_destination_path = cwd + "/files/" + path_wo_cwd
        src_str = {
            "name": os.path.basename(nested_files_file_path),
            "src": nested_files_file_path,
            "dst": file_destination_path
        }
        files_src_dst_paths.append(src_str)

    print()
    print("file_src_dst_paths = [")
    for element in files_src_dst_paths:
        print()
        print("  'name': {}".format(element["name"]))
        print("  'src': {}".format(element["src"]))
        print("  'dst': {}".format(element["dst"]))
        print()
    print("]")
    print()

    subtitles_src_dst_paths = []
    for nested_subtitle_file_path in nested_subtitles:
        nested_subtitle_file_path: str = nested_subtitle_file_path
        path_wo_cwd = nested_subtitle_file_path.replace(cwd, "")
        path_wo_cwd = path_wo_cwd.replace("/", "...")
        if path_wo_cwd.startswith("..."):
            path_wo_cwd = path_wo_cwd[3:]
        subtitle_destination_path = cwd + "/subs/" + path_wo_cwd
        src_str = {
            "name": os.path.basename(nested_subtitle_file_path),
            "src": nested_subtitle_file_path,
            "dst": subtitle_destination_path
        }
        subtitles_src_dst_paths.append(src_str)

    print()
    print("subtitles_src_dst_paths = [")
    for element in subtitles_src_dst_paths:
        print()
        print("  'name': {}".format(element["name"]))
        print("  'src': {}".format(element["src"]))
        print("  'dst': {}".format(element["dst"]))
        print()
    print("]")
    print()

    videos_src_dst_paths = []
    for nested_video_file_path in nested_videos:
        nested_video_file_path: str = nested_video_file_path
        path_wo_cwd = nested_video_file_path.replace(cwd, "")
        path_wo_cwd = path_wo_cwd.replace("/", "...")
        if path_wo_cwd.startswith("..."):
            path_wo_cwd = path_wo_cwd[3:]
        video_destination_path = cwd + "/videos/" + path_wo_cwd
        src_str = {
            "name": os.path.basename(nested_video_file_path),
            "src": nested_video_file_path,
            "dst": video_destination_path
        }
        videos_src_dst_paths.append(src_str)

    print()
    print("videos_src_dst_paths = [")
    for element in videos_src_dst_paths:
        print()
        print("  'name': {}".format(element["name"]))
        print("  'src': {}".format(element["src"]))
        print("  'dst': {}".format(element["dst"]))
        print()
    print("]")
    print()

    for video in videos_src_dst_paths:
        print("moving: {}".format(video["name"]))
        os.rename(video["src"], video["dst"])

    for subtitle in subtitles_src_dst_paths:
        print("moving: {}".format(subtitle["name"]))
        os.rename(subtitle["src"], subtitle["dst"])

    for file in files_src_dst_paths:
        print("moving: {}".format(file["name"]))
        os.rename(file["src"], file["dst"])
# endregion main


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

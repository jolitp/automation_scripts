#! /usr/bin/python3
"""
    measures how much a folder of videos is worth it to be uploaded to youtube
    without being concatenated into smaller videos.

    creates a file named: []
"""

import os


def is_folder(root: str,
                name: str):
    """returns wether or not an item in a directory is a folder

    Args:
        item (str):

    Returns:
        bool: if item is folder or not
    """
    # region def is_folder(item: str):
    full_path = root + name
    if not os.path.isabs(full_path):
        raise ValueError("the path must be an absolute path.")
    is_it_folder : bool = False
    if os.path.isdir(full_path):
        is_it_folder = True
        ...
    return is_it_folder
    ...
# endregion def is_folder(item: str):



def filter_folders(root: str,
                    all_files_and_folders: list,
                    debug_function: bool = False) -> None:
    """returns wether or not an item in a directory is a folder

    Args:
        item (str): the item to check

    Returns:
        bool: if item is folder or not
    """
# region def filter_folders(all_files_and_folders: list):

# region debug_function
    if debug_function:
        print("> [def] process_folder(...)")
        print("> all_files_and_folders: list = {}".format(all_files_and_folders))
        print("> {")
# endregion
    only_folders : list = []
    for item in all_files_and_folders:
        if is_folder(root, item):
            only_folders.append(item)
        ...
# region debug_function
    if debug_function:
        print("> }")
# endregion
    return only_folders
# endregion def filter_folders(all_files_and_folders: list):


def process_folder(root: str,
                    folder: str,
                    debug_function: bool = False) -> None:
    """process each folder passed to it

    Args:
        root (str): the root folder(where the script was called)
        folder (str): the folder to be processed
        debug_function (bool, optional): if function should be debugged. Defaults to False.

    Returns:
        None
    """
# region def process_folder(...):
# region debug_function
    if debug_function:
        print("> [def] process_folder(...)")
        print("> root: str = {}".format(root))
        print("> folder: str = {}".format(folder))
        print("> {")
# endregion

# TODO get the number of videos in the folder
# delegate it to the is_file_video.py.is_video

# TODO get the size of each video

# TODO get the length of each video?
# delegate it to the video_length.py.get_length


# region debug_function
    if debug_function:
        print("> }")
# endregion
    ...
# endregion def process_folder(...):


def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)

# region debug_function
    if debug_function:
        print("[def] main()")
        print("{")
# endregion
    current_directory_path = os.getcwd()
    all_files_and_folders = os.listdir(current_directory_path)
    folders = filter_folders(current_directory_path, all_files_and_folders)

# TODO parallelize the execution of each folder using subprocess
    for folder in folders:
        process_folder(current_directory_path, folder,debug_function=True)

# region debug_function
    if debug_function:
        print("}")
# endregion
# endregion def main(...)


# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    print()
    print("youtube_upload_viability_without_concatenating.py.__main__ : START")
    print()
    main(debug_function = debug_script)
    print()
    print("youtube_upload_viability_without_concatenating.py.__main__ : END")
    print()
# endregion if __name__ == "__main__":

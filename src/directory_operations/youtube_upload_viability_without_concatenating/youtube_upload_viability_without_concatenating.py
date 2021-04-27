#! /usr/bin/python3
"""
    measures how viable each folder is to be uploaded to youtube
"""

import os
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "/src/multiple_files_operations/get_all_videos_in_a_directory/"
spec = importlib.util.spec_from_file_location("get_all_videos_in_a_directory",
    python_scripts_folder_path + subfolder + "get_all_videos_in_a_directory.py")
get_all_videos_in_a_directory_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_all_videos_in_a_directory_script)


def is_viable(videos : list,
            debug_function=False):
    """process each folder passed to it

    Args:
        videos (list):
            a list of videos inside a directory
        debug_function (bool, optional):
            if function should be debugged. Defaults to False.

    Returns:
        viability (float):
            a measure of how viable this folder is to be uploaded
    """
    # debug_function = True # comment to toggle
    viability : float = 0

    number_of_videos = len(videos)
    if number_of_videos < 16:
        viability = 1

# TODO get the size of each video

# TODO get the length of each video?
# delegate it to the video_length.py.get_length

    return viability
    ...

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
    # debug_function = True # comment to toggle
# region debug_function
    if debug_function:
        print()
        print("> [def] process_folder(...)")
        print("> root: str = {}".format(root))
        print("> folder: str = {}".format(folder))
        print("> {")
        print()
# endregion
    cwd = os.getcwd()
# region debug_function
    if debug_function:
        print()
        print("> cwd: str = {}".format(cwd))
        print()
# endregion
    videos : list = get_all_videos_in_a_directory_script \
        .get_all_videos(root + folder)
# region debug_function
    if debug_function:
        print()
        print("> > videos : list = [")
        for debug_index, debug_item in enumerate(videos):
            print("> > videos[{}] = {}".format(debug_index, debug_item))
        print("]")
        print()
# endregion
    how_viable = is_viable(videos)
# TODO move folder to subfolder

    upload_now_folder_name = "[upload_now]"

    os.chdir(root)
    cwd = os.getcwd()
# region debug_function
    if debug_function:
        print()
        print("> cwd: str = {}".format(cwd))
        print()
# endregion
    if not os.path.isdir(upload_now_folder_name):
        os.mkdir(upload_now_folder_name)

    if how_viable == 1:
        source_path = root + folder
        destination_path = root + upload_now_folder_name + "/" + folder
# region debug_function
    if debug_function:
        print()
        print("> source_path: str = {}".format(source_path))
        print()
        print("> destination_path: str = {}".format(destination_path))
        print()
# endregion
        os.rename(source_path, destination_path)
    os.chdir(cwd)
    cwd = os.getcwd()
# region debug_function
    if debug_function:
        print()
        print("> cwd: str = {}".format(cwd))
        print()
# endregion
# region debug_function
    if debug_function:
        print()
        print("> }")
        print()
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
    folders = []
    for item in all_files_and_folders:
        if os.path.isdir(item):
            folders.append(item)

# TODO parallelize the execution of each folder using processing pool executor
    for folder in folders:
        process_folder(current_directory_path, folder)


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

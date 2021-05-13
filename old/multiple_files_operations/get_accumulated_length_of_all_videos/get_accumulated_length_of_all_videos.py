#! /usr/bin/python3
"""
    get accumulated length of all videos in a directory
"""

import os
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/get_video_length/"
spec = importlib.util.spec_from_file_location("get_video_length",
    python_scripts_folder_path + subfolder + "get_video_length.py")
get_video_length_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_video_length_script)

subfolder : str = "src/multiple_files_operations/get_all_videos_in_a_directory/"
spec = importlib.util.spec_from_file_location("get_all_videos_in_a_directory",
    python_scripts_folder_path + subfolder + "get_all_videos_in_a_directory.py")
get_all_videos_in_a_directory_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_all_videos_in_a_directory_script)



def get_accumulated_length_of_all_videos(directory: str,
    debug_function : bool = False):
    """
        get_accumulated_length_of_all_videos
    Args:
        directory (str): the directory with the videos

    Returns: accumulated_length (float): the length in seconds
    """
# region def function(...)
    debug_function = True # comment to toggle
# region debug_function
    if debug_function:
        print("[def] get_accumulated_length_of_all_videos(")
        print("      directory: str = {}"\
            .format(str(directory)))
        print("                                          )")
        print("{")
        print()
# endregion
    accumulated_length : float = 0.0
    all_videos : list = get_all_videos_in_a_directory_script \
        .get_all_videos(directory)
# region debug_function
    if debug_function:
        print()
        print("> all_videos : list = [")
        for debug_item in all_videos:
            print("> {}".format(debug_item))
        print("> ]")
# endregion
    videos_length_dict = {}
# region debug_function
    if debug_function:
        print()
        print("> for video in all_videos:")
# endregion
    for video in all_videos:
# region debug_function
        if debug_function:
            print("> video = {}".format(video))
# endregion
        length = get_video_length_script \
            .get_video_length(video, debug_function=debug_function)
# region debug_function
        if debug_function:
            print("> length = {}".format(length))
# endregion
        videos_length_dict[video] = length
        try:
            accumulated_length += length
        except TypeError:
            pass
# region debug_function
    if debug_function:
        print()
        print("> videos_length_dict: dict = {")
        for debug_key, debug_value in videos_length_dict.items():
            print("  {} : {}".format(debug_key, debug_value))
        print("> }")
# endregion

# TODO handle the case where a video is corrupted
# region debug_function
    if debug_function:
        print()
        print("}")
        print()
# endregion
    return accumulated_length
# endregion def function(...)



def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)
    debug_function = True # comment to toggle
# region debug_function
    if debug_function:
        print("[def] main(")
        print("              )")
        print("{")
# endregion
    current_directory : str = os.getcwd()
# region debug_function
    if debug_function:
        print("     current_directory : str = {}"\
            .format(str(current_directory)))
# endregion
    get_accumulated_length_of_all_videos(current_directory, \
                                debug_function=debug_function)
# region debug_function
    if debug_function:
        print("}")
# endregion
# endregion def main(...)

# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    print("module_template.py.__main__")
    print()
    main(
        debug_function = debug_script
        )
    ...
# endregion if __name__ == "__main__":

#! /usr/bin/python3
"""
    get all videos from a given directory
"""
import os

import importlib.util # needed for importing scripts using the scripts path

# import
# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/is_file_video/"
spec = importlib.util.spec_from_file_location("is_file_video",
    python_scripts_folder_path + subfolder + "is_file_video.py")
is_file_video_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(is_file_video_script)


def get_all_videos(directory_path : str,
    debug_function : bool = False):
    """
        get all videos in a directory using the extension of the files

    Args:
        directory_path (str): the path to the directory to filter the videos

    Returns:
        videos_list list: the list of all videos in the directory
                        the list contains the absolute path of each video
    """
# region def function(...)
# region debug_function
    if debug_function:
        print()
        print("[def] get_all_videos(")
        print("      directory_path : str = {}"\
            .format(str(directory_path)))
        print("              )")
        print("{")
# endregion
# TODO check if directory is absolute path
    directory_path_is_absolute : bool = os.path.isabs(directory_path)
# region debug_function
    if debug_function:
        print("     directory_path_is_absolute : bool = {}"\
            .format(str(directory_path_is_absolute)))
# endregion
    if not directory_path_is_absolute:
        raise ValueError("directory_path must be an absolute path")
    all_items : list = os.listdir(directory_path)
    all_items_absolute_path : list = []
    for item in all_items:
        all_items_absolute_path.append(directory_path + item)
# region debug_function
    if debug_function:
        print("     all_items = {}"\
            .format(str(all_items)))
        print("     all_items_absolute_path = {}"\
            .format(str(all_items_absolute_path)))
# end
    only_videos : list = []
    for filename in all_items_absolute_path:
        is_file_video : bool = is_file_video_script \
            .is_video(filename, debug_function=debug_function)
        if is_file_video:
            only_videos.append(filename)
    only_videos.sort()

# region debug_function
    if debug_function:
        print("}")
# endregion


    return only_videos
# endregion def function(...)

def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)


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

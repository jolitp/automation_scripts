#! /usr/bin/python3
"""
    get all videos from a given directory
"""
import os

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
        print("[def] function(")
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
# TODO get all files in the directory
# TODO filter all videos from all files
# TODO convert the filtered list of video filenames to have absolute paths

# region debug_function
    if debug_function:
        print("}")
# endregion


    return
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

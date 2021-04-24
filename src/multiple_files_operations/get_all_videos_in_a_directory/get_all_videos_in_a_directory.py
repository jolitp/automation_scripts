#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""

def get_all_videos(direcory : str,
    debug_function : bool = False):
    """
        get all videos in a directory using the extension of the files

    Args:
        directory (str): the directory to filter the videos

    Returns:
        videos_list list: the list of all videos in the directory
                        the list contains the absolute path of each video
    """
# region def function(...)

# region debug_function
    if debug_function:
        print("[def] function(")
        print("      parameter : str = {1}"\
            .format(str(parameter)))
        print("              )")
        print("{")
# endregion



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

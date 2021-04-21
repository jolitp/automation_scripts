#! /usr/bin/python3
"""
    script to get the length of a single video file
"""
import os

def get_video_length(filename : str,
    debug_function : bool = False):
    """
        get the length of a video of a given path, path should be absolute

# NOTE should I return the number of seconds or the time formatted?
    Args:
        root_directory (str):

    Returns:
        str:
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
    is_filename_absolute : bool = os.path.isabs(filename)
# region debug_function
    if debug_function:
        print("os.path.isabs(filename) = {1}"\
            .format(is_filename_absolute))
# endregion\
    if not is_filename_absolute:
        raise ValueError("argument filename should be an absolute path.")

# cSpell: disable
# TODO use either of the following methods: ffmpeg, moviepy, pymediainfo or opencv
# source:
# https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
# cSpell: enable

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

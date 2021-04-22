#! /usr/bin/python3
"""
    script to get the length of a single video file
"""
import os
import cv2

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
# endregion
    if not is_filename_absolute:
        raise ValueError("argument filename should be an absolute path.")
# cSpell: disable
    duration = _with_opencv(filename)
# cSpell: enable
# region debug_function
    if debug_function:
        print("duration = {1}"\
            .format(duration))
# endregion
# cSpell: disable
# TODO use either of the following methods: ffmpeg, moviepy, pymediainfo or opencv
# source:
# https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
# cSpell: enable
    return duration
# region debug_function
    if debug_function:
        print("}")
# endregion
    return
# endregion def function(...)


# cSpell: disable
def _with_opencv(filename):
# cSpell: enable
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count/fps
    return duration

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

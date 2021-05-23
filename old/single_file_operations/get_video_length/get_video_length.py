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
        print("[def] get_video_length(")
        print("      filename : str = {}"\
            .format(str(filename)))
        print("              )")
        print("{")
# endregion
    is_filename_absolute : bool = os.path.isabs(filename)
# region debug_function
    if debug_function:
        print("os.path.isabs(filename) = {}"\
            .format(is_filename_absolute))
# endregion
    if not is_filename_absolute:
        raise ValueError("argument filename should be an absolute path.")
# cSpell: disable
    duration = _with_opencv(filename, debug_function=debug_function)
# cSpell: enable
# region debug_function
    if debug_function:
        print("duration = {}"\
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
def _with_opencv(filename, debug_function=False):
# cSpell: enable
    video = cv2.VideoCapture(filename)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
# region debug_function
    if debug_function:
        print("frame_count = {}"\
            .format(frame_count))
        print("fps = {}"\
            .format(fps))
# endregion
    if frame_count == 0.0 or fps == 0.0:
        duration = None
    else:
        duration = frame_count/fps
# region debug_function
    if debug_function:
        print("duration = {}"\
            .format(duration))
# endregion
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

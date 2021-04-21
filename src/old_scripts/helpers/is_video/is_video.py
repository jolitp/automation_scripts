#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""

def is_video(filename: str, debug_function: bool = False):
    """

    wether or not a file is a video

    Args:
        filename (str): the filename of the file

        debug_function (bool, optional): if debug statements should be printed to console.
            Defaults to False.

    Returns:
        bool: wether or not the file is a video
    """
# region def is_video(filename: str, debug_function: bool = False):

# region debug_function
    if debug_function:
        print("[def] is_video(")
        print("      filename: {0} = {1}" \
            .format(type(filename), str(filename)))
        print("              )")
        print("{")
# endregion
# cSpell: disable
    # region video_extensions
    video_extensions = ['.mp4', '.m4v', '.mkv','.ts', '.avi',
                        '.webm', '.flv', '.mov', '.wmv', '.vob',
                        '.ogm', '.mpg', '.divx','.rmvb',
                        ]
    # endregion video_extensions
# cSpell: enable
    is_it_a_video : bool = False
# region debug_function
    if debug_function:
        print("> is_it_a_video : " + str(is_it_a_video))
# endregion

    # region for ext in video_extensions:
    for ext in video_extensions:
        ends_with_ext : bool = filename.lower().rstrip().endswith(ext)
# region debug_function
        if debug_function:
            print()
            print("> [for] ext in video_extensions:")
            print(">       ext: " + str(ext))
            print()
            print("> > [if] ends_with_ext: " + str(ends_with_ext))
# endregion
        # region if ends_with_ext:
        if ends_with_ext:
            is_it_a_video = True
# region debug_function
            if debug_function:
                print("> > > is_it_a_video : " + str(is_it_a_video))
                print("> > > [break]")
# endregion
            break
        # endregion if ends_with_ext:
    # endregion for ext in video_extensions:
# region debug_function
    if debug_function:
        print("}")
# endregion
    return is_it_a_video
# endregion def is_video(filename: str, debug_function: bool = False):



if __name__ == '__main__':
    print("helper_methods.py.__main__")


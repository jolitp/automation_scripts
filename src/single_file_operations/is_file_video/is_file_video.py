#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""

# TODO add doctest for module

# TODO add doctest for function
def is_video(filename : str,
    debug_function : bool = False):
    """wether or not a file is a video

    Args:
        filename (str): the filename of the file

        debug_function (bool, optional): if debug statements should be printed to console.
            Defaults to False.

    Returns:
        bool: wether or not the file is a video

    """
# region def function(...)

# region debug_function
    if debug_function:
        print("[def] function(")
        print("      filename : str = {}"\
            .format(str(filename)))
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
        print("[return] is_it_a_video")
        print("}")
# endregion
    return is_it_a_video
# endregion def function(...)

def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)

# TODO make the script be usable by calling it with arguments

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

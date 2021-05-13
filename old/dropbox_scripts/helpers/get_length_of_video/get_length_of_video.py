#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""

# TODO maybe implementing logging the logic debugging to files
# cSpell: disable
"""
Corey Schafer
Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting
https://www.youtube.com/watch?v=-ARI4Cz-awo&t=600s

Corey Schafer
Python Tutorial: Logging Advanced - Loggers, Handlers, and Formatters
https://www.youtube.com/watch?v=jxmzY9soFXg&t=322s

others
https://www.youtube.com/results?search_query=python+logging

using print() statement redirection
https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
"""
# cSpell: enamble

def get_length_of_video(filename : str,
    debug_function : bool = False):
    """


    Args:
        root_directory (str):

    Returns:
        str:
    """
# region def get_length_of_video(...)
    result : float = 0.0
# region debug_function
    if debug_function:
        print("[def] function(")
        print("      filename : {0} = {1}"\
            .format(type(filename), str(filename)))
        print("              )")
        print("{")
# endregion
# TODO make this function work with subprocess
# TODO handle errors where a video is corrupted
# TODO raise exception if file does not exist



# region debug_function
    if debug_function:
        print("}")
# endregion


    return result
# endregion def get_length_of_video(...)




if __name__ == '__main__':
    print("get_length_of_video.py.__main__")



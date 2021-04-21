#! /usr/bin/python3
"""
    helper functions for use in various scripts
"""
import math

import importlib.util

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# cSpell:enable

spec = importlib.util.spec_from_file_location("module.name",
                                        python_scripts_folder_path +  "helpers/is_video/is_video.py")
is_video_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(is_video_module)



def filter_videos(list_of_filenames, debug_function: bool = False):
    """filter the list of filenames to contain only the videos in it

    Args:
        list_of_filenames (list(str)): a list of filenames

        debug_function (bool, optional): if debug statements should be printed to console.
            Defaults to False.

    Returns:
        list(str): a list of filenames with only videos in it
    """
# region def filter_all_videos(list_of_filenames : list(str)):

# region debug_function
    if debug_function:
        print("[def] filter_videos(")
        print("      list_of_filenames: ")
        list_length : int = len(list_of_filenames)
        digits = int(math.log10(list_length))
        for index, name in enumerate(list_of_filenames):
            print("      > name[{0}]: {1} = {2}" \
                .format(str(index).rjust(digits, "0"),
                        type(name),
                        name))
            # print("      > name[" + str(index) + "]: " + name)
            ...
        print("              )")
        print("{")
# endregion
    all_videos : set(str) = set([])
    # region for video in list_of_filenames:
    for filename in list_of_filenames:
# region debug_function
        if debug_function:
            print()
            print("> [for] filename in list_of_filenames:")
            print(">       filename: " + str(filename))
            print()
            print("> > [if] is_video(video): " + str(is_video_module.is_video(filename)))
# endregion
        # region if is_video(video):
        if is_video_module.is_video(filename):
            all_videos.add(filename)
# region debug_function
            if debug_function:
                print("> > > all_videos.append({})".format(filename))
                list_length : int = len(all_videos)
                digits = int(math.log10(list_length))
                for index, video in enumerate(all_videos):
                    print("> > > all_videos[{0}] = {1}" \
                        .format(str(index).rjust(digits, "0"), video))
# endregion
            ...
        ...
        # endregion if is_video(video):
    # endregion for video in list_of_filenames:
# region debug_function
    if debug_function:
        print("}")
# endregion
    return all_videos
# endregion def filter_all_videos(list_of_filenames : list(str)):



if __name__ == '__main__':
    print("helper_methods.py.__main__")



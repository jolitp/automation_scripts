#! /usr/bin/python3
"""
    creates a file with the total size of all videos in the directory

    creates another file with the number of videos in the directory

    creates a third file with the ratio: size_of_all_videos / number_of_videos

    creates a fourth file with the total length of the videos? same as mark-video-length script?

    creates a fifth file with the ratio of total length / number of videos

    creates a sixth file with the time to convert all the videos.
    probably the formula is the length of the videos * (between 1 to 12)


"""

import os # used for getting the current working directory (cwd)
import importlib.util # needed for importing scripts using the scripts path
from math import log # needed for sizeof_fmt(num : int):

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# cSpell:enable

spec = importlib.util.spec_from_file_location("module.name",
                                        python_scripts_folder_path +  "helpers/helpers/helpers.py")
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)

def get_size(fileobject):
    """get the size of a file in bytes

    Args:
        fileobject ([type]): [description]

    Returns:
        int: the size in bytes
    """
# region def getSize(fileobject):

    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size
# endregion def getSize(fileobject):


def size_formated(num : int):
    """human readable file size

    Args:
        num (int): the size in bytes

    Returns:
        str: the string representation of the filesize with the unit at the end
    """
# region def sizeof_fmt(num : int):

    # unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [0, 0, 1, 2, 2, 2])
    unit_list = ['bytes', 'kB', 'MB', 'GB', 'TB', 'PB']
    log_list = [0, 0, 1, 2, 2, 2]
    if num > 1:
        exponent = min(int(log(num, 1024)), len(unit_list) - 1)
        quotient = float(num) / 1024**exponent
        # unit, num_decimals = unit_list[exponent]
        unit = unit_list[exponent]
        num_decimals = log_list[exponent]
        format_string = '{:.%sf} {}' % (num_decimals)
        return format_string.format(quotient, unit)
    if num == 0:
        return '0 bytes'
    if num == 1:
        return '1 byte'
# endregion def sizeof_fmt(num : int):


def main(debug_function: bool = False):
    """
    the main function for the script
    """

# region def main(debug_function: bool = False):

# region debug_function
    if debug_function:
        print("[def] measure_videos_per_size_ratio.main()")
        print("{")
# endregion
    current_directory_path = os.getcwd()
# region debug_function
    if debug_function:
        print("> current_directory_path : \n (type) {0} = \n{1}"\
            .format(type(current_directory_path),
                    str(current_directory_path)))
        print()
# endregion
    all_files_and_folders = os.listdir(current_directory_path)
# region debug_function
    if debug_function:
        print("> all_files_and_folders:")
        for index, item in enumerate(all_files_and_folders):
            print("> all_files_and_folders[{0}] :\n  (type) {1} = \n  {2}" \
                .format(str(index), type(item), str(item)))
            # print()
        print()
# endregion
    all_videos = []
    all_videos = helpers.filter_videos(all_files_and_folders)
    all_videos = list(all_videos)
    all_videos.sort()
# region debug_function
    if debug_function:
        print("> all_videos:")
        for index, item in enumerate(all_videos):
            print("> all_videos[{0}] :\n  (type) {1} = \n  {2}" \
                .format(str(index), type(item), str(item)))
            # print()
        print()
# endregion
    number_of_videos : int = len(all_videos)
# region debug_function
    if debug_function:
        print("> number_of_videos : \n (type) {0} = \n{1}"\
            .format(type(number_of_videos),
                    str(number_of_videos)))
        print()
# endregion
    size_of_all_videos : list = [0] * number_of_videos
    for index, video in enumerate(all_videos):
        file = open(video, 'rb')
        size_of_all_videos[index] = get_size(file)
        ...
# region debug_function
    if debug_function:
        print("> size_of_all_videos:")
        for index, item in enumerate(size_of_all_videos):
            print("> all_videos[{0}] :\n  (type) {1} = \n  {2}" \
                .format(str(index), type(item), str(item)))
            # print()
        print()
# endregion
    accumulated_size_of_all_videos : int = 0
    for size in size_of_all_videos:
        accumulated_size_of_all_videos += size
        ...
# region debug_function
    if debug_function:
        print("> accumulated_size_of_all_videos : \n (type) {0} = \n{1}"\
            .format(type(accumulated_size_of_all_videos),
                    str(accumulated_size_of_all_videos)))
        print()
# endregion
    accumulated_size_of_all_videos_human_readable : str = \
        size_formated(accumulated_size_of_all_videos)
# region debug_function
    if debug_function:
        print("> accumulated_size_of_all_videos_human_readable : \n (type) {0} = \n{1}"\
            .format(type(accumulated_size_of_all_videos_human_readable),
                    str(accumulated_size_of_all_videos_human_readable)))
        print()
# endregion
    avarage_size : float = accumulated_size_of_all_videos / number_of_videos
# region debug_function
    if debug_function:
        print("> avarage_size : \n (type) {0} = \n{1}"\
            .format(type(avarage_size),
                    str(avarage_size)))
        print()
# endregion
    avarage_size_human_readable = size_formated(avarage_size)
# region debug_function
    if debug_function:
        print("> avarage_size_human_readable : \n (type) {0} = \n{1}"\
            .format(type(avarage_size_human_readable),
                    str(avarage_size_human_readable)))
        print()
# endregion
    number_of_videos : int = len(all_videos)
# region debug_function
    if debug_function:
        print("> number_of_videos : \n (type) {0} = \n{1}"\
            .format(type(number_of_videos),
                    str(number_of_videos)))
        print()
# endregion
    name_of_file : str = " [avarage_size].txt"
    avarage_size_file = open(name_of_file, "w+")
    avarage_size_file.write(str(avarage_size))
    avarage_size_file.close()

    name_of_file : str = " [acc_size_of_all_videos].txt"
    accumulated_size_of_all_videos_file = open(name_of_file, "w+")
    accumulated_size_of_all_videos_file.write(str(accumulated_size_of_all_videos))
    accumulated_size_of_all_videos_file.close()

    name_of_file : str = " [avarage_size_HR] = {0}.txt".format(avarage_size_human_readable)
    avarage_size_human_readable_file = open(name_of_file, "w+")
    avarage_size_human_readable_file.write(str(avarage_size_human_readable))
    avarage_size_human_readable_file.close()

    name_of_file : str = " [acc_size_of_all_videos_HR] = {0}.txt"\
        .format(accumulated_size_of_all_videos_human_readable)
    accumulated_size_of_all_videos_human_readable_file = open(name_of_file, "w+")
    accumulated_size_of_all_videos_human_readable_file\
        .write(str(accumulated_size_of_all_videos_human_readable))
    accumulated_size_of_all_videos_human_readable_file.close()

    name_of_file : str = " [number_of_videos] = {0}.txt".format(number_of_videos)
    number_of_videos_file = open(name_of_file, "w+")
    number_of_videos_file.write(str(number_of_videos))
    number_of_videos_file.close()



# region debug_function
    if debug_function:
        print("}")
# endregion
    ...
# endregion def main(debug_function: bool = False):


# region if __name__ == "__main__":
if __name__ == "__main__":
    main(
        debug_function = True
        )
    ...
# endregion if __name__ == "__main__":

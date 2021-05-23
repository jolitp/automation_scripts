#! /usr/bin/python3
"""
separate the folders containing videos into 2 folders
long or short
"""

import os
import pathlib
from glob import glob
# from datetime import date
# from colorama import Fore
# from colorama import Style
# from arepl_dump import dump


def is_folder(item: str):
    """returns wether or not an item in a directory is a folder

    Args:
        item (str): the item to check

    Returns:
        bool: if item is folder or not
    """
# region def is_folder(item: str):
    is_it_folder : bool = False
    if os.path.isdir(item):
        is_it_folder = True
        ...
    return is_it_folder
    ...
# endregion def is_folder(item: str):


# dump() # yes
def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...):

# region debug_function
    if debug_function:
        print("[def] sort_by_number_of_videos_and_size.main()")
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
    only_folders : list = []
    for item in all_files_and_folders:
        if is_folder(item):
            only_folders.append(item)
        ...
# region debug_function
    if debug_function:
        print("> only_folders:")
        for index, item in enumerate(only_folders):
            print("> only_folders[{0}] :\n  (type) {1} = \n  {2}" \
                .format(str(index), type(item), str(item)))
            # print()
        print()
# endregion
    # region for folder in only_folders:
    for folder in only_folders:
        if ' BIG' in folder or ' SMALL' in folder:
            continue
        if ' SHORT' in folder or ' LONG' in folder:
            continue
# region debug_function
        if debug_function:
            print("> folder : \n (type) {0} = \n{1}"\
                .format(type(folder),
                        str(folder)))
            print()
# endregion
        all_files_and_folders_inside = os.listdir(folder)
# region debug_function
        if debug_function:
            print("> all_files_and_folders_inside:")
            for index, item in enumerate(all_files_and_folders_inside):
                print("> all_files_and_folders_inside[{0}] :\n  (type) {1} = \n  {2}" \
                    .format(str(index), type(item), str(item)))
                # print()
            print()
# endregion
    # endregion for folder in only_folders:
# region debug_function
    if debug_function:
        print("}")
# endregion
    ...
# endregion def main(...):


# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    main(
        debug_function = debug_script
        )
    ...
# endregion if __name__ == "__main__":


# print(" ================== script root ================== ")
# current_path = os.getcwd()


# dirs = glob(str(current_path) + '/*/')
# # print(f'\n{Fore.YELLOW}all directories {Style.RESET_ALL}: ' + str(dirs))

# for folder in dirs:
#     if ' BIG' in folder or ' SMALL' in folder:
#         continue
#     if ' SHORT' in folder or ' LONG' in folder:
#         continue
#     # print(f'\n{Fore.YELLOW}folder{Style.RESET_ALL}: ' + folder)
#     folder_path = os.path.dirname(folder)
#     base_name = os.path.basename(folder_path)

#     file_path = folder_path + '/mark-video-length-finished.data'
#     # print(file_path)
#     print()
#     if pathlib.Path(file_path).is_file():
#         f = open(file_path, 'r+t')
#         first_line = f.readline().strip()
#         f.close()

#         # print('length : ' + str(first_line))

#         DESTINATION_SHORT = str(current_path) + '/ SHORT/'
#         DESTINATION_LONG = str(current_path) + '/ LONG/'

#         source = str(current_path) + '/' + base_name
#         print('source :      ' + source)
#         print(first_line + ' < ' + '12:00:00:000000')
#         # date_format = date.fromisoformat(first_line)
#         # print(date_format)

#         time_separated = first_line.split(':')
#         print(time_separated)
#         print(first_line)
#         if not '.' in first_line:
#             # print(f'{Fore.RED}directory has no videos{Style.RESET_ALL}: ')
#             continue
#         day = 0
#         if 'day' in time_separated[0]:
#             print('has day')
#             day_and_hour = time_separated[0].split(',')
#             day = str(day_and_hour[0].replace(' day', ''))
#             # print(f'{Fore.GREEN}day {Style.RESET_ALL}: ' + str(day))
#             hour = int(day_and_hour[1])
#             # print(f'{Fore.GREEN}hour{Style.RESET_ALL}: ' + str(hour))
#             minutes = int(time_separated[1])
#             # print(f'{Fore.GREEN}minutes{Style.RESET_ALL}: ' + str(minutes))
#             # cSpell: disable
#             seconds_and_miliseconds = time_separated[2].split('.')
#             seconds = int(seconds_and_miliseconds[0])
#             # print(f'{Fore.GREEN}seconds{Style.RESET_ALL}: ' + str(seconds))
#             miliseconds = int(seconds_and_miliseconds[1])
#             # print(f'{Fore.GREEN}miliseconds{Style.RESET_ALL}: ' + str(miliseconds))
#         else:
#             hour = int(time_separated[0])
#             # print(f'{Fore.GREEN}hour{Style.RESET_ALL}: ' + str(hour))
#             minutes = int(time_separated[1])
#             # print(f'{Fore.GREEN}minutes{Style.RESET_ALL}: ' + str(minutes))
#             seconds_and_miliseconds = time_separated[2].split('.')
#             seconds = int(seconds_and_miliseconds[0])
#             # print(f'{Fore.GREEN}seconds{Style.RESET_ALL}: ' + str(seconds))
#             miliseconds = int(seconds_and_miliseconds[1])
#             # print(f'{Fore.GREEN}miliseconds{Style.RESET_ALL}: ' + str(miliseconds))
#             # cSpell: enable

#         if hour < 12 and day == 0:
#             print('length is short')
#             print(DESTINATION_SHORT)
#             os.rename(source, DESTINATION_SHORT + base_name)
#         else:
#             print('length is long')
#             print(DESTINATION_LONG)

#             os.rename(source, DESTINATION_SHORT + base_name)

# print(" ================== script root ================== ")

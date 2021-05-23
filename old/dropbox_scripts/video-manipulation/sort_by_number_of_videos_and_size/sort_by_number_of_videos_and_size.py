#! /usr/bin/python3
"""
    creates a file with the total size of all videos in the directory

    creates another file with the number of videos in the directory

    creates a third file with the ratio: size_of_all_videos / number_of_videos

    creates a fourth file with the total length of the videos? same as mark-video-length script?

    creates a fifth file with the ratio of total length / number of videos

    creates a sixth file with the time to convert all the videos.
    probably the formula is the length of the videos * (between 1 to 12)

    sort the most viable videos to go to youtube without concatenating

"""

import os             # used for getting the current working directory (cwd)

import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# cSpell:enable

spec = importlib.util.spec_from_file_location("module.name",
                                        python_scripts_folder_path +  "helpers/helpers/helpers.py")
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)


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


def process_folder(root: str,
                    folder: str,
                    debug_function: bool = False) -> None:
    """process each folder passed to it
    Args:
        root (str): the root folder(where the script was called)
        folder (str): the folder to be processed
        debug_function (bool, optional): if function should be debugged. Defaults to False.
    """
# region def process_folder(...):
# region debug_function
    if debug_function:
        print("> [def] process_folder(...)")
        print("> [def] process_folder(...)")
        print("> {")
# endregion



# region debug_function
    if debug_function:
        print("> }")
# endregion
    ...
# endregion def process_folder(...):


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
    for folder in only_folders:
        process_folder(current_directory_path, folder, debug_function=True)
        ...

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

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

import os # used for getting the current working directory (cwd),
            # used also for deleting files
# import importlib.util # needed for importing scripts using the scripts path

# # cSpell:disable
# python_scripts_folder_path : str = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
# # cSpell:enable

# spec = importlib.util.spec_from_file_location("module.name",
#                                         python_scripts_folder_path +  "helpers/helpers/helpers.py")
# helpers = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(helpers)


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

def is_py_script(item: str):
    """check to see if item(file or folder) is a python script, by checking it's extension

    Args:
        item (str): the name of the file or folder

    Returns:
        bool: wether or not the item is a python script
    """
    is_it_py_script : bool = False
    ext : str = ".py"
    if ext in item:
        is_it_py_script = True
        ...

    return is_it_py_script
    ...


def process_folder(root_folder: str, folder: str, debug_function: bool = False):
    """do what have to be done inside the folder

    Args:
        root_folder (str): the root folder, most likely the cwd from the script

        folder (str): the name of the folder being processed

        debug_function (bool, optional): if debug statements should be printed to console.
            Defaults to False.
    """
# region def process_folder(...):
# region debug_function
    if debug_function:
        print()
        print("> [def] process_folder(...)")
        print("> root_folder: {0} = {1}" \
            .format(type(root_folder), str(root_folder)))
        print()
        print("> folder: {0} = {1}" \
            .format(type(folder), str(folder)))
        print()
        print("> debug_function: {0} = {1}" \
            .format(type(debug_function), str(debug_function)))
        print()
        print("> {")
        print()
# endregion
        items_inside_folder : list = os.listdir(folder)
# region debug_function
        if debug_function:
            print("> > items_inside_folder = [")
            for debug_item in items_inside_folder:
                print("    {0},".format(str(debug_item)))
            print("]")
        print()
# endregion
        files_to_remove : list = []
# region debug_function
        if debug_function:
            print()
            print("> > [for] item in items_inside_folder:")
            print("> >  items_inside_folder = [")
            for debug_item in items_inside_folder:
                print("    {0},".format(str(debug_item)))
            print("]")
# endregion
        # region for item in items_inside_folder:
        for item in items_inside_folder:
# region debug_function
            if debug_function:
                print()
                print("[iteration]")
                print("> > item: " + str(item))
                print()
                print("> > [if] is_py_script(item): " + str(is_py_script(item)))
                print()
                print("> > > <before appending>: \n> > > {0}" \
                    .format(item))
                print("> > > to:")
                print("> > > files_to_remove = [")
                for debug_item in files_to_remove:
                    print("> > > {0},".format(str(debug_item)))
                print("]")
# endregion
            # region if is_py_script(item):
            if is_py_script(item):
                files_to_remove.append(item)
            # endregion if is_py_script(item):
# region debug_function
                if debug_function:
                    print()
                    print("[iteration]")
                    print("> > item: " + str(item))
                    print()
                    print("> > [if] is_py_script(item): " + str(is_py_script(item)))
                    print()
                    print("> > > <after appending>: \n> > > {0}" \
                        .format(item))
                    print("> > > to:")
                    print("> > > files_to_remove = [")
                    for debug_item in files_to_remove:
                        print("> > > {0},".format(str(debug_item)))
                    print("]")
# endregion
# region debug_function
        if debug_function:
            print()
            print("> > [for] item in files_to_remove:")
            print("> >  files_to_remove = [")
            for debug_item in files_to_remove:
                print("  " + debug_item + ",")
            print("]")
# endregion
        # endregion for item in items_inside_folder:
        for filename in files_to_remove:
            absolute_path : str = root_folder + "/" + folder + "/" + filename
# region debug_function
            if debug_function:
                print()
                print("> > > [iteration]")
                print("> > > filename = {0}".format(filename))
                print()
                print("> > > absolute_path = {0}".format(absolute_path))
                print("> > > <deleting file>")
# endregion
            os.remove(absolute_path) # comment to toggle

# region debug_function
    if debug_function:
        print()
        print("> }")
        print()
# endregion
    ...
# endregion def process_folder(...):

def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(debug_function: bool = False):


# region debug_function
    if debug_function:
        print("[def] remove_scripts_from_folders.main()")
        print("> > {")
        print()
# endregion
    current_directory_path = os.getcwd()
# region debug_function
    if debug_function:
        print()
        print("> current_directory_path : \n (type) {0} = \n{1}"\
            .format(type(current_directory_path),
                    str(current_directory_path)))
        print()
# endregion
    all_files_and_folders = os.listdir(current_directory_path)
# region debug_function
    if debug_function:
        print("> all_files_and_folders = [")
        for debug_item in all_files_and_folders:
            print("  {0}," \
                .format(str(debug_item)))
        print("]")
        print()
# endregion
    only_folders : list = []
    # region for item in all_files_and_folders:
    for item in all_files_and_folders:
        if is_folder(item):
            only_folders.append(item)
        ...
    # endregion for item in all_files_and_folders:
    only_folders.sort()
# region debug_function
    if debug_function:
        print("> only_folders = [")
        for debug_item in only_folders:
            print("  {0}," \
                .format(str(debug_item)))
        print("]")
        print()
# endregion
    # region for folder in only_folders:
# region debug_function
    if debug_function:
        print()
        print("> [for] folder in only_folders:")
        print("> >  only_folders = [")
        for debug_item in only_folders:
            print("    " + debug_item + ",")
        print("]")
        print()
# endregion
    for folder in only_folders:
        debug_func : bool = False
        debug_func : bool = True # comment to toggle
        process_folder(current_directory_path, folder, debug_function=debug_func)
    # endregion for folder in only_folders:
# region debug_function
    if debug_function:
        print("}")
# endregion
    ...
# endregion def main(debug_function: bool = False):


# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_main : bool = False
    # debug_main : bool = True  # comment to toggle
    main(
        debug_function = debug_main
        )
    ...
# endregion if __name__ == "__main__":


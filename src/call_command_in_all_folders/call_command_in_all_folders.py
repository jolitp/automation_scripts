#! /usr/bin/env python3
"""
call all the commands passed to the script in order
"""
# cSpell: word jolitp chdir
import os
import sys
from pathlib import Path

from natsort import natsorted, ns

# region process_folder
def process_folder(
    folder_path:Path,
    debug_function = None
):
    """do the actual logic of the script on a specified folder

    Args:
        folder_path (Path): the path to the folder
        debug_function (bool, optional): Defaults to None.
    """
    debug_function = True # comment to toggle

    if debug_function:
        print()
        print("START === process_folder() === START ")
        print()
        print("def process_folder(")
        print(f"|   folder_path:Path = {folder_path}")
        print()

    args = sys.argv[1:]

    for arg in args:
        # subprocess.run(arg)
        print()
        print(f"calling: {arg}")
        print()
        os.chdir(folder_path)
        os.system(arg)
        print()
        print(f"called: {arg}")
        print()
        ...

    if debug_function:
        print()
        print("END === process_folder() === END")
        print()
    ...
# endregion process_folder


# region main
def main(
    debug_function = None
):
    """main function from script

    Args:
        debug_function (bool, optional): Defaults to None.
    """
    debug_function = True # comment to toggle
    cwd = os.getcwd()

    if debug_function:
        print()
        print("current_working_directory:")
        print(cwd)

    all_immediate_items = os.listdir(cwd)

    all_immediate_items \
        = natsorted(all_immediate_items , alg=ns.PATH)

    if debug_function:
        print()
        print("all_immediate_items = [")
        for element in all_immediate_items:
            print("  {}".format(element))
        print("]")
        print()

    all_immediate_folders = []
    for item in all_immediate_items:
        if os.path.isdir(item):
            all_immediate_folders.append(item)

    if debug_function:
        print()
        print("all_immediate_folders = [")
        for element in all_immediate_folders:
            print("  {}".format(element))
        print("]")
        print()

    for folder in all_immediate_folders:
        folder_path: Path = Path(cwd + "/" + folder)
        process_folder(folder_path)
        ...

    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   main")
# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START call_command_in_all_folders.py START"
    print(msg)
    print()

    main()

    msg = "END call_command_in_all_folders.py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":


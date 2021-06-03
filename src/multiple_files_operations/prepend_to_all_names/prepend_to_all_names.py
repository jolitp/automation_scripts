#! /usr/bin/python3
"""
    adds the first argument to all files of types of the second argument.

    to add to folders pass --folders
"""

import os
import sys
import argparse
import warnings

def main(debug_function: bool = False):
    """
    the main function for the script
    """
# region def main(...)

    desc = """
    adds -p/--prepend [text] to the start of the names of all files of the -e/--extension
    if the -f/--folders flag is given adds the text to folders instead of files
    """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-p", "--prepend", dest="text", type=str, required=True,
                        help="the text to be appended to the start of each file or folder")
# cSpell: disable
    parser.add_argument("-e", "--extension", dest="extension", type=str, nargs='*',
                        help="the extension of the files that will be changed")
# cSpell: enable
    parser.add_argument("-f", "--folders", dest="folders", action='store_true',
                        help="wether or not to add text to folders instead of files")
    parser.add_argument("-ns", "--nospace", dest="nospace", action='store_true', default=False,
                        help="wether or not to add a space in front of the text")
    arguments = parser.parse_args()
    # print(arguments)

    current_directory : str = str(os.getcwd())
# region debug_function
    print("> current_directory = {}".format(current_directory))
# endregion debug_function
    all_files = os.listdir(current_directory)

    text_to_prepend : str = arguments.text
    extensions : list = arguments.extension

    do_folders = False
    if arguments.folders:
        do_folders = True

    add_space = True
    if arguments.nospace:
        add_space = False

    print("add space = " , add_space)
    if extensions is None and not do_folders:
        warnings.warn("If -f/--folders is not given -e/--extension is required")
        sys.exit()

    elements_to_append_to = []
    if do_folders:
        for file_or_folder in all_files:
            if os.path.isdir(file_or_folder):
                elements_to_append_to.append(file_or_folder)
    else:
        for file_or_folder in all_files:
            for extension in extensions:
                if extension in file_or_folder:
                    elements_to_append_to.append(file_or_folder)

    print()
    print(" elements to append to ")
    print()
    print(elements_to_append_to)
    print()
    for element in elements_to_append_to:
        source = "{0}/{1}" \
            .format(current_directory, element)
        print("source : ")
        print(source)
        if add_space:
            destination = "{0}/{1} {2}" \
                .format(current_directory, text_to_prepend, element)
        else:
            destination = "{0}/{1}{2}" \
                .format(current_directory, text_to_prepend, element)
        print("destination : ")
        print(destination)

        os.rename(source, destination)
        ...

# endregion def main(...)

# region if __name__ == "__main__":
if __name__ == "__main__":
    debug_script : bool = False
    debug_script : bool = True  # comment to toggle
    print("prepend_to_all_names.py.__main__")
    print()
    main(
        debug_function = debug_script
        )
    ...
# endregion if __name__ == "__main__":

#! /usr/bin/env python3
"""
separate files into folders:

videos/
subs/
files/
"""

import os
import os.path
from blessings import Terminal

def get_nested_files(path: str):
    """
    gets the nested files in the directory recursively

    Args:
        path (str):
            the path to the folder to get the files
            defaults to current working directory.

    Returns:
        nested_files (list(str)):
            a list of paths containing the absolute path to each file.
    """
    nested_files = []
    for root, _, files in os.walk(path, topdown=False):
        for name in files:
            full_path = (os.path.join(root, name))
            nested_files.append(full_path)
    return nested_files


def filter_files_by_extension(files: list ,
                            extensions: list):
    """
    filter the files in a list to have only files of the given extensions

    Args:
        files (list):
            the list of files
        extensions (list):
            the list of extensions

    Returns:
        filtered_files (list):
            the list of files with only files of the given extensions
    """
    filtered_files = []
    for file in files:
        file_ext = os.path.splitext(file)[-1].lower()
        file_ext = remove_dot_from_extension(file_ext)
        for extension in extensions:
            ext = remove_dot_from_extension(extension).lower()
            # print("ext \n", ext)
            # print("file_ext \n", file_ext)
            if file_ext == ext:
                filtered_files.append(file)

    return filtered_files
    ...


def remove_dot_from_extension(extensions):
    """remove the dot from an extension

    Args:
        extensions (str or list): the extension
    Returns:
        the extension without the dot
    """
    if isinstance(extensions, str):
        ext : str = extensions
        extensions = ext.replace(".","")
    return extensions


def main():

    print()
    print("START main() START")
    print()

    t = Terminal()
    cwd = os.getcwd()
    print()
    print(t.blue("current_working_directory:"))
    print(cwd)
    print()

    all_nested_files = get_nested_files(cwd)

    print("all_nested_files = [")
    for element in all_nested_files:
        print("  {}".format(element))
    print("]")

    print()
    print("END main() END")
    print()
    ...

if __name__ == "__main__":
    print()
    msg = "START separate_videos_subs_files START"
    print(msg)
    print()

    main()

    msg = "END separate_videos_subs_files END"
    print()
    print(msg)
    print()
    ...
#! /usr/bin/env python3
"""
separate files into folders:

videos/
subs/
files/
"""

import os


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


def main():

    print()
    print("START main() START")
    print()
    cwd = os.getcwd()
    print()
    print("current_working_directory:")
    # print(cwd)
    print()
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
#! /usr/bin/env python3
"""
remove special characters from files and folders
"""
# cSpell: word jolitp pytest isdigit isalpha
import os
import sys
from pathlib import Path
import concurrent.futures



# region remove special characters
def remove_special_characters(
    input:str
    ):
    """removes any character that is not a letter or a number
    from the input string, exceptions are:

    _ -> <space>
    . -> <space>
    (unless it is a dot at the start of a file or folder)
    <space> -> <space>
    / -> /

    any other symbol is renamed to <space>

    Args:
        input (str): the input string

    Returns:
        (str) : the string with the characters removed
    """
    output = ""
    ext = ""
    basename = ""

    # is_file = os.path.isfile(input)
    # if is_file:
    basename = os.path.splitext(input)[0]
    ext = os.path.splitext(input)[1]

    for index, character in enumerate(basename):
        if index == 0:
            if character == ".":
                output += "."
                continue
        if basename[index - 1] == "/":
            if character == ".":
                output += "."
                continue
        if character.isalpha() or character.isdigit():
            output += character
        elif character == " " or character == "_":
            output += character
        elif character == "/":
            output += "/"
        elif character == ".":
            output += " "
        else:
            output += " "

    output.replace("/ ", "/.")
    output = output + ext
    sys.stdout.flush()
    return output
    ...
# endregion remove special characters


# region main
def main(
    debug_function = None
):
    debug_function = True # comment to toggle
    cwd = os.getcwd()

    args = sys.argv

    if debug_function:
        print()
        print("current_working_directory:")
        print(cwd)

    nested_files = []
    nested_folders = []

    print("found:")

    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            dir_path = os.path.join(root,name)
            print(dir_path)
            nested_folders.append(dir_path)
        for name in files:
            file_path = os.path.join(root,name)
            print(file_path)
            nested_files.append(file_path)

    for index, folder in enumerate(nested_folders):
        nested_folders[index] = folder[2:]
        ...

    for index, file in enumerate(nested_files):
        nested_files[index] = file[2:]
        ...

    if debug_function:
        print()
        print("  nested_files = [")
        for item in nested_files:
            print(item)
        print("  ]")

    if debug_function:
        print()
        print("  nested_folders = [")
        for item in nested_folders:
            print(item)
        print("  ]")

    src_folders = []
    for folder in nested_folders:
        src_folders.append(cwd + "/" + folder)
    src_files = []
    for file in nested_files:
        src_files.append(cwd + "/" + file)


    processed_folders = []
    processed_files = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        folders_results = \
            executor.map(remove_special_characters, nested_folders)
        files_results = \
            executor.map(remove_special_characters, nested_files)

        print()
        print("folders results: ")
        for result in folders_results:
            print(result)
            processed_folders.append(result)

        print()
        print("files results: ")
        for result in files_results:
            print(result)
            processed_files.append(result)
        print()
        ...

    if debug_function:
        print()
        print("  processed_folders = [")
        for item in processed_folders:
            print(item)
        print("  ]")

    if debug_function:
        print()
        print("  processed_files = [")
        for item in processed_files:
            print(item)
        print("  ]")

    dst_folders = []
    for folder in processed_folders:
        dst_folders.append(cwd + "/" + folder)

    dst_files = []
    for file in processed_files:
        dst_files.append(cwd + "/" + file)

    folders_to_move = []
    for index, _ in enumerate(nested_folders):
        src = src_folders[index]
        dst = dst_folders[index]

        if src == dst:
            continue
        else:
            folders_to_move.append((src, dst))

    files_to_move = []
    for index, _ in enumerate(nested_files):
        src = src_files[index]
        dst = dst_files[index]

        if src == dst:
            continue
        else:
            files_to_move.append((src, dst))

    if debug_function:
        print()
        print("folders to move: ")
        for folder in folders_to_move:
            basename = os.path.basename(folder[0])
            print()
            print("folder: {}".format(basename))
            print("from:")
            print(folder[0])
            print("to:")
            print(folder[1])

        print("files to move: ")
        for file in files_to_move:
            basename = os.path.basename(file[0])
            print()
            print("file: {}".format(basename))
            print("from:")
            print(file[0])
            print("to:")
            print(file[1])

    for folder_pair in folders_to_move:
        src = folder_pair[0]
        dst = folder_pair[1]
        os.rename(src, dst)

    for file_pair in files_to_move:
        src = file_pair[0]
        dst = file_pair[1]
        os.rename(src, dst)



    if debug_function:
        print("---------=---------=---------=---------=---------=---------=---------=---------=")
        print("END   main")
# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START remove_special_characters.py START"
    print(msg)
    print()

    main()

    msg = "END remove_special_characters.py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":


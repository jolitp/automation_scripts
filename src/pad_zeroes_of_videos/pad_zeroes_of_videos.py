#! /usr/bin/env python3
"""
pad the numbers with zeroes of the filenames of videos in a folder
"""
# cSpell: word jolitp chdir isdigit itertools groupby numpy zfill
import os
import sys
from pathlib import Path
import re
from itertools import groupby
from numpy import transpose

from natsort import natsorted, ns
import snoop
from rich.console import Console
from rich.theme import Theme
from rich.traceback import install as rich_install_traceback

rich_install_traceback()

C = Console()

# region separate_name
# @snoop
def separate_name(name: str):
    """
    separates a name into a list of strings based on
    the locations where numbers appear

    example:

    name <- "01_section_1_name_1

    result -> [ "01", "_section_", "1", "_name_", "1" ]

    Args:
        name (str) : the name as a string

    Returns:
        (list) : list of the sections of the name separated
    """
    # result = re.findall(r'(\d+|[A-Za-z]+)', name)
    # result = re.findall(r'(\d+|[^\d+])', name)

    result = [''.join(g) for _, g in groupby(name, str.isdigit)]

    # C.log(res)
    return result
    ...
# endregion separate_name


# region add_blanks_to_the_end
def add_blanks_to_the_end(input_list:list):
    max_length = 0
    for section in input_list:
        section_length = len(section)
        if section_length > max_length:
            max_length = section_length
            ...
        ...

    for section in input_list:
        section: list = section
        section_length = len(section)
        if section_length < max_length:
            remaining_length = max_length - section_length
            for _ in range(remaining_length):
                section.append("")
                ...
            ...
        ...
    return input_list
    ...
# endregion add_blanks_to_the_end


# region are_numbers_predicate
def are_numbers_predicate(input:list):
    result = []
    for index, element in enumerate(input):
        if input[index].isdigit():
            result.append(True)
        else:
            result.append(False)
    return result
# endregion are_numbers_predicate


# region pad_zeroes
def pad_zeroes(
    input: list,
):
    # separate numbers and non-numbers from each name
    names_separated = []
    for element in input:
        separated_name = separate_name(element)
        names_separated.append(separated_name)
    names_separated = add_blanks_to_the_end(names_separated)
    inverted_sections = transpose(names_separated)

    # check which sections are numbers
    are_numbers = []
    for element in inverted_sections:
        x = are_numbers_predicate(element)
        are_numbers.append(x)
    only_numbers = []
    for section in are_numbers:
        _all = any(section)
        only_numbers.append(_all)
    inverted_sections_padded = list(inverted_sections.copy())
    for section_index, are_all_numbers in enumerate(only_numbers):
        if are_all_numbers:
            max_digits = 0
            for number in inverted_sections[section_index]:
                number_of_digits:int = len(number)
                if number_of_digits > max_digits:
                    max_digits = number_of_digits
            for index, number in enumerate(inverted_sections[section_index]):
                number: str = str(number)
                number_of_digits = len(number)
                difference = max_digits - number_of_digits
                zeroes_padded = difference * "0" + number
                inverted_sections_padded[section_index][index] \
                    = zeroes_padded
        else:
            inverted_sections_padded[section_index] = inverted_sections[section_index]
    restored_sections_padded = transpose(inverted_sections_padded)

    # filter out sections with only zeroes
    restored_sections_padded_filtered = []
    for index_section, section in enumerate(restored_sections_padded):
        restored_sections_padded_filtered.append([])
        section_filtered = restored_sections_padded_filtered[index_section]
        for index_part, part in enumerate(section):
            m = re.match("0+",str(part))
            if m == None:
                result = ""
            else:
                result = m.group()
            if part == result:
                restored_sections_padded_filtered[index_section].append("")
            else:
                restored_sections_padded_filtered[index_section].append(part)
            ...
    # assemble strings back
    output = []
    for section in restored_sections_padded_filtered:
        joined_string = ""
        for part in section:
            joined_string += part
        output.append(joined_string)
    return output
# endregion pad_zeroes


# TODO move to utility module
# region print_logic
def print_logic(
    value,
    note=""
    ):
    theme = Theme(
        {
            "statement" : "yellow",
            "value" : "cyan",
            "true" : "bold green",
            "false" : "bold red",
            "none" : "red on white",
        }
    )
    console = Console(theme=theme)

    value_type = type(value)
    value_name = retrieve_outermost_name(value)
    value_is_scalar = not hasattr(value, '__len__') and (not isinstance(value, str))
# DONE check if value is scalar or not
# https://stackoverflow.com/questions/16807011/python-how-to-identify-if-a-variable-is-an-array-or-a-scalar
# To support any type of sequence, check collections.Sequence instead of list.
# DONE print arrays of arrays better
# TODO print dictionaries better
# TODO change type checking to isinstance

    if note:
        console.print(note)
    if value_is_scalar:
        if value == True and value_type  == bool:
            console.print(
                "[statement]{}[/statement] of {} type == [true]{}[/true]" \
                    .format(value_name, value_type, value)
            )
        elif value == False and value_type == bool:
            console.print(
                "[statement]{}[/statement] of {} type == [false]{}[/false]" \
                    .format(value_name, value_type, value)
            )
        # elif value == None and type(value) == None:
        #     console.print(
        #         "[statement]{}[/statement] == [none]{}[/none]" \
        #             .format(statement, value))
        else:
            console.print(
                "[statement]{}[/statement] of {} type == [value]{}[/value]" \
                    .format(value_name, value_type, value)
            )
    #if not value_is_scalar:
    else:
        if isinstance(value, str):
            console.print(
                "[statement]{}[/statement] of {} type = \'{}\'" \
                    .format(value_name, value_type, value))
        if isinstance(value, list):
            value_list = value
            console.print(
                "[statement]{}[/statement] of {} type = [" \
                    .format(value_name, value_type)
            )
            for index, element in enumerate(value_list):
                element_type = type(element)
                console.print(
                    " [statement] {} [/statement] -> [value]{}[/value] of type {}" \
                        .format(index, element, element_type)
                )
            console.print(
                "[" \
            )
        elif isinstance(value, dict):
            value_dict = value
        else:
            console.print(
                    " [statement] {} [/statement] -> [value]{}[/value] of type {}" \
                    .format(value_name, value, value_type)
            )
        ...
    ...
# endregion print_logic


# TODO put function in a library
# region filter_files_by_extension
def filter_files_by_extension(
    files: list ,
    extensions: list
):
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
        file_ext = _remove_dot_from_extension(file_ext)
        for extension in extensions:
            ext = _remove_dot_from_extension(extension).lower()
            # print("ext \n", ext)
            # print("file_ext \n", file_ext)
            if file_ext == ext:
                filtered_files.append(file)

    return filtered_files
    ...
# endregion filter_files_by_extension


# TODO put function in a library
# region filter_videos
def filter_videos(
    files: list
):
    """filter a list of files to contain only video type files
    the filtering happens based on the extension of the files

    Args:
        files (list): the list of files

    Returns:
        videos (list): the list of videos
    """
#cSpell:words webm vchd rmvb gifv xvid vidx
    video_extensions = [
        "WEBM",
        "MPG","MP2", "MPEG", "MPE", "MPV",
        "OGV","OGG",
        "MP4", "M4P", "M4V",
        "AVI",
        "WMV",
        "MOV","QT",
        "FLV","SWF",
        "F4V","F4P","F4A","F4B",
        "VCHD",
        "RMVB","RM",
        "VOB",
        "MKV",
        "MTS", "M2TS", "TS",
        "MNG",
        "GIFV",
        "DRC",
        "XVID",
        "VIDX",
        "ASF",
        "AMV",
        "M2V",
        "SVI",
        "3GP",
        "MXF",
        "ROQ",
        "NSV",
        "3G2",
    ]
    return filter_files_by_extension(files, video_extensions)
    ...
# endregion filter_videos


# TODO put function in a library
# region _remove_dot_from_extension
def _remove_dot_from_extension(
    extensions
):
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
# endregion _remove_dot_from_extension


# TODO put function in a library
# region filter_subtitles
def filter_subtitles(
    files: list
):
    """filter a list of files to contain only subtitle type files
    the filtering happens based on the extension of the files

    Args:
        files (list): the list of files

    Returns:
        videos (list): the list of subtitles
    """
#cSpell:words ttml dfxp
    subtitles_extensions = [
            "srt",
            "vtt",
            "ssa",
            "ttml",
            "sbv",
            "dfxp",
    ]
    return filter_files_by_extension(files, subtitles_extensions)
    ...
# endregion filter_subtitles


# region retrieve_outermost_name
import inspect
def retrieve_outermost_name(var):
        """
        Gets the name of var. Does it from the
        out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
# endregion retrieve_outermost_name


# region process_folder
def process_folder(
    folder_path:Path,
    filter=filter_videos
    ):
    """
    do the actual work of the script on a specified folder
    using the filter to filter the files of the directory

    Args:
        folder (Path): the path to the folder to process

        filter (function): the filter function to use

    Returns:
        (Path,Path) : a tuple of paths, first is source, second is destination
    """
    # print()
    # print("+" + 80 * "-" + "+")
    # print("| def process_folder(")
    # print("| \n| folder:Path -> {}" \
    #     .format(folder_path))
    # print("| \n| filter -> {}" \
    #     .format(filter))
    # print("| \n):")

    folder_exists = os.path.isdir(folder_path)
    if folder_exists:
        all_items = os.listdir(folder_path)
        # print_logic(all_items)
        filtered_items = filter(all_items)
        # print_logic(filtered_items)

        # remove extension

        items_no_ext_list = []
        list_of_ext = []
        for item in filtered_items:
            item_no_ext, ext = os.path.splitext(item)
            items_no_ext_list.append(item_no_ext)
            list_of_ext.append(ext)

        # print_logic(items_no_ext_list)
        # print_logic(list_of_ext)

        items_padded = pad_zeroes(items_no_ext_list)

        # print_logic(items_padded)

        src_dst_paths = []
        for index, _ in enumerate(items_padded):
            src = folder_path / filtered_items[index]
            padded_item = items_padded[index] + list_of_ext[index]
            dst = folder_path / padded_item
            src_dst_paths.append((src,dst))
            ...

        # print_logic(src_dst_paths)
    else:
        # raise OSError("Folder {} does not exist.")
        src_dst_paths = None
        ...

    # print("| returning form process_folder(...)")
    # print("+" + 80 * "-" + "+")
    # print()
    return src_dst_paths
    ...
# endregion process_folder


# region main
def main():
    """main function from script

    Args:
        debug_function (bool, optional): Defaults to None.
    """
    cwd = Path(os.getcwd())

    # print_logic("cwd", cwd)

    videos_folder_path = cwd / "videos"
    converted_folder_path = cwd / "converted"
    subs_folder_path = cwd / "subs"

    # process_folder(cwd)
    files_to_move =  process_folder(videos_folder_path)
    move_files(files_to_move)

    files_to_move =  process_folder(converted_folder_path)
    move_files(files_to_move)

    files_to_move =  process_folder(subs_folder_path, filter_subtitles)
    move_files(files_to_move)

    # current_test()
# endregion main


# region move_files
def move_files(files_to_move):
    if files_to_move:
        for file in files_to_move:
            src, dst = file

            basename_src = os.path.basename(src)
            basename_dst = os.path.basename(dst)

            c = Console()
            c.print("renaming: [purple]{}[/purple] to [magenta]{}[/magenta]"\
                .format(basename_src, basename_dst))

            os.rename(src, dst)

        ...
    ...
# endregion move_files


# region current_test
def current_test():
#     input = [
#         '1_section_1_file_1',
#         '11_section_1_file_a'
#     ]
#     expected = [
#         '01_section_1_file_1',
#         '11_section_1_file_a'
#     ]
    input = [
        "1_section_part_1_name_1",
        "11_section_part_11_name_11",
        "22_section_name_222",
        "333_section",
    ]
    expected = [
        "001_section_part_001_name_01",
        "011_section_part_011_name_11",
        "022_section_name_222",
        "333_section",
    ]

    print()
    print("+ calling pad_zeroes ")
    print()
    actual = pad_zeroes(input)
    print()
    print("- calling pad_zeroes ")
    print()

    result = actual == expected

    print_logic(input)
    print_logic(expected)
    print_logic(actual)
    print_logic(result)
# endregion current_test


# region if __name__ == "__main__":
if __name__ == "__main__":
    print()
    msg = "START pad_zeroes_of_videos.py START"
    print(msg)
    print()

    main()

    msg = "END pad_zeroes_of_videos.py END"
    print()
    print(msg)
    print()
    ...
# endregion if __name__ == "__main__":


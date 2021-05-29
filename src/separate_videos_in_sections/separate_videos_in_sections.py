#! /usr/bin/env python3
"""
separate video files in sections
based on the names of the files
"""

# TODO make the print statements colored using the colored package

import os
import os.path
from pathlib import Path
import re

from rich.traceback import install
from rich.console import Console, ConsoleDimensions
from rich import print,inspect
install()

CONSOLE = Console(record=True)


def print_begin_end_debug(
    input: str,
    begin: int,
    end: int
    ):

    # CONSOLE.print("def print_begin_end_debug(")
    CONSOLE.print( "string = " + input)
    space_in_between = end - begin - 1
    if begin == end:
        CONSOLE.print( " start ──" + "─" * begin + "┴─ end")
    else:
        CONSOLE.print( " start ──" + "─" * begin + "┘" + " " * space_in_between + "└─ end")


# region get_number_location
def get_number_location(
    input : str,
    debug_function : bool = False
    ):
    """
    get the string indices of all numbers that occur on the string

    format example: [ ( 0, 1 ), ( 4, 6 ), ( 9, 9 ) ]

    both begin and end are inclusive, in contrast with the way the std_lib does it
    which is begin(inclusive), end(exclusive)
    """
    # debug_function = True # comment to toggle

    if debug_function:
        CONSOLE.print("def get_number_location(input : str):")
        CONSOLE.print(f"  input = {input}")

    locations = []
    for match in re.finditer("\d+", input):

        if debug_function:
            CONSOLE.print()
            CONSOLE.print("for match in re.finditer(...):")

        value = match.group(0)
        # match start is inclusive
        position_start = match.start()
        # match end is exclusive
        position_end = match.end() - 1

        locations.append((position_start, position_end))

        if debug_function:
            CONSOLE.print(f"value: {value}")
            CONSOLE.print(f"position_start: {position_start}")
            CONSOLE.print(f"position_end: {position_end}")
            CONSOLE.print()
            print_begin_end_debug(input, position_start, position_end)
            CONSOLE.print()

        ...
    ...
    if debug_function:
        CONSOLE.print(locals())

    return locations
# endregion get_number_location


# BUG
# {'file_2': ['file_2'], 'file_1': ['file_1']}
# should be:
# {'file_': ['file_2' , 'file_1']}
#
# region separate_into_sections
def separate_into_sections(
    input_list : list,
    debug_function : bool = False
    ) -> dict:
    """separates a list of strings into sections

    Args:
        input_list (list): the input list

    Returns:
        dict: lists separated in categories
    """

    # debug_function = True # comment to toggle

    if debug_function:
        CONSOLE.log()
        CONSOLE.log("def separate_into_sections(input_list : list) -> dict:")
        CONSOLE.log(f"  input_list : list = {input_list}")
        CONSOLE.log()

    # prepare the data structure
    input_list_data = {}
    for element in input_list:
        input_list_data[element] = {
            "number locations" : [],
            "sections" : []
        }

    for key, value in input_list_data.items():
        if debug_function:
            print()
            CONSOLE.log(f"key: {key} , value : {value} ")

        # add number locations to data structure
        input_list_data[key]["number locations"] \
            = get_number_location(key)
        number_locations = input_list_data[key]["number locations"]

        # add sections to data structure
        input_list_data[key]["sections"] \
            = sections_from_number_locations(key, number_locations)
        if debug_function:
            CONSOLE.log(f"key: {key} , value : {value} ")

    common_sections = set()
    for key, value in input_list_data.items():
        if debug_function:
            print("key {}".format(key))
            print("value {}".format(value))

        if value["sections"]:
            common_sections.add(input_list_data[key]["sections"][0])
        else:
            common_sections.add(key)

    sections = {}
    for common_section in common_sections:
        sections[common_section] = []

    for section in common_sections:
        for input in input_list:
            if section in input:
                sections[section].append(input)
            ...
        ...
    # print(locals())

    if debug_function:
        CONSOLE.log()
        CONSOLE.log("locals: ")
        CONSOLE.log()
        CONSOLE.log(locals())
    return sections
    ...
# endregion separate_into_sections


# BUG the last character of a section is missing
#
# region sections_from_number_locations
def sections_from_number_locations(
    string : str,
    number_locations : list,
    debug_function : bool = False
    ):
    """
    get the characters from a string and separate those into sections
    separated by numbers
    """

    # debug_function = True # comment to toggle

    sections = []
    for index, location in enumerate(number_locations):
        begin_of_number, end_of_number = location

        section = ""
        # we are at the start of the string,
        # so the string starts with a number
        # se we want to go from the first
        # number to the last non number
        if debug_function:
            CONSOLE.log("begin_of_number")
            CONSOLE.log(begin_of_number)

        if begin_of_number == 0 and index == 0:
            starts_with_number = True
            last_non_number_before_numbers = \
                number_locations[index + 1][0] - 1

            last_index = len(number_locations) - 1
            if index == last_index:
                section += string[begin_of_number:]
            else:
                section += string[begin_of_number : \
                                last_non_number_before_numbers]

        # the string starts with a non-number or is not
        # so the section need to be from the first non-number before
        # to the end of this number
        elif index == 0:
            starts_with_number = False
            first_non_number_before_numbers = 0

            if debug_function:
                CONSOLE.log("first_non_number_before_numbers")
                CONSOLE.log(first_non_number_before_numbers)

            last_index = len(number_locations) - 1
            if index == last_index:
                section += string[first_non_number_before_numbers:-1]
            else:
                section += string[first_non_number_before_numbers: \
                                    end_of_number]

        # not on the first number occurrence
        # always get the number then the letters
        else:
            last_non_number_after_number = len(string) - 1
            last_index = len(number_locations) - 1
            if index == last_index:
                last_non_number_after_number = len(string)
            else:
                last_non_number_after_number = number_locations[index + 1][1] - 1
            section += string[begin_of_number : last_non_number_after_number]
            if debug_function:
                print_begin_end_debug(
                    string,
                    begin_of_number,
                    last_non_number_after_number)

        sections.append(section)

    for index, section in enumerate(sections):
        # print(section)
        sections[index] = remove_trailing_whitespace(section)
    if debug_function:
        print(sections)

    return sections
    ...
# endregion sections_from_number_locations


# region
def remove_trailing_whitespace(input: str):
    last_index = len(input) - 1
    if " " in input[last_index] \
    or "_" in input[last_index]:
        input = input[:-1]

    return input

# endregion


# region main
def main():
    cwd = os.getcwd()
    # print()
    # print("current_working_directory:")
    # print(cwd)
    # print()
    CONSOLE.log()
    CONSOLE.log("current_working_directory:")
    CONSOLE.log(cwd)
    CONSOLE.log()
# endregion main


# region if __name__ == "__main__":
if __name__ == "__main__":
    msg = "START separate_videos_in_sections START"

    # CONSOLE.log()
    # CONSOLE.log(msg)
    # CONSOLE.log()

    try:
        main()
    except:
        CONSOLE.print.exception()

    msg = "END separate_videos_in_sections END"

    # CONSOLE.log()
    # CONSOLE.log(msg)
    # CONSOLE.log()

    CONSOLE.save_html(str(os.getcwd()) + "/last_run.html")

# endregion if __name__ == "__main__":

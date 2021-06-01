#! /usr/bin/env python3
"""
separate video files in sections
based on the names of the files
"""

import os
import os.path
from pathlib import Path
import re

import snoop
from rich.traceback import install
from rich.console import Console, ConsoleDimensions
from rich import print,inspect
install()

CONSOLE = Console(record=True)


# region print_begin_end_debug
# region print_begin_end_debug header
def print_begin_end_debug(
    input: str,
    begin: int,
    end: int
    ):
# endregion print_begin_end_debug header
# region print_begin_end_debug docstring
    """print the begin index and end index of a string input, the
    with the string in one line and markers on the next line

    Args:
        input (str): [description]
        begin (int): [description]
        end (int): [description]

    Returns:
        [type]: [description]
    """
# endregion print_begin_end_debug docstring
# region print_begin_end_debug implementation
    CONSOLE.log( "string = " + input)
    space_in_between = end - begin - 1
    if begin == end:
        CONSOLE.log( " start ──" + "─" * begin + "┴─ end")
    else:
        CONSOLE.log( " start ──" + "─" * begin + "┘" + " " * space_in_between + "└─ end")

# endregion print_begin_end_debug implementation
# endregion print_begin_end_debug


# region print_index_of_string
# region print_index_of_string header
def print_index_of_string(
    input_string,
    index
    ):
# endregion print_index_of_string header
# region print_index_of_string docs
    """prints the string in one line
    and mark the index in the line below

    Args:
        input_string (str):
        index (int):
    """
# endregion print_index_of_string docs
# region print_index_of_string implementation
    index_position = " " * index + "|"
    CONSOLE.log("  string: {}".format(input_string))
    CONSOLE.log("  ....... {}".format(index_position))
# endregion print_index_of_string implementation
# endregion print_index_of_string


# region get_number_location
# region get_number_location header
def get_number_location(
    input : str,
    ):
# endregion get_number_location header
# region get_number_location docs
    """
    get the string indices of all numbers that occur on the string

    format example: [ ( 0, 1 ), ( 4, 6 ), ( 9, 9 ) ]

    both begin and end are inclusive, in contrast with the way the std_lib does it
    which is begin(inclusive), end(exclusive)
    """
# endregion get_number_location docs
# region get_number_location implementation
    locations = []
    for match in re.finditer("\d+", input):
        # match start is inclusive
        position_start = match.start()
        # match end is exclusive
        position_end = match.end() - 1
        locations.append((position_start, position_end))
        ...
    return locations
# endregion get_number_location implementation
# endregion get_number_location


# region add_keys_with_empty_list_values
def add_keys_with_empty_list_values(
    list: list,
    keys: list
    ):

    new_list = {}

    for element in list:
        dictionary = {}
        for key in keys:
            dictionary[key] = []

        new_list[element] = dictionary
    return new_list
    ...
# endregion add_keys_with_empty_list_values

# region get_list_data(
def get_list_data(input_list):
    # prepare the data structure
    input_list_data = add_keys_with_empty_list_values(
        input_list,
        [
            "number locations",
            "sections"
        ])
    for key, value in input_list_data.items():
        # add number locations to data structure
        input_list_data[key]["number locations"] \
            = get_number_location(key)
        number_locations = input_list_data[key]["number locations"]
        # add sections to data structure
        input_list_data[key]["sections"] \
            = sections_from_number_locations(key, number_locations)
    return input_list_data
    ...
# endregion get_list_data(


# region separate_into_sections
# region separate_into_sections header
def separate_into_sections(
    input_list : list,
    ) -> dict:
# endregion separate_into_sections header
# region separate_into_sections docs
    """separates a list of strings into sections

    Args:
        input_list (list): the input list

    Returns:
        dict: lists separated in categories
    """
# endregion separate_into_sections docs
# region separate_into_sections implementation
    input_list_data = get_list_data(input_list)
    unique_first_sections = set()
    for _, value in input_list_data.items():
        sections = value["sections"]
        first_section = sections[0]
        unique_first_sections.add(first_section)
    sections = {}
    for section in unique_first_sections:
        sections[section] = []
        for input_name in input_list:
            if input_name.startswith(section):
                sections[section].append(input_name)
                ...
            ...
        ...
    return sections
# endregion separate_into_sections implementation
# endregion separate_into_sections


# region sections_from_number_locations
# region sections_from_number_locations header
def sections_from_number_locations(
    string : str,
    number_locations : list,
    debug_function : bool = False
    ):
# endregion sections_from_number_locations header
# region sections_from_number_locations docs
    """
    get the characters from a string and separate those into sections
    separated by numbers
    """
# endregion sections_from_number_locations docs
# region sections_from_number_locations implementation

    # debug_function = True # comment to toggle

# region number_then_letters
# region number_then_letters header
    def number_then_letters(
        index,
        location
        ):
# endregion number_then_letters header
# region number_then_letters docstring
        """given the example string:

        01_section_01_subsection_1

        returns:
        01_section_

        Args:
            index (): the index of the numbers
            location (): the location of the numbers

        Returns:
            str : the substring representing the section
        """
# endregion number_then_letters docstring
# region number_then_letters implementation
        begin_of_number, _ = location
        last_non_number_before_numbers = \
            number_locations[index + 1][0] - 1

        section = ""
        last_index = len(number_locations) - 1
        if index == last_index:
            section += string[begin_of_number:]
        else:
            section += string[begin_of_number : \
                            last_non_number_before_numbers]

        return section
        ...
# endregion number_then_letters implementation
# endregion number_then_letters


# region letters_then_numbers
# region letters_then_numbers header
    def letters_then_numbers(
        location_index,
        location,
        debug_function: bool = False
        ):
# endregion letters_then_numbers header
# region letters_then_numbers docstring
        """given the example string:

        section_01_subsection_1

        returns:
        section_01

        Args:
            index (): the index of the numbers
            location (): the location of the numbers

        Returns:
            str : the substring representing the section
        """
# endregion letters_then_numbers docstring
# region letters_then_numbers implementation
        debug_function = True # comment to toggle
        _ , end_of_number = location
        section = ""
        begin, end = (0, 0)
        last_location_index = len(number_locations) - 1
        begin_of_non_numbers = 0
        # to get the first index of the last non numbers:
        # get the index of the last number of the index before
        # and add one to it
        if location_index != 0 and location_index != last_location_index:
            previous_location_index = location_index - 1
            _ , end_of_last_number = number_locations[previous_location_index]
            begin_of_non_numbers = end_of_last_number + 1
            begin = begin_of_non_numbers
            end = end_of_number
        if location_index != 0 and location_index == last_location_index:
            _ , end_of_last_number = number_locations[location_index - 1]
            begin_of_non_numbers = end_of_last_number + 1
            end_of_string_index = len(string) - 1
            begin = begin_of_non_numbers
            end = end_of_string_index
        elif location_index == 0:
            begin = 0
            end = end_of_number
        section += string[begin:end + 1]
        return section
# endregion letters_then_numbers implementation
# endregion letters_then_numbers
    sections = []
    starts_with_number = None
    for index, location in enumerate(number_locations):
        begin_of_number, end_of_number = location
        section = ""
        # start of string
        if index == 0:
            # string starts with number
            if begin_of_number == 0:
                starts_with_number = True
                section = number_then_letters(index, location)
            # the string starts with a non-number
            else:
                starts_with_number = False
                section = letters_then_numbers(index, location)
        # not on the first number occurrence
        else:
            if starts_with_number == None:
                raise Exception \
        ("Something wrong happened!\nstarts_with_number == None")
            if starts_with_number == False:
                # section is letters then numbers
                section = letters_then_numbers(index, location)
            if starts_with_number == True:
                # section is number then letters
                section = number_then_letters(index, location)
        sections.append(section)
    for index, section in enumerate(sections):
        sections[index] = remove_trailing_whitespace(section)
    return sections
# endregion sections_from_number_locations implementation
# endregion sections_from_number_locations


# region remove_trailing_whitespace
# region remove_trailing_whitespace header
def remove_trailing_whitespace(
    input: str
    ):
# endregion remove_trailing_whitespace header
# region remove_trailing_whitespace docs
    """removes whitespace (SPACE and _) from the end of the input

    Args:
        input (str): the input string

    Returns:
        (str): the input without the trailing whitespace
    """
# endregion remove_trailing_whitespace docs
# region remove_trailing_whitespace implementation
    if input:
        last_index = len(input) - 1
        if " " in input[last_index] \
        or "_" in input[last_index]:
            input = input[:-1]

    return input
# endregion remove_trailing_whitespace implementation
# endregion remove_trailing_whitespace


# region main
def main():
    cwd = os.getcwd()
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
        CONSOLE.print_exception()

    msg = "END separate_videos_in_sections END"

    # CONSOLE.log()
    # CONSOLE.log(msg)
    # CONSOLE.log()

# endregion if __name__ == "__main__":


# region current_manual_test
def current_manual_test():

    CONSOLE.print(" ==============================================")
    CONSOLE.print("test_have_three_files_should_return_two_sections")
    CONSOLE.print(" ==============================================")

    # setup

    input = [
        "section_1_subsection_1_file_1",
        "section_1_subsection_2_file_2",
        "section_2_subsection_1_file_3"
    ]

    expected_output = {
        "section_1" : [
            "section_1_subsection_1_file_1",
            "section_1_subsection_2_file_2"
        ],
        "section_2" : [
            "section_2_subsection_1_file_3"
        ]
    }

    CONSOLE.print(" ==============================================")
    CONSOLE.print("calling separate_into_sections(input)")
    CONSOLE.print(" ==============================================")

    # act
    actual_output = separate_into_sections(input)

    CONSOLE.print(" ==============================================")
    CONSOLE.print("called separate_into_sections(input)")
    CONSOLE.print(" ==============================================")
    CONSOLE.print("")
    CONSOLE.log("input")
    CONSOLE.log(input, )

    CONSOLE.print("")
    CONSOLE.log("expected_output")
    CONSOLE.log(expected_output)

    CONSOLE.print("")
    CONSOLE.log("actual_output")
    CONSOLE.log(actual_output)

    CONSOLE.print("")
    CONSOLE.log("are equal?")
    CONSOLE.log(actual_output == expected_output)

    CONSOLE.print(" ==============================================")
    CONSOLE.print("test_have_three_files_should_return_two_sections")
    CONSOLE.print(" ==============================================")

    ...
# endregion current_manual_test


current_manual_test()

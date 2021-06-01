#! /usr/bin/env python3
"""
tests for separate_videos_in_sections.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass


import separate_videos_in_sections as script

USERNAME = getpass.getuser()
PROJECT_FOLDER \
    = Path("/home/") \
    / USERNAME \
    / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
    / "src" \
    / "separate_videos_in_sections" \
    / "test_bed"


# FIXME bug:
#             sections = value["sections"]
# >           first_section = sections[0]
# E           IndexError: list index out of range
# separate_videos_in_sections.py:169: IndexError
# test_separate_videos_in_sections.py:42:

# corner case: where the list of locations is empty
# because there is no numbers


# region test_input_have_1_file_should_return_1_section
def test_input_have_1_file_should_return_1_section():
    # setup
    input = [
        "single_file"
    ]

    expected_output = {
        "single_file" : [
            "single_file"
        ]
    }

    # act
    actual_output = script.separate_into_sections(input)

    # assert
    assert expected_output == actual_output
    ...
# endregion test_input_have_1_file_should_return_1_section


# region test_have_3_files_should_return_2_sections_1_digit
def test_have_3_files_should_return_2_sections_1_digit():
    # setup
    input = [
        "section_1_file_1",
        "section_1_file_2",
        "section_2_file_1"
    ]

    expected_output = {
        "section_1" : [
            "section_1_file_1",
            "section_1_file_2"
        ],
        "section_2" : [
            "section_2_file_1"
        ]
    }

    # act
    actual_output = script.separate_into_sections(input)

    # assert
    assert expected_output == actual_output
    ...
# endregion test_have_3_files_should_return_2_sections_1_digit


# region test_have_3_files_should_return_2_sections_2_digits
def test_have_3_files_should_return_2_sections_2_digits():
    # setup
    input = [
        "section_01_file_01",
        "section_01_file_02",
        "section_02_file_01"
    ]

    expected_output = {
        "section_01" : [
            "section_01_file_01",
            "section_01_file_02"
        ],
        "section_02" : [
            "section_02_file_01"
        ]
    }

    # act
    actual_output = script.separate_into_sections(input)

    # assert
    assert expected_output == actual_output
    ...
# endregion test_have_3_files_should_return_2_sections_2_digits


# region test_input_have_3_files_should_return_2_section_no_number_at_the_end
def test_input_have_3_files_should_return_2_section_no_number_at_the_end():
    # setup
    input = [
        "section_1_file_a",
        "section_1_file_b",
        "section_2_file_a"
    ]

    expected_output = {
        "section_1" : [
            "section_1_file_a",
            "section_1_file_b"
        ],
        "section_2" : [
            "section_2_file_a"
        ]
    }

    # act
    actual_output = script.separate_into_sections(input)

    # assert
    assert expected_output == actual_output

    ...
# endregion test_input_have_3_files_should_return_2_section_no_number_at_the_end


from birdseye import eye

# region test_input_have_3_files_should_return_2_sections_3_sets_of_numbers_in_each_file

# @eye
def test_input_have_3_files_should_return_2_sections_3_sets_of_numbers_in_each_file():
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

    # act
    actual_output = script.separate_into_sections(input)

    # assert
    assert expected_output == actual_output

    # BUG

        # assert
# >       assert expected_output == actual_output
# E       AssertionError: assert {'section_1':...on_1_file_3']} == {'section_1':...on_1_file_3']}
# E         Differing items:
# E         {'section_1':
#               ['section_1_subsection_1_file_1',
#                'section_1_subsection_2_file_2']}
# !=
#           {
#             'section_1':
#               ['section_1_subsection_1_file_1',
#                'section_1_subsection_2_file_2',
#                'section_2_subsection_1_file_3'
#               ]
#           }

# E         {
#            'section_2':
#            [
#               'section_2_subsection_1_file_3'
#            ]
#           }
# !=
#           {
#           'section_2':
#           [
#           'section_1_subsection_2_file_2',
#           'section_2_subsection_1_file_3'
#           ]
#           }
# E         Use -v to get the full dif
    ...
# endregion test_input_have_3_files_should_return_2_sections_3_sets_of_numbers_in_each_file


if __name__ == "__main__":
    unittest.main()

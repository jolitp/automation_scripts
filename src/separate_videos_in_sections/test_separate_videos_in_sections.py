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



# region test_input_have_one_file_should_return_one_section
def test_input_have_one_file_should_return_one_section():
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
# endregion test_input_have_one_file_should_return_one_section


# region input_have_two_files_should_return_two_sections
def test_input_have_two_files_should_return_two_sections():
    # setup
    input = [
        "file_1",
        "file_2",
    ]

    expected_output = {
        "file" : [
            "file_1",
            "file_2",
        ]
    }

    # act
    actual_output = script.separate_into_sections(input)

    # assert
    assert expected_output == actual_output
    ...
# endregion input_have_two_files_should_return_two_sections


# region test_have_three_files_should_return_two_sections
def test_have_three_files_should_return_two_sections():
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

    # BUG
    #  # assert
# >       assert expected_output == actual_output
# E       AssertionError:
# assert {'section_1':...on_2_file_1']}
#                     ==
#        {'section': [...on_2_file_1']}

# E         Left contains 2 more items:
# E {'section_1':
#      ['section_1_file_1',
#       'section_1_file_2'],
# E  'section_2':
#      ['section_2_file_1']}

# E         Right contains 1 more item:
# E {'section':
#      ['section_1_file_1',
#       'section_1_file_2',
#       'section_2_file_1']}
# E         Use -v to get the full diff


    ...
# endregion test_have_three_files_should_return_two_sections



if __name__ == "__main__":
    unittest.main()

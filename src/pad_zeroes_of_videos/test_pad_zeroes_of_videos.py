#! /usr/bin/env python3
"""
tests for pad_zeroes_of_videos.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import pad_zeroes_of_videos as script

USERNAME = getpass.getuser()
PROJECT_FOLDER \
    = Path("/home/") \
        / USERNAME \
        / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
        / "src" \
        / "pad_zeroes_of_videos" \
        / "test_bed"

def test_dummy():
    assert True

if __name__ == "__main__":
    unittest.main()


# region test_separate_name_receives_allowed_value_returns_expected_value
# region test_separate_name_receives_allowed_value_returns_expected_value header
@pytest.mark.parametrize(
    # setup
    "input, expected_output",
    [
        ("test", ["test"]),
        ("01_test", ["01", "_test"]),
        ("01_test_1", ["01", "_test_", "1"]),
        ("start 01_test_1", ["start ", "01", "_test_", "1"]),
        ("filename.mp4", ["filename.mp", "4"] )
    ]
)
def test_separate_name_receives_allowed_value_returns_expected_value(
    input: str,
    expected_output:list
):
# endregion test_separate_name_receives_allowed_value_returns_expected_value header
# region test_separate_name_receives_allowed_value_returns_expected_value docstring
    """
    do a battery of tests on separate_name()

    all calls receive allawed values

    result is compared with expected values
    """
# endregion test_separate_name_receives_allowed_value_returns_expected_value docstring
# region test_separate_name_receives_allowed_value_returns_expected_value implementation
    # act
    result_output = script.separate_name(input)

    # assert
    assert result_output == expected_output
    ...
# endregion test_separate_name_receives_allowed_value_returns_expected_value implementation
# endregion test_separate_name_receives_allowed_value_returns_expected_value




# region test_pad_zeroes_receives_allawed_values_returns_expected_results
# region test_pad_zeroes_receives_allawed_values_returns_expected_results header
@pytest.mark.parametrize(
    # setup
    # names
    "input, expected_output",
    # values
    [
        # test 1
        (
            [
                '1_file_1',
                '11_file_1'
            ],
            [
                '01_file_1',
                '11_file_1'
            ]
        ),
        # test 2
        (
            [
                '1_section_1_file_1',
                '11_section_1_file_a'
            ],
            [
                '01_section_1_file_1',
                '11_section_1_file_a'
            ]
        ),
        # test 3
        (
            [
                '11_section_1_file_1',
                '11_section_01_file_a'
            ],
            [
                '11_section_01_file_1',
                '11_section_01_file_a'
            ]
        ),
        # test 3
        (
            [
                '01_section_1_file_1_part_1',
                '1_section_1_file_1_part_2',
                '01_section_1_file_2',
                '1_section_03_file_1',
                '1_section_03_file_1',
                '11_section_1_file_1_part_a',
                '22_section_2_file_3_part_1'
            ],
            [
                '01_section_01_file_1_part_1',
                '01_section_01_file_1_part_2',
                '01_section_01_file_2',
                '01_section_03_file_1',
                '01_section_03_file_1',
                '11_section_01_file_1_part_a',
                '22_section_02_file_3_part_1'
            ]
        ),
        (
            [
                "1_section_part_1_name_1",
                "11_section_part_11_name_11",
                "22_section_name_222",
                "333_section",
            ],
            [
                "001_section_part_001_name_01",
                "011_section_part_011_name_11",
                "022_section_name_222",
                "333_section",
            ]
        )
# E       AssertionError:
# assert [
    # '001_section_part_1_name_1',\n
    # '011_section_part_11_name_11',\n
    # '022_section_name_222',\n
    # '333_section'
    # ]
    # ==
    # [
    # '001_section_part_001_name_01',\n
    # '011_section_part_011_name_11',\n
    # '022_section_name_222',\n
    # '333_section']
# E         At index 0 diff:
#           '001_section_part_1_name_1'
# !=
#           '001_section_part_001_name_01'

# E         Full diff:
# E           [
# E         -  '001_section_part_001_name_01',
# E         ?                    --       -
# E         +  '001_section_part_1_name_1',
# E         -  '011_section_part_011_name_11',
# E         ?                    -
# E         +  '011_section_part_11_name_11',
# E            '022_section_name_222',
# E            '333_section',
# E           ]

# test_pad_zeroes_of_videos.py:171: AssertionError
    ]
)
def test_pad_zeroes_receives_allawed_values_returns_expected_results(
    input: list,
    expected_output:list
):
# endregion test_pad_zeroes_receives_allawed_values_returns_expected_results header
# region test_pad_zeroes_receives_allawed_values_returns_expected_results docstring
    """
    do a battery of tests on pad_zeroes()

    all calls receive allawed values

    result is compared with expected values
    """
# endregion test_pad_zeroes_receives_allawed_values_returns_expected_results docstring
# region test_pad_zeroes_receives_allawed_values_returns_expected_results implementation
    # act
    result_output = script.pad_zeroes(input)

    # print("expected_output")
    # print(expected_output)
    # assert
    assert result_output == expected_output
    ...
# endregion test_pad_zeroes_receives_allawed_values_returns_expected_results implementation
# endregion test_pad_zeroes_receives_allawed_values_returns_expected_results

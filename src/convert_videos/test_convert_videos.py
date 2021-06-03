#! /usr/bin/env python3
"""
tests for convert_videos.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import convert_videos as script

USERNAME = getpass.getuser()
PROJECT_FOLDER \
    = Path("/home/") \
        / USERNAME \
        / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
        / "src" \
        / "convert_videos" \
        / "test_bed"


# # region test_dummy
# def test_dummy():
#     assert True

# # endregion test_dummy


# region test_dummy
@pytest.mark.parametrize(
    "input, expected_output",
    # setup
    [
        # test 1
        (
            # input
            [
                (1920, 1080),
                (1920, 1080),
                (1080, 720),
            ],
            # expected_output
            (1920, 1080)
        )
    ]
)
def test_most_frequent_dimension_should_return_expected_values(
    input:list,
    expected_output
):
    # act
    actual_output = script.most_common_dimension(input)
    # assert
    assert actual_output == expected_output

# endregion test_dummy



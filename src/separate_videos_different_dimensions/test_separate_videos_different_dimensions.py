#! /usr/bin/env python3
"""
tests for separate_videos_different_dimensions.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import separate_videos_different_dimensions as script

USERNAME = getpass.getuser()
PROJECT_FOLDER \
    = Path("/home/") \
        / USERNAME \
        / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
        / "src" \
        / "separate_videos_different_dimensions " \
        / "test_bed"

def test_dummy():
    assert True

@pytest.mark.parametrize(
    # paramaeter names
    "input, expected_result",
    # parameter values
    [
        # 1st test
        (
            # input
            [
                ('320', '240'),
                ('320', '240'),
            ],
            # expected_result
            [
                (0,1)
            ]
        ),
        # 2nd test
        (
            # input
            [
                (1920,1080),
                (1920,1080),
                (1080,720),
                (1080,720),
                (1920,1080),
                (1920,1080),
            ],
            # expected_result
            [
                (0,1),
                (2,3),
                (4,5)
            ]
        ),
    ]
) # setup
def test_segment_by_dimensions_should_return_expected_result(
    input,
    expected_result
):
    # act
    output = script.segment_by_dimensions(input)

    # assert
    assert expected_result == output
    ...


if __name__ == "__main__":
    unittest.main()



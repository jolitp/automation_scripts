#! /usr/bin/env python3
"""
tests for separate_videos_subs_files.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import separate_videos_subs_files

USERNAME = getpass.getuser()
PROJECT_FOLDER = Path("/home/") / USERNAME / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER / "src" / "separate_videos_subs_files" / "test_bed"

test_folder = TEST_BED_FOLDER_PATH \
    / "test_get_files_should_return_expected_files/"

# region parameters
@pytest.mark.parametrize(
    "folder,expected_files",
    [
    # setup
        (
            "no_files_nor_folders",
            [],
        ),
        (
            "no_files_one_folder",
            [],
        ),
        (
            "no_files_two_folders",
            [],
        ),
        (
            "one_file_no_folders",
            [
                str(test_folder) + "single_file"
            ],
        ),
        (
            "one_file_one_folder",
            [
                str(test_folder) + "single_file"
            ],
        ),
        (
            "two_files_no_folders",
            [
                str(test_folder) + "file_one",
                str(test_folder) + "file_two"
            ],
        ),
        (
            "two_files_one_folder",
            [
                str(test_folder) + "file_one",
                str(test_folder) + "file_two"
            ],
        )
    ]
)
# endregion parameters
def test_get_files_should_return_expected_files(
    folder, expected_files
    ):
    """
    do a battery of test with files in nested folders,
    should return the expected values.

    not event testing with videos, just generic files.
    """
    # act
    # full_path = str(test_folder) + "/" + str(folder)

    # files_in_folder = separate_videos_subs_files \
    #     .get_nested_files(full_path)
    # expected_file_list = []
    # for file in expected_files:
    #     expected_file_list.append(file)

    # assert
        # assert files_in_folder == expected_file_list

    # assert len(files_in_folder) == len(expected_file_list)
    # assert all([a == b for a, b in zip(files_in_folder, expected_file_list)])


@pytest.mark.parametrize("files, extensions, expected", [
    # setup
    (
        [],
        [],
        []),
    (
        ["text.txt"],
        ["txt"],
        ["text.txt"]),
    (
        ["text.txt", "no_extension_file"],
        ["txt"],
        ["text.txt"],
    ),
    (
        ["/home/user/absolute_path_file.txt"],
        ["txt"],
        ["/home/user/absolute_path_file.txt"],
    ),
    (
        ["text.txt", "file_with_close_extension.tx"],
        ["txt"],
        ["text.txt"],
    ),
    (
        ["text.txt", "file_with_close_extension._txt"],
        ["txt"],
        ["text.txt"],
    ),
    (
        ["text.txt"],
        ["TXT"],
        ["text.txt"],
    )
])
def test_filter_files_by_extension_should_return_expected_values(
    files, extensions, expected
):
    """
    do a battery of tests with lists of files and lists of extensions.
    should return expected values.
    """
    # act
    result = separate_videos_subs_files \
        .filter_files_by_extension(files, extensions)

    # assert
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


if __name__ == "__main__":
    unittest.main()
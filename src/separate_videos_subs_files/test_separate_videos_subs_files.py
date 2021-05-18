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


# region test_get_files_should_return_expected_files
test_get_files_should_return_expected_files_folder = TEST_BED_FOLDER_PATH \
    / "test_get_files_should_return_expected_files/"
@pytest.mark.parametrize(
    "folder,expected_files", [
    # setup
    # test
    ("no_files_nor_folders", [],),
    # test
    ("no_files_one_folder", [],),
    # test
    ("no_files_two_folders", [],),
    # test
    ("one_file_no_folders",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "one_file_no_folders" + "/" + \
    "single_file"],),
    # test
    ("one_file_one_folder",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "one_file_one_folder" + "/" + \
    "single_file"],),
    # test
    ("two_files_no_folders",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_no_folders" + "/" + \
    "file_one",
    str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_no_folders" + "/" + \
    "file_two"],),
    # test
    ("two_files_one_folder",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_one_folder" + "/" + \
    "file_one",
    str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_one_folder" + "/" + \
    "file_two"],),
])
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
    print("folder: \n" + str(folder))
    print("expected_files: \n" + str(expected_files))
    full_path = str(test_get_files_should_return_expected_files_folder) + "/" + str(folder)

    print("full path: \n" + str(full_path))
    files_in_folder = separate_videos_subs_files \
        .get_nested_files(full_path)
    print("files in folder: " + str(files_in_folder))

    # assert
    assert len(files_in_folder) == len(expected_files)
    assert sorted(files_in_folder) == sorted(expected_files)
# endregion

# region test_filter_files_by_extension_should_return_expected_values
@pytest.mark.parametrize("files, extensions, expected", [
    # setup

    # test
    ([],[],[]),
    # test
    (["text.txt"],["txt"],["text.txt"]
    ),
    # test
    (["text.txt", "no_extension_file"],
    ["txt"],
    ["text.txt"],
    ),
    # test
    (["/home/user/absolute_path_file.txt"],
    ["txt"],
    ["/home/user/absolute_path_file.txt"],
    ),
    # test
    (["text.txt", "file_with_close_extension.tx"],
    ["txt"],
    ["text.txt"],
    ),
    # test
    (["text.txt", "file_with_close_extension._txt"],
    ["txt"],
    ["text.txt"],
    ),
    # test
    (["text.txt"],
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
# endregion



if __name__ == "__main__":
    unittest.main()
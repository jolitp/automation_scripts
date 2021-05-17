#! /usr/bin/env python3
"""
tests for separate_videos_subs_files.py
"""

import unittest
from pathlib import Path
import getpass

import separate_videos_subs_files

USERNAME = getpass.getuser()
PROJECT_FOLDER = Path("/home/") / USERNAME / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER / "src" / "separate_videos_subs_files" / "test_bed"

class Tests_separate_videos_subs_files(unittest.TestCase):
    """
    tests for separate_videos_subs_files.py
    """


    def test_get_files_should_return_expected_files(self):
        """
        do a battery of test with files in nested folders,
        should return the expected values.

        not event testing with videos, just generic files.
        """

        # setup
        test_folder = TEST_BED_FOLDER_PATH / "test_get_files_should_return_expected_files"
        folders = [
            "no_files_nor_folders",
            "no_files_one_folder",
            "no_files_two_folders",
            "one_file_no_folders",
            "one_file_one_folder",
            "two_files_no_folders",
            "two_files_one_folder",
        ]
        expected_results_only_names = [
            [],
            [],
            [],
            ["single_file"],
            ["single_file"],
            ["file_one", "file_two"],
            ["file_one", "file_two"],
        ]
        # act
        for index, folder in enumerate(folders):
            full_path = str(test_folder) + "/" + str(folder)

            files_in_folder = separate_videos_subs_files \
                .get_nested_files(full_path)
            expected_file_list = []
            for file in expected_results_only_names[index]:
                expected_file_list.append(str(test_folder) + "/" + folder + "/" + file)

        # assert
            self.assertCountEqual(files_in_folder, expected_file_list)


    def test_filter_files_by_extension_should_return_expected_values(self):
        """
        do a battery of tests with lists of files and lists of extensions.
        should return expected values.
        """
        # setup
        lists_of_files = [
            [],
            ["text.txt"],
            ["text.txt", "no_extension_file"],
            ["/home/user/absolute_path_file.txt"],
            ["text.txt", "file_with_close_extension.tx"],
            ["text.txt", "file_with_close_extension._txt"],
        ]
        lists_of_extensions = [
            [],
            ["txt"],
            ["txt"],
            ["txt"],
            ["txt"],
            ["txt"],
        ]

        lists_of_expected_results = [
            [],
            ["text.txt"],
            ["text.txt"],
            ["/home/user/absolute_path_file.txt"],
            ["text.txt"],
            ["text.txt"],
        ]
# TODO testcase: mismatch case
# TODO change tests to parameterized tests
        # act
        for index, list_ in enumerate(lists_of_files):
            result = separate_videos_subs_files \
                .filter_files_by_extension(list_, lists_of_extensions[index])
            expected_result = lists_of_expected_results[index]

        # assert
            self.assertCountEqual(result, expected_result)
            ...
        ...


if __name__ == "__main__":
    unittest.main()
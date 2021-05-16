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

if __name__ == "__main__":
    unittest.main()
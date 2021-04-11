#! /usr/bin/python3
"""
    tests for youtube_upload_viability_without_concatenating.py
"""

import os
import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/multiple_files_operations/youtube_upload_viability_without_concatenating/"
spec = importlib.util.spec_from_file_location("youtube_upload_viability_without_concatenating",
    python_scripts_folder_path + subfolder + "youtube_upload_viability_without_concatenating.py")
youtube_upload_viability_without_concatenating = importlib.util.module_from_spec(spec)
spec.loader.exec_module(youtube_upload_viability_without_concatenating)



# region class IntegrationTest(unittest.TestCase):

class IntegrationTestYoutubeUploadViabilityWithoutConcatenating(unittest.TestCase):
    """
        integration tests for youtube_upload_viability_without_concatenating.py
    """
# region tests is_folder(...):


# DONE testcase: passing a relative path to is_folder() raise ValueError exception
# TODO testcase: passing a folder that does not exist to is_folder() returns false
# TODO testcase: passing a file to is_folder() returns false


    # region def test_is_folder_receives_a_valid_path_and_returns_true(...):
    def test_is_folder_receives_a_valid_path_and_returns_true(self):
        """
            dummy test
        """
        # cSpell:disable
        project_folder = "/home/jolitp/Projects/automation_scripts/"
        tests_folder = \
            "src/multiple_files_operations/youtube_upload_viability_without_concatenating/tests/"
        test_bed_folder = "test_bed/"
        this_test_folder = "test_is_folder_receives_a_valid_path_and_returns_true/"

        folder = "valid_folder"
        root_folder = project_folder + tests_folder + test_bed_folder + this_test_folder
        # cSpell:enable

        result = youtube_upload_viability_without_concatenating \
            .is_folder(root_folder, folder)

        self.assertTrue(result)
    # endregion def test_is_folder_receives_a_valid_path_and_returns_true(...):


    # region def test_is_folder_receives_a_relative_path_and_raises_exception(...):
    def test_is_folder_receives_a_relative_path_and_raises_exception(self):
        """
            dummy test
        """
        # cSpell:disable
        project_folder = "project_folder"
        folder = "only_one_folder"
        # cSpell:enable

        with self.assertRaises(ValueError):
            youtube_upload_viability_without_concatenating.is_folder(project_folder, folder)


    # endregion def test_is_folder_receives_a_relative_path_and_raises_exception(...):


# endregion tests is_folder(...):


# TODO testcase: passing a relative path to filter_folders() raise ValueError exception
# TODO testcase: passing a list with only a file inside returns empty list

# region tests filter_folders(...):


    # region def test_filter_folders_receives_1_folder_returns_same_folder(...):
    def test_filter_folders_receives_1_folder_returns_same_folder(self):
        """
            dummy test
        """
        # cSpell:disable
        project_folder = "/home/jolitp/Projects/automation_scripts/"
        # cSpell:enable
        tests_folder = \
            "src/multiple_files_operations/youtube_upload_viability_without_concatenating/tests/"
        test_bed_folder = "test_bed/"
        this_test_folder = "test_filter_folders_receives_1_folder_returns_same_folder/"
        root_folder = project_folder + tests_folder + test_bed_folder + this_test_folder

        all_files_and_folders : set(str) = os.listdir(root_folder)

        expected_result : set(str) = [
            "only_one_folder"
        ]

        folders : set(str) = youtube_upload_viability_without_concatenating \
            .filter_folders(root_folder , all_files_and_folders, debug_function=True)
        self.assertSequenceEqual(folders, expected_result)
    # endregion def test_filter_folders_receives_1_folder_returns_same_folder(...):


# endregion tests filter_folders(...):


# region tests process_folder(...)


# TODO testcase: ...


    # region def test_process_folder(self)
    def test_process_folder(self):
        """
            tests process_folder() function
        """

        ...

    # endregion def test_process_folder(self)

# endregion tests process_folder(...)


if __name__ == "__main__":
    print("integration_tests_module_template.__main__")
    unittest.main()


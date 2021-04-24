#! /usr/bin/python3
"""
    tests for .py
"""

import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "get_all_videos_in_a_directory/"
spec = importlib.util.spec_from_file_location("get_all_videos_in_a_directory",
    python_scripts_folder_path + subfolder + "get_all_videos_in_a_directory.py")
get_all_videos_in_a_directory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_all_videos_in_a_directory)


class IntegrationTest(unittest.TestCase):
    """
        integration tests for get_all_videos_in_a_directory.py
    """
# region tests get_all_videos_in_a_directory(...):


    # region def (...):
    def test_(self):
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

        result = False
        self.assertTrue(result)
    # endregion def (...):


# endregion tests get_all_videos_in_a_directory(...):


if __name__ == "__main__":
    print("get_all_videos_in_a_directory.__main__")
    unittest.main()

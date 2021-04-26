#! /usr/bin/python3
"""
    tests for get_accumulated_length_of_all_videos.py
"""

import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = \
    "src/multiple_files_operations/get_accumulated_length_of_all_videos/"
spec = importlib.util.spec_from_file_location("get_accumulated_length_of_all_videos",
    python_scripts_folder_path + subfolder + "get_accumulated_length_of_all_videos.py")
get_accumulated_length_of_all_videos_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_accumulated_length_of_all_videos_script)




class IntegrationTest(unittest.TestCase):
    """
        integration tests for .py

        CHANGE ME
    """
# region tests CHANGE_ME_function(...):


    # region def CHANGE_ME_test_is_folder_receives_a_valid_path_and_returns_true(...):
    def test_(self):
        """
            dummy test

            CHANGE ME
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
    # endregion def CHANGE_ME_test_is_folder_receives_a_valid_path_and_returns_true(...):


# endregion tests CHANGE_ME_function(...):


if __name__ == "__main__":
    print("CHANGE_ME.__main__")
    unittest.main()

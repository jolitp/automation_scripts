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


# cSpell:disable
PROJECT_FOLDER = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
TESTS_FOLDER = \
"src/multiple_files_operations/get_accumulated_length_of_all_videos/tests/"
TEST_BED_FOLDER = PROJECT_FOLDER +  TESTS_FOLDER + "test_bed/"

DEBUG_TESTS = True
DEBUG_TESTS = False # comment to toggle

class IntegrationTest_get_accumulated_length_of_all_videos(unittest.TestCase):
    """
        integration tests for get_accumulated_length_of_all_videos.py
    """
# region tests IntegrationTest_get_accumulated_length_of_all_videos(...):

# TODO testcase: when given a folder without videos should return 0.0 seconds
# TODO testcase: when given a folder with a corrupted video should return 0.0 seconds
    # region def (...):
    def test_directory_with_a_10_sec_video_should_return_10_seconds(self):
        """
            when giving a directory with only a 10 seconds video
            should return 10 seconds
        """
        # setup
        this_test_folder = "test_directory_with_a_10_sec_video_should_return_10_seconds/"
        folder = TEST_BED_FOLDER + this_test_folder

        # act
        accumulated_length : float = get_accumulated_length_of_all_videos_script \
            .get_accumulated_length_of_all_videos(folder, debug_function=DEBUG_TESTS)
        # assert
        expected : float = 10.0
        self.assertEqual(accumulated_length, expected)
    # endregion def (...):


    # region def (...):
    def test_directory_with_2_10_sec_videos_should_return_20_seconds(self):
        """
            when giving a directory with two 10 seconds videos
            should return 20 seconds
        """
        # setup
        this_test_folder = "test_directory_with_2_10_sec_videos_should_return_20_seconds/"
        folder = TEST_BED_FOLDER + this_test_folder

        # act
        accumulated_length : float = get_accumulated_length_of_all_videos_script \
            .get_accumulated_length_of_all_videos(folder, debug_function=DEBUG_TESTS)
        # assert
        expected : float = 20.0
        self.assertEqual(accumulated_length, expected)
    # endregion def (...):


# endregion tests IntegrationTest_get_accumulated_length_of_all_videos(...):

if __name__ == "__main__":
    print("integration_test_get_accumulated_length_of_all_videos.__main__")
    print()
    unittest.main()

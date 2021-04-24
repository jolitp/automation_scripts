#! /usr/bin/python3
"""
    tests for .py
"""

import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/multiple_files_operations/get_all_videos_in_a_directory/"
spec = importlib.util.spec_from_file_location("get_all_videos_in_a_directory",
    python_scripts_folder_path + subfolder + "get_all_videos_in_a_directory.py")
get_all_videos_in_a_directory_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_all_videos_in_a_directory_script)

DEBUG_TEST = False
# DEBUG_TEST = True # comment to toggle

class IntegrationTest(unittest.TestCase):
    """
        integration tests for get_all_videos_in_a_directory.py
    """
# region tests get_all_videos_in_a_directory(...):


    # region def (...):
    def test_a_folder_with_only_videos_should_return_only_videos(self):
        """
            tests many combinations of valid inputs,
            where the folder has only videos,
            so the result of the filtered list should be equal to the input list.
        """

        # setup
        # cSpell:disable
        project_folder = "/home/jolitp/Projects/automation_scripts/"
        # cSpell:enable
        tests_folder = \
            "src/multiple_files_operations/get_all_videos_in_a_directory/tests/"
        test_bed_folder = "test_bed/"
        this_test_folder = \
        "test_a_folder_with_only_videos_should_return_the_same_list_as_input/"

        root_folder = project_folder + tests_folder + test_bed_folder + this_test_folder

        input_x_expected = [
            (
                root_folder + "only_one_video/",
                [root_folder + "only_one_video/dummy_video.mkv"]
            ),
            (
                root_folder + "two_videos/",
                [
                    root_folder + "two_videos/dummy_video_01.mp4",
                    # cSpell: disable
                    root_folder + "two_videos/dummy_video_02.webm",
                    # cSpell: enable
                ]
            ),
            (
                root_folder + "three_videos/",
                [
                    root_folder + "three_videos/dummy_video_1.avi",
                    # cSpell: disable
                    root_folder + "three_videos/dummy_video_2.rmvb",
                    # cSpell: enable
                    root_folder + "three_videos/dummy_video_3.wmv",
                ]
            )
        ]

        # act
        for param, expected in input_x_expected:
            with self.subTest():
                result = get_all_videos_in_a_directory_script\
                    .get_all_videos(param,debug_function=DEBUG_TEST)
                # self.assertEqual(result, expected)
                self.assertCountEqual(result, expected)
                ...
            ...
        # assert

    # endregion def (...):


# endregion tests get_all_videos_in_a_directory(...):


if __name__ == "__main__":
    print("get_all_videos_in_a_directory.__main__")
    unittest.main()

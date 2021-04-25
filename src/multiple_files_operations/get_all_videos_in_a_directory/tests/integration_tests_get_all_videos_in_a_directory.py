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
DEBUG_TEST = True # comment to toggle

class IntegrationTest_get_all_videos_in_a_directory(unittest.TestCase):
    """
        integration tests for get_all_videos_in_a_directory.py
    """
# region tests get_all_videos_in_a_directory(...):


    # region def test_folders_with_only_videos_should_return_only_videos(...):
    def test_folders_with_only_videos_should_return_only_videos(self):
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

        inputs = [
            root_folder + "only_one_video/",
            root_folder + "two_videos/",
            root_folder + "three_videos/",

        ]

        # cSpell: disable
        expected_values = [
            # expected_values[0]
            [root_folder + "only_one_video/dummy_video.mkv"],
            # expected_values[1]
            [root_folder + "two_videos/dummy_video_01.mp4",
            root_folder + "two_videos/dummy_video_02.webm"],
            # expected_values[2]
            [root_folder + "three_videos/dummy_video_1.avi",
            root_folder + "three_videos/dummy_video_2.rmvb",
            root_folder + "three_videos/dummy_video_3.wmv",]
        ]
        # cSpell: enable

        # act
        for index, _ in enumerate(expected_values):
            with self.subTest():
                param : str = inputs[index]
                expected : list = expected_values[index]
                result = get_all_videos_in_a_directory_script\
                    .get_all_videos(param,debug_function=DEBUG_TEST)
                # self.assertEqual(result, expected)
        # assert
                self.assertCountEqual(result, expected)
                ...
            ...

    # endregion def test_folders_with_only_videos_should_return_only_videos(...):

    # region def (...):
    def test_folders_with_videos_and_a_text_file_should_return_only_videos(self):
        """when giving a directory to get_all_videos(...)
            with videos and a text file inside
            should return only the videos
        """

        # setup
        # cSpell:disable
        project_folder = "/home/jolitp/Projects/automation_scripts/"
        # cSpell:enable
        tests_folder = \
            "src/multiple_files_operations/get_all_videos_in_a_directory/tests/"
        test_bed_folder = "test_bed/"
        this_test_folder = \
        "test_folders_with_videos_and_a_text_file_should_return_only_videos/"

        root_folder = project_folder + tests_folder + test_bed_folder + this_test_folder

        inputs = [
            root_folder + "only_one_video/",
            root_folder + "two_videos/",
            root_folder + "three_videos/",

        ]

        # cSpell: disable
        expected_values = [
            # expected_values[0]
            [root_folder + "only_one_video/dummy_video.mkv"],
            # expected_values[1]
            [root_folder + "two_videos/dummy_video_01.mp4",
            root_folder + "two_videos/dummy_video_02.webm"],
            # expected_values[2]
            [root_folder + "three_videos/dummy_video_1.avi",
            root_folder + "three_videos/dummy_video_2.rmvb",
            root_folder + "three_videos/dummy_video_3.wmv",]
        ]
        # cSpell: enable

        # act
        for index, _ in enumerate(expected_values):
            with self.subTest():
                param : str = inputs[index]
                expected : list = expected_values[index]
                result = get_all_videos_in_a_directory_script\
                    .get_all_videos(param,debug_function=DEBUG_TEST)
                # self.assertEqual(result, expected)
        # assert
                self.assertCountEqual(result, expected)
                ...
            ...


        ...
    # endregion def (...):



    # region def (...):
    def test_folders_with_videos_and_a_directory_should_return_only_videos(self):
        """when giving a directory to get_all_videos(...)
            with videos and a folder inside
            should return only the videos
        """

        # setup
        # cSpell:disable
        project_folder = "/home/jolitp/Projects/automation_scripts/"
        # cSpell:enable
        tests_folder = \
            "src/multiple_files_operations/get_all_videos_in_a_directory/tests/"
        test_bed_folder = "test_bed/"
        this_test_folder = \
        "test_folders_with_videos_and_a_directory_should_return_only_videos/"

        root_folder = project_folder + tests_folder + test_bed_folder + this_test_folder

        inputs = [
            root_folder + "only_one_video/",
            root_folder + "two_videos/",
            root_folder + "three_videos/",

        ]

        # cSpell: disable
        expected_values = [
            # expected_values[0]
            [root_folder + "only_one_video/dummy_video.mkv"],
            # expected_values[1]
            [root_folder + "two_videos/dummy_video_01.mp4",
            root_folder + "two_videos/dummy_video_02.webm"],
            # expected_values[2]
            [root_folder + "three_videos/dummy_video_1.avi",
            root_folder + "three_videos/dummy_video_2.rmvb",
            root_folder + "three_videos/dummy_video_3.wmv",]
        ]
        # cSpell: enable

        # act
        for index, _ in enumerate(expected_values):
            with self.subTest():
                param : str = inputs[index]
                expected : list = expected_values[index]
                result = get_all_videos_in_a_directory_script\
                    .get_all_videos(param,debug_function=DEBUG_TEST)
                # self.assertEqual(result, expected)
        # assert
                self.assertCountEqual(result, expected)
                ...
            ...


        ...
    # endregion def (...):

# endregion tests get_all_videos_in_a_directory(...):


if __name__ == "__main__":
    print("get_all_videos_in_a_directory.__main__")
    unittest.main()

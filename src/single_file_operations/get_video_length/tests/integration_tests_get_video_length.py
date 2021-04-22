#! /usr/bin/python3
"""
    integration tests for get_video_length.py
"""

import unittest
import os
import shutil
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/get_video_length/"
spec = importlib.util.spec_from_file_location("get_video_length",
    python_scripts_folder_path + subfolder + "get_video_length.py")
get_video_length_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_video_length_script)



class IntegrationTest(unittest.TestCase):
    """
        integration tests for get_video_length.py
    """
# region tests (...):

    def copy_video_from_assets_to_test_bed(self,old_name: str, new_name: str):
        """copy a video from the assets/videos/ folder of the project to the test_bed/
        folder of the scripts test

        Args:
            old_name (str): the name of the video file on the assets/videos/ folder
            new_name (str): the name of the file in the test_bed/ folder in the script's test

        returns:
            destination_video_path (str): the full path of the new video file.
        """
        assets_folder : str = python_scripts_folder_path + "assets/"
        # cSpell: disable
        source_video_path : str = assets_folder + "videos/" + old_name
        # cSpell: enable
        test_bed_folder : str = python_scripts_folder_path + subfolder + "tests/test_bed/"
        destination_video_path : str = test_bed_folder + new_name

        shutil.copy(source_video_path, destination_video_path)
        return destination_video_path
        ...

    def clear_test_bed(self):
        """deletes all files in the test bed directory"""
        test_bed_folder: str = python_scripts_folder_path + subfolder + "tests/test_bed/"
        all_files_or_directories: list = os.listdir(test_bed_folder)
        for element in all_files_or_directories:
            shutil.rmtree(element)
            ...
        ...

    # region def CHANGE_ME_test_is_folder_receives_a_valid_path_and_returns_true(...):
    def test_given_a_small_video_should_return_10_seconds(self):
        """
            when given a 10 seconds video, should return 10 seconds
        """

# cSpell: disable
        # setup
        path_to_video = self.copy_video_from_assets_to_test_bed("10_seconds_video.webm",
                                                "10_seconds_video.webm")
        length = get_video_length_script.get_video_length(path_to_video)

        # assert
        expected_length = 10.0
        self.assertEquals(length, expected_length)

        # clean up
        # self.clear_test_bed()
        ...
# TODO testcase: ffmpeg could not be found
# cSpell: enable
    # endregion def CHANGE_ME_test_is_folder_receives_a_valid_path_and_returns_true(...):


# endregion tests (...):


if __name__ == "__main__":
    print("integration_tests_get_video_length.py.__main__")
    unittest.main()

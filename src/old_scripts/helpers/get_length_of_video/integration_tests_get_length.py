#! /usr/bin/python3
"""
    integration tests for remove_special_characters(...) function from helpers module
"""

import unittest
import shutil
import get_length_of_video as script

# FIXME how to actually import the function
# from .. import helpers
# import get_length


class IntegrationTestGetLength(unittest.TestCase):
    """
        tests for remove_special_characters(string) function
    """
# region test class TestGetLength(unittest.TestCase):


    # region def test_dummy(self):
    def test_dummy(self):
        """
            test that the resulting string have one less character
        """

        self.assertEqual(True,True)
        ...
    # endregion def test_dummy(self):


    # region def test_dummy(self):
    def test_function_returns_a_number(self):
        """
            test that the resulting string have one less character
        """
        # cSpell: disable
        scripts_folder = "/home/jolitp/Dropbox/PROJECTS/python-scripts/"
        tests_folder = scripts_folder + "helpers/helpers/tests/"
        # cSpell: enable
        source_video_path : str = tests_folder + "assets/" + "dummy_video.mkv"

        destination_folder : str = "test_bed/"
        destination_path : str = scripts_folder + tests_folder + destination_folder + "working_video.mkv"

        unused_variable = ""
        # shutil.copy(src, dst)



        result : float = script.get_length_of_video("")

        ...
    # endregion def test_dummy(self):

# TODO testcase: everything goes well
# TODO testcase: video is corrupted and value can't be probed
# TODO testcase: file that doesn't exist should raise exception

    ...
# endregion class TestGetLength(unittest.TestCase):


"""
how to test this?

first have a small video laying around, lets say in the folder assets/

before every video copy this video to a test_bed/ folder


"""

if __name__ == "__main__":
    unittest.main()


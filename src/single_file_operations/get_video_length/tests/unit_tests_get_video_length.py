#! /usr/bin/python3
"""
    unit tests for get_video_length.py
"""

import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/get_video_length/"
spec = importlib.util.spec_from_file_location("get_video_length",
    python_scripts_folder_path + subfolder + "get_video_length.py")
get_video_length_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(get_video_length_script)



class UnitTest(unittest.TestCase):
    """
        unit tests for .py

        CHANGE ME
    """
# region tests CHANGE_ME_function(...):


    # region def test_when_filename_is_relative_ValueError_should_be_raised(...):
    def test_when_filename_is_relative_ValueError_should_be_raised(self):
        """
            when filename is relative ValueError should be raised.
        """
        with self.assertRaises(ValueError):
            get_video_length_script.get_video_length("unit_tests_get_video_length.py")
    # endregion def test_when_filename_is_relative_ValueError_should_be_raised(...):



# endregion tests CHANGE_ME_function(...):


if __name__ == "__main__":
    print("CHANGE_ME.__main__")
    unittest.main()


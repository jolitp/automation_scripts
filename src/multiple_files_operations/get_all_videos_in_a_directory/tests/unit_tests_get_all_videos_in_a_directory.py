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


class UnitTest_get_all_videos_in_a_directory(unittest.TestCase):
    """
        unit tests for .py
    """
# region tests (...):


    # region def (...):
    def test_given_a_relative_path_should_raise_ValueError(self):
        """
            when the function get_all_videos_in_a_directory(...)
            is given a relative path it should raise a ValueError exception.
        """
        # setup
        relative_path : str = "path"

        # act
        with self.assertRaises(ValueError) as error:
            get_all_videos_in_a_directory_script \
                .get_all_videos(relative_path)

        # assert
        self.assertTrue("directory_path must be an absolute path" in str(error.exception))

    # endregion def (...):


# endregion tests (...):


if __name__ == "__main__":
    print("get_all_videos_in_a_directory.__main__")
    unittest.main()


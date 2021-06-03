#! /usr/bin/python3
"""
    tests for .py
"""

import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/single_file_operations/is_file_video/"
script_name : str = "is_file_video.py"
full_script_path : str = python_scripts_folder_path + subfolder + script_name
print("Loading module from path : {}".format(full_script_path))
module_name : str = "is_file_video_script"
print("module name : {}".format(module_name))
spec = importlib.util.spec_from_file_location(module_name, full_script_path)
is_file_video_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(is_file_video_script)

print("as {}".format(is_file_video_script))

DEBUG_TESTS = False
DEBUG_TESTS = True   # comment to toggle

class UnitTestIsVideo(unittest.TestCase):
    """
        tests is_video function
    """
# region class TestIsVideo(unittest.TestCase):


    # region def test_filename_has_accepted_extension_should_return_true(self):
    def test_filename_has_accepted_extension_should_return_true(self):
        # setup
# cSpell: disable
        video_extensions = ['.mp4', '.m4v', '.mkv','.ts', '.avi',
                        '.webm', '.flv', '.mov', '.wmv', '.vob',
                        '.ogm', '.mpg', '.divx','.rmvb', '.f4v'
                        ]
# cSpell: enable
        test_name : str = "dummy_video"

        input_x_expected = []
        for extension in video_extensions:
            name = test_name + extension
            element = (name , True)
            input_x_expected.append(element)
            ...
        # act
        for video_name, expected in input_x_expected:
            with self.subTest():
                result : bool = is_file_video_script \
                    .is_video(video_name, debug_function = DEBUG_TESTS)

        # assert
                self.assertEqual(result, expected)
                ...
        ...
    # region def test_filename_has_accepted_extension_should_return_true(self):

# cSpell: disable
    # region def test_video_name_from_real_file_was_not_recognized_but_should_work(self):
    def test_video_name_from_real_file_was_not_recognized_but_should_work(self):
        """
            tests a real world example that should be true
        """

        video_name : str = " 01. Família Dinossauros - O Poderoso Megalossauro.divx"

        is_video : bool = is_file_video_script.is_video(video_name, debug_function = True)

        self.assertTrue(is_video)
        ...
    ...
    # endregion def test_video_name_from_real_file_was_not_recognized_but_should_work(self):
# cSpell: enable


    # region def test_video_name_with_trailing_space(self):
    def test_video_name_with_trailing_space(self):
        """
            tests given a video with trailing space return true
        """

        video_name : str = "video with trailing space.mp4 "

        is_video : bool = is_file_video_script.is_video(video_name, debug_function = True)

        self.assertTrue(is_video)
        ...
    ...
    # endregion def test_video_name_with_trailing_space(self):


    # region def test_video_name_with_trailing_new_line(self):
    def test_video_name_with_trailing_new_line(self):
        """
            tests given a video with trailing new line return true
        """

        video_name : str = "video with trailing new line.mp4\n"

        is_video : bool = is_file_video_script.is_video(video_name, debug_function = True)

        self.assertTrue(is_video)
        ...
    ...
    # endregion def test_video_name_with_trailing_new_line(self):


    # region def test_file_name_is_not_video(self):
    def test_file_name_is_not_video_should_return_false(self):
        """
            tests given a video with trailing new line return true
        """

        video_name : str = "file is not a video.txt"

        is_video : bool = is_file_video_script.is_video(video_name, debug_function = True)

        self.assertFalse(is_video)
        ...
    ...
    # endregion def test_file_name_is_not_video(self):


    # region def test_filename_is_an_absolute_path(self):
    def test_filename_is_an_absolute_path_should_return_false(self):
        """
            tests given a video with trailing new line return true
        """

        video_name : str = "/home/user/videos/filename.mp4"

        is_video : bool = is_file_video_script.is_video(video_name, debug_function = True)

        self.assertTrue(is_video)
        ...
    ...
    # endregion def test_filename_is_an_absolute_path(self):
# endregion class TestIsVideo(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()


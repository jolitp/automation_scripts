#! /usr/bin/python3
"""
    tests get_absolute_path_before_moving_to_directory(...) function from script module
"""

import unittest
import get_absolute_path_before_moving_to_directory as script


class UnitTestGetAbsolutePathAfterMovingToDirectory(unittest.TestCase):
    """
        tests get_absolute_path_before_moving_to_directory() function
    """
# region class TestGetAbsolutePathAfterMovingToDirectory(unittest.TestCase):


    # region def test_(self):
    def test_right_parameters_results_right_return(self):
        """
            test: given a root directory that is absolute path, and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory"
        destination_directory : str = "destination"
        file_or_folder_to_move : str = "video_file.mkv"

        expected_result : str = "/home/user/videos/root_directory/destination/video_file.mkv"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):


    # region def test_(self):
    def test_root_directory_has_trailing_slash(self):
        """
            test: given a root directory that is absolute path with a trailing slash,
                and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory/"
        destination_directory : str = "destination"
        file_or_folder_to_move : str = "video_file.mkv"

        expected_result : str = "/home/user/videos/root_directory/destination/video_file.mkv"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):


    # region def test_(self):
    def test_destination_directory_has_trailing_slash(self):
        """
            test: given a root directory that is absolute path with a trailing slash,
                and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory"
        destination_directory : str = "destination/"
        file_or_folder_to_move : str = "video_file.mkv"

        expected_result : str = "/home/user/videos/root_directory/destination/video_file.mkv"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):


    # region def test_(self):
    def test_folder_to_move_has_trailing_slash(self):
        """
            test: given a root directory that is absolute path with a trailing slash,
                and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory"
        destination_directory : str = "destination"
        file_or_folder_to_move : str = "inside_folder/"

        expected_result : str = "/home/user/videos/root_directory/destination/inside_folder"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):


    # region def test_(self):
    def test_both_destination_directory_and_file_or_folder_to_move_have_trailing_slashes(self):
        """
            test: given a root directory that is absolute path with a trailing slash,
                and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory"
        destination_directory : str = "destination/"
        file_or_folder_to_move : str = "inside_folder/"

        expected_result : str = "/home/user/videos/root_directory/destination/inside_folder"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):


    # region def test_(self):
    def test_both_root_directory_and_file_or_folder_to_move_have_trailing_slashes(self):
        """
            test: given a root directory that is absolute path with a trailing slash,
                and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory/"
        destination_directory : str = "destination"
        file_or_folder_to_move : str = "inside_folder/"

        expected_result : str = "/home/user/videos/root_directory/destination/inside_folder"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):


    # region def test_(self):
    def test_both_root_directory_and_destination_directory_have_trailing_slashes(self):
        """
            test: given a root directory that is absolute path with a trailing slash,
                and both other parameters
                relative paths to directories in the root directory, result should be
                root directory + / + destination_directory + / + file_or_folder_to_move
        """

        root_directory : str = "/home/user/videos/root_directory/"
        destination_directory : str = "destination/"
        file_or_folder_to_move : str = "inside_folder"

        expected_result : str = "/home/user/videos/root_directory/destination/inside_folder"

        actual_result : str = script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                            destination_directory,
                                                                            file_or_folder_to_move,
                                                                            debug_function=True)

        self.assertEqual(expected_result, actual_result)
        ...
    # endregion def test_(self):

    # region def test_root_directory_relative_path_raises_ValueError(self):
    def test_root_directory_relative_path_raises_value_error(self):
        """
            test: if root_directory is not absolute path raise exception ValueError
        """

        root_directory : str = "root_directory"
        destination_directory : str = "destination"
        file_or_folder_to_move : str = "inside_folder"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)

            ...
        ...
        self.assertEqual(str(error.exception), 'root_directory is not absolute path')
    # endregion def test_root_directory_relative_path_raises_ValueError(self):


    # region def test_destination_directory_relative_path_raises_value_error(self):
    def test_destination_directory_relative_path_raises_value_error(self):
        """
            test: if destination_directory is absolute path raise exception ValueError
        """

        root_directory : str = "/home/user/videos/root_directory"
        file_or_folder_to_move : str = "inside_folder"
        destination_directory : str = "/destination"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)
            ...
        ...
        self.assertEqual(str(error.exception), 'destination_directory is absolute path')
    # endregion def test_destination_directory_relative_path_raises_value_error(self):


    # region def test_file_or_folder_to_move_relative_path_raises_value_error(self):
    def test_file_or_folder_to_move_relative_path_raises_value_error(self):
        """
            test: if file_or_folder_to_move is absolute path raise exception ValueError
        """

        root_directory : str = "/home/user/videos/root_directory"
        file_or_folder_to_move : str = "/inside_folder"
        destination_directory : str = "destination"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)
            ...
        ...
        self.assertEqual(str(error.exception), 'file_or_folder_to_move is absolute path')
    # endregion def test_file_or_folder_to_move_relative_path_raises_value_error(self):


    # region def test_file_or_folder_to_move_relative_path_raises_value_error(self):
    def test_root_directory_relative_path_with_double_dots_raises_value_error(self):
        """
        test: if root_directory is absolute with ../ at the start path raise exception ValueError
        """

        root_directory : str = "../home/user/videos/root_directory"
        file_or_folder_to_move : str = "inside_folder"
        destination_directory : str = "destination"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)
            ...
        ...
        self.assertEqual(str(error.exception), 'root_directory is not absolute path')
    # endregion def test_file_or_folder_to_move_relative_path_raises_value_error(self):


    # region def test_file_or_folder_to_move_relative_path_raises_value_error(self):
    def test_file_or_folder_to_move_relative_path_with_double_dots_raises_value_error(self):
        """
            test: if file_or_folder_to_move is absolute path raise exception ValueError
        """

        root_directory : str = "/home/user/videos/root_directory"
        file_or_folder_to_move : str = "../inside_folder"
        destination_directory : str = "destination"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)
            ...
        ...
        self.assertEqual(str(error.exception), 'found ../ in result path, that is not supported')
    # endregion def test_file_or_folder_to_move_relative_path_raises_value_error(self):


# region def test_destination_directory_relative_path_with_double_dots_raises_value_error(self):
    def test_destination_directory_relative_path_with_double_dots_raises_value_error(self):
        """
            test: if destination_directory is absolute path raise exception ValueError
        """

        root_directory : str = "/home/user/videos/root_directory"
        file_or_folder_to_move : str = "inside_folder"
        destination_directory : str = "../destination"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)
            ...
        ...
        self.assertEqual(str(error.exception), 'found ../ in result path, that is not supported')
# endregion def test_destination_directory_relative_path_with_double_dots_raises_value_error(self):


# region def test_destination_directory_relative_path_with_double_dots_raises_value_error(self):
    def test_2_parameters_are_relative_path_with_double_dots_raises_value_error(self):
        """
            test: if destination_directory is absolute path raise exception ValueError
        """

        root_directory : str = "/home/user/videos/root_directory"
        file_or_folder_to_move : str = "../inside_folder"
        destination_directory : str = "../destination"

        with self.assertRaises(ValueError) as error:
            script.get_absolute_path_before_moving_to_directory(root_directory,
                                                                destination_directory,
                                                                file_or_folder_to_move,
                                                                debug_function=True)
            ...
        ...
        self.assertEqual(str(error.exception), 'found ../ in result path, that is not supported')
# endregion def test_destination_directory_relative_path_with_double_dots_raises_value_error(self):


# DONE test when root_directory is in the format ../something
# DONE test when file_or_folder_to_move is in the format ../something
# DONE test when destination_directory is in the format ../something
# TODO handle the case where 2 of the parameters have ../something

# TODO test when file_or_folder_to_move have more than one element like folder/inside_folder
# should raise exception
# TODO test when destination_directory have more than one element like folder/inside_folder
# should raise exception



    ...
# endregion class TestGetAbsolutePathAfterMovingToDirectory(unittest.TestCase):



if __name__ == "__main__":
    unittest.main()


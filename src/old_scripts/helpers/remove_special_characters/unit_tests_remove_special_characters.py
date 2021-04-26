#! /usr/bin/python3
"""
    tests remove_special_characters(...) function from helpers module
"""

import unittest
import remove_special_characters as script



class UnitTestRemoveSpecialCharacters(unittest.TestCase):
    """
        tests for remove_special_characters(string) function
    """
# region test class TestRemoveSpecialCharacters(unittest.TestCase):


    # region def test_string_does_not_contain_special_characters(self):
    def test_string_does_not_contain_special_characters(self):
        """
            test that the resulting string is the same as the original string if
            the original string does not have any special characters
        """

        original_string : str = "does not contain special characters"
        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(original_string, resulting_string)
        ...
    # endregion def test_string_does_not_contain_special_characters(self):


    # region def test_string_does_contain_1_backslash_character(self):
    def test_string_does_contain_1_backslash_character(self):
        """
            test that the resulting string is the same as the original string if
            the original string does not have any special characters
        """

        original_string : str = "contains 1 \\ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_backslash_character(self):


    # region def test_string_does_contain_1_double_quote_character(self):
    def test_string_does_contain_1_double_quote_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 \" character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_double_quote_character(self):


    # region def test_string_does_contain_1_single_quote_character(self):
    def test_string_does_contain_1_single_quote_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 \' character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_single_quote_character(self):


    # region def test_string_does_contain_1_pipe_character(self):
    def test_string_does_contain_1_pipe_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 | character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_pipe_character(self):


    # region def test_string_does_contain_1_open_parenthesis_character(self):
    def test_string_does_contain_1_open_parenthesis_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ( character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_open_parenthesis_character(self):


    # region def test_string_does_contain_1_close_parenthesis_character(self):
    def test_string_does_contain_1_close_parenthesis_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ) character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_close_parenthesis_character(self):


    # region def test_string_does_contain_1_tilde_character(self):
    def test_string_does_contain_1_tilde_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ~ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_tilde_character(self):


    # region def test_string_does_contain_1_backtick_character(self):
    def test_string_does_contain_1_backtick_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ` character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_backtick_character(self):


    # region def test_string_does_contain_1_pound_character(self):
    def test_string_does_contain_1_pound_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 # character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_pound_character(self):


    # region def test_string_does_contain_1_at_character(self):
    def test_string_does_contain_1_at_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 @ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_at_character(self):


    # region def test_string_does_contain_1_exclamation_point_character(self):
    def test_string_does_contain_1_exclamation_point_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ! character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_exclamation_point_character(self):


    # region def test_string_does_contain_1_dollar_sign_character(self):
    def test_string_does_contain_1_dollar_sign_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 $ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_dollar_sign_character(self):


    # region def test_string_does_contain_1_percentage_sign_character(self):
    def test_string_does_contain_1_percentage_sign_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 $ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_percentage_sign_character(self):


    # region def test_string_does_contain_1_caret_sign_character(self):
    def test_string_does_contain_1_caret_sign_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ^ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_caret_sign_character(self):


    # region def test_string_does_contain_1_ampersand_character(self):
    def test_string_does_contain_1_ampersand_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 & character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_ampersand_character(self):


    # region def test_string_does_contain_1_asterisk_character(self):
    def test_string_does_contain_1_asterisk_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 * character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_asterisk_character(self):


    # region def test_string_does_contain_1_open_bracket_character(self):
    def test_string_does_contain_1_open_bracket_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 [ character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_open_bracket_character(self):


    # region def test_string_does_contain_1_close_bracket_character(self):
    def test_string_does_contain_1_close_bracket_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ] character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_close_bracket_character(self):


    # region def test_string_does_contain_1_open_curly_bracket_character(self):
    def test_string_does_contain_1_open_curly_bracket_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 { character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_open_curly_bracket_character(self):


    # region def test_string_does_contain_1_close_curly_bracket_character(self):
    def test_string_does_contain_1_close_curly_bracket_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 } character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_close_curly_bracket_character(self):


    # region def test_string_does_contain_1_semicolon_character(self):
    def test_string_does_contain_1_semicolon_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ; character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_semicolon_character(self):


    # region def test_string_does_contain_1_colon_character(self):
    def test_string_does_contain_1_colon_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 : character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_colon_character(self):


    # region def test_string_does_contain_1_open_angle_bracket_character(self):
    def test_string_does_contain_1_open_angle_bracket_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 < character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_open_angle_bracket_character(self):


    # region def test_string_does_contain_1_close_angle_bracket_character(self):
    def test_string_does_contain_1_close_angle_bracket_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 } character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_close_angle_bracket_character(self):


    # region def test_string_does_contain_1_interrogation_point_character(self):
    def test_string_does_contain_1_interrogation_point_character(self):
        """
            test that the resulting string have one less character
        """

        original_string : str = "contains 1 ? character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_interrogation_point_character(self):


    # region def test_string_does_contain_1_interrogation_point_character(self):
    def test_string_does_contain_2_special_characters(self):
        """
            test that the resulting string have two less characters
        """

        original_string : str = "contains$ 1 ? character"

        expected_result : str = "contains 1  character"

        resulting_string : str = \
            script.remove_special_characters(original_string, debug_function = True)

        self.assertEqual(expected_result, resulting_string)
        ...
    # endregion def test_string_does_contain_1_interrogation_point_character(self):


    ...
# endregion class TestRemoveSpecialCharacters(unittest.TestCase):



if __name__ == "__main__":
    unittest.main()

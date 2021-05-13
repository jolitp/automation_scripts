"""
    test
"""
import unittest
import separate_videos_in_parts as script


class TestSeparateVideosInParts(unittest.TestCase):

    """
        tests
    """

    def test_list_has_one_element(self):
        """
            test_list_has_one_element
        """

        list_of_files = [
            "only one file.mkv"
        ]

        expected_dict = {
            "only one file": [
                "only one file.mkv"
            ]
        }


        sections = script.get_sections(list_of_files)
        print(sections)

        self.assertDictEqual(sections, expected_dict)
        ...


    def test_list_has_two_elements_both_in_same_section(self):
        """
            test_list_has_two_elements_both_in_same_section
        """

        list_of_files = [
            "file one.mkv",
            "file two.mkv",
        ]

        expected_dict = {
            "file ": [
                "file two.mkv",
                "file one.mkv",
            ]
        }

        sections = script.get_sections(list_of_files)

        self.assertDictEqual(sections, expected_dict)
        ...


    ...


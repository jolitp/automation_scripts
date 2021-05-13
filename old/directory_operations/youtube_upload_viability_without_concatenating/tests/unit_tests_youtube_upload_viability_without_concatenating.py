#! /usr/bin/python3
"""
    unit tests for youtube_upload_viability_without_concatenating.py
"""

import os
import unittest
import importlib.util # needed for importing scripts using the scripts path

# cSpell:disable
python_scripts_folder_path : str = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
subfolder : str = "src/directory_operations/youtube_upload_viability_without_concatenating/"
spec = importlib.util.spec_from_file_location("youtube_upload_viability_without_concatenating",
    python_scripts_folder_path + subfolder + "youtube_upload_viability_without_concatenating.py")
youtube_upload_viability_without_concatenating_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(youtube_upload_viability_without_concatenating_script)

# cSpell:disable
PROJECT_FOLDER = "/home/jolitp/Projects/automation_scripts/"
# cSpell:enable
TESTS_FOLDER = \
    "src/directory_operations/youtube_upload_viability_without_concatenating/tests/"
TEST_BED_FOLDER = PROJECT_FOLDER + TESTS_FOLDER + "test_bed/"


# region class IntegrationTest(unittest.TestCase):

class UnitTestsYoutubeUploadViabilityWithoutConcatenating(unittest.TestCase):
    """
        unit tests for youtube_upload_viability_without_concatenating.py
    """

    def test_when_passing_less_than_16_videos_to_is_viable_should_return_1(self):
        """
            when passing a list of videos that has less than 16 videos inside

            the result from is_viable should always be 1
        """

        # setup
        list_of_args = []
        for index, n in enumerate(range(15)):
            args = []
            for number in range(index + 1):
                args.append(number)
            list_of_args.append(args)
        for args in list_of_args:
            for index, item in enumerate(args):
                args[index] = str(item) + ".mkv"
        # for arg in list_of_args:
            # print(arg)

        # act
        for index, args in enumerate(list_of_args):
            result = youtube_upload_viability_without_concatenating_script \
                .is_viable(args)
            ...
        # assert
            self.assertEqual(result, 1)

        ...







if __name__ == "__main__":
    print("integration_tests_module_template.__main__")
    unittest.main()



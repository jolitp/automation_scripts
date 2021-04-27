#! /usr/bin/python3
"""
    tests for youtube_upload_viability_without_concatenating.py
"""

import os
import shutil
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

class IntegrationTestYoutubeUploadViabilityWithoutConcatenating(unittest.TestCase):
    """
        integration tests for youtube_upload_viability_without_concatenating.py
    """

    def test_having_a_directory_with_one_video_moves_the_folder_to_viable_folder(self):
        """
            when having a folder with one video inside

            should move the folder into a folder named [upload_now]/
        """
        # setup

        this_test_folder = \
            "test_having_a_directory_with_one_video_moves_the_folder_to_viable_folder/"
        folder = "folder_with_one_video/"
        root_path = TEST_BED_FOLDER + this_test_folder

        video_filename = "dummy_video.mkv"

        os.chdir(root_path)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        os.chdir(folder)
        if not os.path.isfile(video_filename):
            file = open(video_filename, "w")
            file.close()

        # act
        youtube_upload_viability_without_concatenating_script \
            .process_folder(root_path, folder, debug_function=True)

        # assert
        upload_now_folder = root_path + "[upload_now]/"
        result_folder = upload_now_folder + folder

        upload_now_folder_exists = os.path.isdir(upload_now_folder)
        print("upload_now_folder_exists : " + str(upload_now_folder_exists))
        os.chdir(upload_now_folder)
        folder_was_moved = os.path.isdir(result_folder)
        print("folder was moved : " + str(folder_was_moved))
        self.assertTrue(upload_now_folder_exists and folder_was_moved)

        # cleanup
        shutil.rmtree(upload_now_folder)
        ...


if __name__ == "__main__":
    print("integration_tests_module_template.__main__")
    unittest.main()


#! /usr/bin/python3
"""
    tests filter_videos(...) function from helpers module
"""

import unittest
# from helpers import filter_videos
# import helpers.filter_videos
import filter_videos as script

class UnitTestFilterVideos(unittest.TestCase):
    """
        test filter_video function
    """
# region class TestFilterVideos(unittest.TestCase):


    # region def test_1_video_from_1_file(self):
    def test_1_video_from_1_file(self):
        """
            test: given one file return one video
        """

        files : set(str) = {
            "single video.mp4"
        }

        expected_result : set(str) = {
            "single video.mp4"
        }

        videos : set(str) = script.filter_videos(files, debug_function=True)

        self.assertSequenceEqual(videos, expected_result)
        ...
    # endregion def test_1_video_from_1_file(self):


    # region def test_1_video_from_11_files(self):
    def test_1_video_from_11_files(self):
        """
            test: given one file return one video
        """

        files : set(str) = {
            "single video.mp4",
            "1st non video file.txt",
            "2nd non video file.txt",
            "3rd non video file.txt",
            "4th non video file.txt",
            "5th non video file.txt",
            "6th non video file.txt",
            "7th non video file.txt",
            "8th non video file.txt",
            "9th non video file.txt",
            "10th non video file.txt",
        }

        expected_result : set(str) = {
            "single video.mp4"
        }

        videos : set(str) = script.filter_videos(files, debug_function=True)

        self.assertSequenceEqual(videos, expected_result)
        ...
    ...
    # endregion def test_1_video_from_11_files(self):


    # region def test_2_videos_from_11_files(self):
    def test_2_videos_from_11_files(self):
        """
            test: given one file return one video
        """

        files : set(str) = [
            "1st video.mp4",
            "2nd video.mp4",
            "1st non video file.txt",
            "2nd non video file.txt",
            "3rd non video file.txt",
            "4th non video file.txt",
            "5th non video file.txt",
            "6th non video file.txt",
            "7th non video file.txt",
            "8th non video file.txt",
            "9th non video file.txt",
        ]

        expected_result : set(str) = {
            "1st video.mp4",
            "2nd video.mp4",
        }

        videos : set(str) = script.filter_videos(files, debug_function=True)

        self.assertSequenceEqual(videos, expected_result)
        ...
    ...
    # endregion def test_2_videos_from_11_files(self):


    # region def test_0_videos_from_1_file(self):
    def test_0_videos_from_1_file(self):
        """
            test: given one file return one video
        """

        files : list(str) = [
            "1st not video.csv",
            "2nd not video.txt",
        ]

        expected_result : set(str) = set()

        videos : set(str) = script.filter_videos(files, debug_function=True)

        self.assertSequenceEqual(videos, expected_result)
        ...
    ...
    # endregion def test_0_videos_from_1_file(self):


    # region def test_lists_should_equal_even_if_order_does_not_match(self):
    def test_lists_should_equal_even_if_order_does_not_match(self):
        """
            test: given one file return one video
        """

        files : set(str) = {
            "1st video.mp4",
            "2nd video.mp4",
        }

        expected_result : set(str) = {
            "2nd video.mp4",
            "1st video.mp4",
        }

        videos : set(str) = script.filter_videos(files, debug_function=True)

        self.assertSequenceEqual(videos, expected_result)
        ...
    ...
    # endregion def test_lists_should_equal_even_if_order_does_not_match(self):
# endregion TestFilterVideos(unittest.TestCase):


if __name__ == "__main__":
    unittest.main()

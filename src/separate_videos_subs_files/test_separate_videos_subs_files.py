#! /usr/bin/env python3
"""
tests for separate_videos_subs_files.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import separate_videos_subs_files as script

USERNAME = getpass.getuser()
PROJECT_FOLDER = Path("/home/") / USERNAME / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER / "src" / "separate_videos_subs_files" / "test_bed"



# region test_filter_subtitles_should_return_the_same_subtitles
#cSpell:words ttml dfxp
@pytest.mark.parametrize(
    "subtitle_files, expected_result", [
    # setup
        ( [ "subtitle.srt" ] , [ "subtitle.srt" ] ),
        ( [ "subtitle.vtt" ] , [ "subtitle.vtt" ] ),
        ( [ "subtitle.ssa" ] , [ "subtitle.ssa" ] ),
        ( [ "subtitle.ttml" ] , [ "subtitle.ttml" ] ),
        ( [ "subtitle.sbv" ] , [ "subtitle.sbv" ] ),
        ( [ "subtitle.dfxp" ] , [ "subtitle.dfxp" ] ),
    ]
)
def test_filter_subtitles_should_return_the_same_subtitles(
    subtitle_files, expected_result
):
    # act
    filtered_subtitles = script \
        .filter_subtitles(subtitle_files)

    # assert
    assert sorted(filtered_subtitles) == sorted(expected_result)
    ...
# endregion test_filter_subtitles_should_return_the_same_subtitles



# region test_filter_subtitles_should_return_the_same_subtitles_without_the_text_file
#cSpell:words webm vchd rmvb gifv xvid vidx
@pytest.mark.parametrize(
    "subtitle_files, expected_result", [
    # setup
        ( [ "subtitle.srt" , "video.mp4" ] , [ "subtitle.srt" ] ),
        ( [ "subtitle.vtt" , "video.mp4" ] , [ "subtitle.vtt" ] ),
        ( [ "subtitle.ssa" , "video.mp4" ] , [ "subtitle.ssa" ] ),
        ( [ "subtitle.ttml" , "video.mp4" ] , [ "subtitle.ttml" ] ),
        ( [ "subtitle.sbv" , "video.mp4" ] , [ "subtitle.sbv" ] ),
        ( [ "subtitle.dfxp" , "video.mp4" ] , [ "subtitle.dfxp" ] ),
    ]
)
# region
def test_filter_subtitles_should_return_the_same_subtitles_without_the_video_file(
    subtitle_files, expected_result
):
    # act
    filtered_subtitles = script \
        .filter_subtitles(subtitle_files)

    # assert
    assert sorted(filtered_subtitles) == sorted(expected_result)
    ...
# endregion test_filter_subtitles_should_return_the_same_subtitles_without_the_text_file



# region test_filter_videos_should_return_the_same_videos

#cSpell:words webm vchd rmvb gifv xvid vidx
@pytest.mark.parametrize(
    "video_files, expected_result", [
    # setup
        ( [ "video.WEBM" ] , [ "video.WEBM" ] ),
        ( [ "video.MPG" ]  , [ "video.MPG" ] ),
        ( [ "video.MP2" ]  , [ "video.MP2" ] ),
        ( [ "video.MPEG" ] , [ "video.MPEG" ] ),
        ( [ "video.MPE" ]  , [ "video.MPE" ] ),
        ( [ "video.MPV" ]  , [ "video.MPV" ] ),
        ( [ "video.OGV" ]  , [ "video.OGV" ] ),
        ( [ "video.OGG" ]  , [ "video.OGG" ] ),
        ( [ "video.MP4" ]  , [ "video.MP4" ] ),
        ( [ "video.M4P" ]  , [ "video.M4P" ] ),
        ( [ "video.M4V" ]  , [ "video.M4V" ] ),
        ( [ "video.AVI" ]  , [ "video.AVI" ] ),
        ( [ "video.WMV" ]  , [ "video.WMV" ] ),
        ( [ "video.MOV" ]  , [ "video.MOV" ] ),
        ( [ "video.QT" ]   , [ "video.QT" ] ),
        ( [ "video.FLV" ]  , [ "video.FLV" ] ),
        ( [ "video.SWF" ]  , [ "video.SWF" ] ),
        ( [ "video.F4V" ]  , [ "video.F4V" ] ),
        ( [ "video.F4P" ]  , [ "video.F4P" ] ),
        ( [ "video.F4A" ]  , [ "video.F4A" ] ),
        ( [ "video.F4B" ]  , [ "video.F4B" ] ),
        ( [ "video.VCHD" ] , [ "video.VCHD" ] ),
        ( [ "video.RMVB" ] , [ "video.RMVB" ] ),
        ( [ "video.RM" ]   , [ "video.RM" ] ),
        ( [ "video.VOB" ]  , [ "video.VOB" ] ),
        ( [ "video.MKV" ]  , [ "video.MKV" ] ),
        ( [ "video.MTS" ]  , [ "video.MTS" ] ),
        ( [ "video.M2TS" ] , [ "video.M2TS" ] ),
        ( [ "video.TS" ]   , [ "video.TS" ] ),
        ( [ "video.MNG" ]  , [ "video.MNG" ] ),
        ( [ "video.GIFV" ] , [ "video.GIFV" ] ),
        ( [ "video.GIF" ]  , [ "video.GIF" ] ),
        ( [ "video.DRC" ]  , [ "video.DRC" ] ),
        ( [ "video.XVID" ] , [ "video.XVID" ] ),
        ( [ "video.VIDX" ] , [ "video.VIDX" ] ),
        ( [ "video.ASF" ]  , [ "video.ASF" ] ),
        ( [ "video.AMV" ]  , [ "video.AMV" ] ),
        ( [ "video.MPG" ]  , [ "video.MPG" ] ),
        ( [ "video.MPEG" ] , [ "video.MPEG" ] ),
        ( [ "video.M2V" ]  , [ "video.M2V" ] ),
        ( [ "video.SVI" ]  , [ "video.SVI" ] ),
        ( [ "video.3GP" ]  , [ "video.3GP" ] ),
        ( [ "video.MXF" ]  , [ "video.MXF" ] ),
        ( [ "video.ROQ" ]  , [ "video.ROQ" ] ),
        ( [ "video.NSV" ]  , [ "video.NSV" ] ),
        ( [ "video.3G2" ]  , [ "video.3G2" ] ),
    ]
)
def test_filter_videos_should_return_the_same_videos(
    video_files, expected_result
):
    # act
    filtered_videos = script \
        .filter_videos(video_files)

    # assert
    assert sorted(filtered_videos) == sorted(expected_result)
    ...
# endregion test_filter_videos_should_return_the_same_videos


# region test_filter_videos_should_return_the_same_videos_without_the_text_file
#cSpell:words webm vchd rmvb gifv xvid vidx
@pytest.mark.parametrize(
    "video_files, expected_result", [
    # setup
        ( [ "video.WEBM", "text.txt" ] , [ "video.WEBM" ] ),
        ( [ "video.MPG", "text.txt" ]  , [ "video.MPG" ] ),
        ( [ "video.MP2", "text.txt" ]  , [ "video.MP2" ] ),
        ( [ "video.MPEG", "text.txt" ] , [ "video.MPEG" ] ),
        ( [ "video.MPE", "text.txt" ]  , [ "video.MPE" ] ),
        ( [ "video.MPV", "text.txt" ]  , [ "video.MPV" ] ),
        ( [ "video.OGV", "text.txt" ]  , [ "video.OGV" ] ),
        ( [ "video.OGG", "text.txt" ]  , [ "video.OGG" ] ),
        ( [ "video.MP4", "text.txt" ]  , [ "video.MP4" ] ),
        ( [ "video.M4P", "text.txt" ]  , [ "video.M4P" ] ),
        ( [ "video.M4V", "text.txt" ]  , [ "video.M4V" ] ),
        ( [ "video.AVI", "text.txt" ]  , [ "video.AVI" ] ),
        ( [ "video.WMV", "text.txt" ]  , [ "video.WMV" ] ),
        ( [ "video.MOV", "text.txt" ]  , [ "video.MOV" ] ),
        ( [ "video.QT", "text.txt" ]   , [ "video.QT" ] ),
        ( [ "video.FLV", "text.txt" ]  , [ "video.FLV" ] ),
        ( [ "video.SWF", "text.txt" ]  , [ "video.SWF" ] ),
        ( [ "video.F4V", "text.txt" ]  , [ "video.F4V" ] ),
        ( [ "video.F4P", "text.txt" ]  , [ "video.F4P" ] ),
        ( [ "video.F4A", "text.txt" ]  , [ "video.F4A" ] ),
        ( [ "video.F4B", "text.txt" ]  , [ "video.F4B" ] ),
        ( [ "video.VCHD", "text.txt" ] , [ "video.VCHD" ] ),
        ( [ "video.RMVB", "text.txt" ] , [ "video.RMVB" ] ),
        ( [ "video.RM", "text.txt" ]   , [ "video.RM" ] ),
        ( [ "video.VOB", "text.txt" ]  , [ "video.VOB" ] ),
        ( [ "video.MKV", "text.txt" ]  , [ "video.MKV" ] ),
        ( [ "video.MTS", "text.txt" ]  , [ "video.MTS" ] ),
        ( [ "video.M2TS", "text.txt" ] , [ "video.M2TS" ] ),
        ( [ "video.TS", "text.txt" ]   , [ "video.TS" ] ),
        ( [ "video.MNG", "text.txt" ]  , [ "video.MNG" ] ),
        ( [ "video.GIFV", "text.txt" ] , [ "video.GIFV" ] ),
        ( [ "video.GIF", "text.txt" ]  , [ "video.GIF" ] ),
        ( [ "video.DRC", "text.txt" ]  , [ "video.DRC" ] ),
        ( [ "video.XVID", "text.txt" ] , [ "video.XVID" ] ),
        ( [ "video.VIDX", "text.txt" ] , [ "video.VIDX" ] ),
        ( [ "video.ASF", "text.txt" ]  , [ "video.ASF" ] ),
        ( [ "video.AMV", "text.txt" ]  , [ "video.AMV" ] ),
        ( [ "video.MPG", "text.txt" ]  , [ "video.MPG" ] ),
        ( [ "video.MPEG", "text.txt" ] , [ "video.MPEG" ] ),
        ( [ "video.M2V", "text.txt" ]  , [ "video.M2V" ] ),
        ( [ "video.SVI", "text.txt" ]  , [ "video.SVI" ] ),
        ( [ "video.3GP", "text.txt" ]  , [ "video.3GP" ] ),
        ( [ "video.MXF", "text.txt" ]  , [ "video.MXF" ] ),
        ( [ "video.ROQ", "text.txt" ]  , [ "video.ROQ" ] ),
        ( [ "video.NSV", "text.txt" ]  , [ "video.NSV" ] ),
        ( [ "video.3G2", "text.txt" ]  , [ "video.3G2" ] ),
    ]
)
def test_filter_videos_should_return_the_same_videos_without_the_text_file(
    video_files, expected_result
):
    # act
    filtered_videos = script \
        .filter_videos(video_files)


    # assert
    assert sorted(filtered_videos) == sorted(expected_result)
    ...
# endregion test_filter_videos_should_return_the_same_videos_without_the_text_file


# region test_get_files_should_return_expected_files
test_get_files_should_return_expected_files_folder = TEST_BED_FOLDER_PATH \
    / "test_get_files_should_return_expected_files/"
@pytest.mark.parametrize(
    "folder,expected_files", [
    # setup
    # test
    ("no_files_nor_folders", [],),
    # test
    ("no_files_one_folder", [],),
    # test
    ("no_files_two_folders", [],),
    # test
    ("one_file_no_folders",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "one_file_no_folders" + "/" + \
    "single_file"],),
    # test
    ("one_file_one_folder",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "one_file_one_folder" + "/" + \
    "single_file"],),
    # test
    ("two_files_no_folders",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_no_folders" + "/" + \
    "file_one",
    str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_no_folders" + "/" + \
    "file_two"],),
    # test
    ("two_files_one_folder",
    [str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_one_folder" + "/" + \
    "file_one",
    str(test_get_files_should_return_expected_files_folder) + "/" + \
    "two_files_one_folder" + "/" + \
    "file_two"],),
])
def test_get_files_should_return_expected_files(
    folder, expected_files
    ):
    """
    do a battery of test with files in nested folders,
    should return the expected values.

    not event testing with videos, just generic files.
    """
    # act
    print("folder: \n" + str(folder))
    print("expected_files: \n" + str(expected_files))
    full_path = str(test_get_files_should_return_expected_files_folder) + "/" + str(folder)

    print("full path: \n" + str(full_path))
    files_in_folder = script \
        .get_nested_files(full_path)
    print("files in folder: " + str(files_in_folder))

    # assert
    assert len(files_in_folder) == len(expected_files)
    assert sorted(files_in_folder) == sorted(expected_files)
# endregion


# region test_filter_files_by_extension_should_return_expected_values
@pytest.mark.parametrize("files, extensions, expected", [
    # setup

    # test
    ([],[],[]),
    # test
    (["text.txt"],["txt"],["text.txt"]
    ),
    # test
    (["text.txt", "no_extension_file"],
    ["txt"],
    ["text.txt"],
    ),
    # test
    (["/home/user/absolute_path_file.txt"],
    ["txt"],
    ["/home/user/absolute_path_file.txt"],
    ),
    # test
    (["text.txt", "file_with_close_extension.tx"],
    ["txt"],
    ["text.txt"],
    ),
    # test
    (["text.txt", "file_with_close_extension._txt"],
    ["txt"],
    ["text.txt"],
    ),
    # test
    (["text.txt"],
    ["TXT"],
    ["text.txt"],
    )
])
def test_filter_files_by_extension_should_return_expected_values(
    files, extensions, expected
):
    """
    do a battery of tests with lists of files and lists of extensions.
    should return expected values.
    """
    # act
    result = script \
        .filter_files_by_extension(files, extensions)

    # assert
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])
# endregion


if __name__ == "__main__":
    unittest.main()

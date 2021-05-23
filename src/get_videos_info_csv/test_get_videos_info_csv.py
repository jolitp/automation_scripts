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
PROJECT_FOLDER \
    = Path("/home/") \
        / USERNAME \
        / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
        / "src" \
        / "get_videos_info_csv" \
        / "test_bed"

def test_dummy():
    assert True

if __name__ == "__main__":
    unittest.main()

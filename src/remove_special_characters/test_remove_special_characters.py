#! /usr/bin/env python3
"""
tests for remove_special_characters.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import remove_special_characters as script

USERNAME = getpass.getuser()
PROJECT_FOLDER \
    = Path("/home/") \
        / USERNAME \
        / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
        / "src" \
        / "concatenate_videos" \
        / "test_bed"

def test_dummy():
    assert True

if __name__ == "__main__":
    unittest.main()


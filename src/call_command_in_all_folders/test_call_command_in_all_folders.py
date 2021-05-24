#! /usr/bin/env python3
"""
tests for call_command_in_all_folders.py
"""
#cSpell:words pytest jolitp

import unittest
import pytest
from pathlib import Path
import getpass

import call_command_in_all_folders as script

USERNAME = getpass.getuser()
PROJECT_FOLDER \
    = Path("/home/") \
        / USERNAME \
        / "Projects/automation_scripts/"
TEST_BED_FOLDER_PATH = \
    PROJECT_FOLDER \
        / "src" \
        / "call_command_in_all_folders" \
        / "test_bed"

def test_dummy():
    assert True

if __name__ == "__main__":
    unittest.main()



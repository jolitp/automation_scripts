#! /usr/bin/python3
"""
    tests for
"""

import unittest
# import helpers
# from helpers_save_for_reference.tests.scaffold_tests import function
import sys
sys.path.insert(0,'..')
# cSpell: disable
# pylint: disable=wrong-import-position
# cSpell: enable
import helpers

# cSpell: disable
# pylint: disable=no-member
helpers.function("parameter", debug_function=True)
# cSpell: enable


# test function scaffold


#     # region def test_(self):
#     def test_(self):
#         """

#         """

#         files : set(str) = {
#         }

#         expected_result : set(str) = {
#         }

#         videos : set(str) = helpers.filter_videos(files, debug_function=True)

#         self.assertSequenceEqual(videos, expected_result)



# region class IntegrationTest(unittest.TestCase):

#     # region def test_dummy(self):
#     def test_dummy(self):
#         """
#             dummy test
#         """

#         files : set(str) = {
#             "a.mkv"
#         }

#         expected_result : set(str) = {
#             "a.mkv"
#         }

#         videos : set(str) = helpers.filter_videos(files, debug_function=True)

#         self.assertSequenceEqual(videos, expected_result)
# #     # endregion def test_dummy(self):



# test class scaffold

# # region test
# class TestFirst(unittest.TestCase):
#     """

#     """


#     # region def test_(self):
#     def test_(self):
#         """

#         """

#         files : set(str) = {
#         }

#         expected_result : set(str) = {
#         }

#         videos : set(str) = helpers.filter_videos(files, debug_function=True)

#         self.assertSequenceEqual(videos, expected_result)


#         ...
#     # endregion def test_(self):
#     ...
# # endregion TestFirst(unittest.TestCase):

if __name__ == "__main__":
    print("unit_tests_module_template.__main__")
    unittest.main()

